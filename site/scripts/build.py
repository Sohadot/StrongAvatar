from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_launch_set(root: Path) -> dict:
    path = root / "site" / "data" / "launch_set.json"
    if not path.exists():
        print("FAIL: site/data/launch_set.json does not exist")
        sys.exit(1)
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"FAIL: site/data/launch_set.json is not valid JSON: {exc}")
        sys.exit(1)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Parse YAML frontmatter and return (fields_dict, body_text)."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", text, re.DOTALL)
    if not match:
        return {}, text
    fm_text = match.group(1)
    body = match.group(2)
    fields: dict[str, str] = {}
    for line in fm_text.splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    return fields, body


def escape_html(text: str) -> str:
    """Escape & and < in text content."""
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    return text


def markdown_to_html(md: str) -> str:
    """Convert Markdown body to HTML. Handles headings, hr, tables, lists, links, bold, code, paragraphs."""
    lines = md.splitlines()
    html_parts: list[str] = []
    i = 0
    in_list = False
    in_table = False

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            html_parts.append("</ul>")
            in_list = False

    def close_table() -> None:
        nonlocal in_table
        if in_table:
            html_parts.append("</tbody></table>")
            in_table = False

    def inline(text: str) -> str:
        """Process inline Markdown: links, bold, code."""
        # Links: [text](url)
        def replace_link(m: re.Match) -> str:
            link_text = m.group(1)
            href = m.group(2)
            return f'<a href="{href}">{link_text}</a>'
        text = re.sub(r"\[([^\[\]]*)\]\(([^)]+)\)", replace_link, text)
        # Bold: **text**
        text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
        # Code: `text`
        text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
        return text

    def is_table_separator(line: str) -> bool:
        """Check if line is a table separator like |---|---|."""
        stripped = line.strip()
        if not stripped.startswith("|"):
            return False
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        return all(re.match(r"^[-:]+$", c) for c in cells if c)

    def parse_table_row(line: str) -> list[str]:
        stripped = line.strip().strip("|")
        return [cell.strip() for cell in stripped.split("|")]

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Heading 3
        if stripped.startswith("### "):
            close_list()
            close_table()
            text = escape_html(stripped[4:])
            html_parts.append(f"<h3>{inline(text)}</h3>")
            i += 1
            continue

        # Heading 2
        if stripped.startswith("## "):
            close_list()
            close_table()
            text = escape_html(stripped[3:])
            html_parts.append(f"<h2>{inline(text)}</h2>")
            i += 1
            continue

        # Heading 1
        if stripped.startswith("# "):
            close_list()
            close_table()
            text = escape_html(stripped[2:])
            html_parts.append(f"<h1>{inline(text)}</h1>")
            i += 1
            continue

        # Horizontal rule
        if stripped == "---":
            close_list()
            close_table()
            html_parts.append("<hr>")
            i += 1
            continue

        # Table row
        if stripped.startswith("|"):
            if is_table_separator(stripped):
                i += 1
                continue
            cells = parse_table_row(stripped)
            if not in_table:
                # First row is header
                close_list()
                html_parts.append("<table><thead><tr>")
                for cell in cells:
                    html_parts.append(f"<th>{inline(escape_html(cell))}</th>")
                html_parts.append("</tr></thead><tbody>")
                in_table = True
            else:
                html_parts.append("<tr>")
                for cell in cells:
                    html_parts.append(f"<td>{inline(escape_html(cell))}</td>")
                html_parts.append("</tr>")
            i += 1
            continue

        # Unordered list item
        if stripped.startswith("- "):
            close_table()
            if not in_list:
                html_parts.append("<ul>")
                in_list = True
            text = escape_html(stripped[2:])
            html_parts.append(f"<li>{inline(text)}</li>")
            i += 1
            continue

        # Empty line
        if stripped == "":
            close_list()
            close_table()
            i += 1
            continue

        # Paragraph
        close_list()
        close_table()
        text = escape_html(stripped)
        html_parts.append(f"<p>{inline(text)}</p>")
        i += 1

    close_list()
    close_table()
    return "\n".join(html_parts)


HTML_TEMPLATE = """\
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{meta_description}">
  <link rel="canonical" href="{canonical}">
  <meta name="robots" content="index, follow">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{meta_description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{meta_description}">
  <link rel="stylesheet" href="/static/css/main.css">
</head>
<body class="site-shell" data-interface="violet-gold-identity-field">
  <a class="skip-link" href="#main-content">Skip to main content</a>
  <div class="site-shell__page">
    <header class="site-shell__header" role="banner">
      <nav class="site-nav" aria-label="Site navigation">
        <a class="site-nav__brand" href="/">StrongAvatar.com</a>
        <ul class="site-nav__list">
          <li><a href="/ontology/">Ontology</a></li>
          <li><a href="/standard/">Standard</a></li>
          <li><a href="/protocol/">Protocol</a></li>
        </ul>
      </nav>
    </header>
    <main id="main-content" class="site-shell__main page-shell" tabindex="-1">
      <div class="page-shell__content protocol-card">
        {body_html}
      </div>
    </main>
    <aside class="site-shell__trust" aria-label="Source and methodology context">
      <p class="trust-note">StrongAvatar.com is a governance reference layer. Content reflects internal doctrine and methodology. External claims require documented sources before publication.</p>
    </aside>
    <footer class="site-shell__footer">
      <nav class="footer-nav" aria-label="Footer navigation">
        <a href="/">StrongAvatar.com</a>
        <a href="/ontology/">Ontology</a>
        <a href="/standard/">Standard</a>
        <a href="/protocol/">Protocol</a>
      </nav>
      <p class="footer-legal">&#169; 2026 StrongAvatar.com. Avatar governance reference layer.</p>
    </footer>
  </div>
</body>
</html>"""


def route_to_output_path(root: Path, route: str) -> Path:
    """Convert a route like /weakness/consent-absence/ to output/weakness/consent-absence/index.html."""
    if route == "/":
        return root / "output" / "index.html"
    # Strip leading/trailing slashes
    parts = route.strip("/").split("/")
    return root / "output" / Path(*parts) / "index.html"


def scan_page_sources(root: Path) -> dict[str, Path]:
    """Build route -> file mapping from all page-source files."""
    page_sources_dir = root / "site" / "page-sources"
    route_to_file: dict[str, Path] = {}
    for source_file in sorted(page_sources_dir.rglob("*.md")):
        text = source_file.read_text(encoding="utf-8")
        match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
        if not match:
            continue
        for line in match.group(1).splitlines():
            if line.startswith("route:"):
                route = line.split(":", 1)[1].strip()
                route_to_file[route] = source_file
                break
    return route_to_file


def main() -> None:
    root = repo_root()
    launch_set = load_launch_set(root)

    if not launch_set.get("output_generation_enabled"):
        print("FAIL: output_generation_enabled is false; HTML generation is not authorized")
        sys.exit(1)
    if not launch_set.get("public_generation_enabled"):
        print("FAIL: public_generation_enabled is false; HTML generation is not authorized")
        sys.exit(1)

    allowed_routes: list[str] = launch_set.get("allowed_routes", [])
    if not allowed_routes:
        print("FAIL: no allowed_routes in launch_set.json")
        sys.exit(1)

    # Scan page sources
    route_to_file = scan_page_sources(root)

    errors: list[str] = []
    generated: list[str] = []

    for route in allowed_routes:
        if route not in route_to_file:
            errors.append(f"no page source found for route: {route}")
            continue

        source_file = route_to_file[route]
        text = source_file.read_text(encoding="utf-8")
        fields, body = parse_frontmatter(text)

        title = fields.get("title", "")
        meta_description = fields.get("meta_description", "")
        canonical = fields.get("canonical", "")

        if not title:
            errors.append(f"route {route}: missing title in frontmatter")
        if not meta_description:
            errors.append(f"route {route}: missing meta_description in frontmatter")
        if not canonical:
            errors.append(f"route {route}: missing canonical in frontmatter")

        body_html = markdown_to_html(body)

        html = HTML_TEMPLATE.format(
            title=title,
            meta_description=meta_description,
            canonical=canonical,
            body_html=body_html,
        )

        output_path = route_to_output_path(root, route)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(html, encoding="utf-8")
        generated.append(str(output_path.relative_to(root)))

    if errors:
        for err in errors:
            print(f"FAIL: {err}")
        sys.exit(1)

    # Copy CSS
    src_css = root / "site" / "static" / "css" / "main.css"
    dst_css = root / "output" / "static" / "css" / "main.css"
    dst_css.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(str(src_css), str(dst_css))

    print(f"PASS: generated {len(generated)} HTML files")
    for path in sorted(generated):
        print(f"  {path}")
    print(f"  output/static/css/main.css (copied)")


if __name__ == "__main__":
    main()
