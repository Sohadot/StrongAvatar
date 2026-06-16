from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from validation_utils import fail, load_json, pass_message, repo_root


W_TO_C_REQUIRED: dict[str, list[str]] = {
    "/weakness/consent-absence/":      ["/component/consent-infrastructure/"],
    "/weakness/provenance-void/":      ["/component/provenance-credentials/"],
    "/weakness/disclosure-failure/":   ["/component/disclosure-layer/"],
    "/weakness/identity-drift/":       ["/component/scope-usage-binding/"],
    "/weakness/impersonation-exposure/": ["/component/anti-impersonation-controls/"],
    "/weakness/rights-ambiguity/":     ["/component/rights-chain-documentation/"],
    "/weakness/revocation-gap/":       ["/component/revocation-mechanism/"],
    "/weakness/context-collapse/":     ["/component/scope-usage-binding/"],
    "/weakness/attribution-loss/":     ["/component/attribution-binding/"],
    "/weakness/robustness-weakness/":  ["/component/provenance-credentials/"],
}

C_TO_W_REQUIRED: dict[str, list[str]] = {
    "/component/consent-infrastructure/":    ["/weakness/consent-absence/"],
    "/component/provenance-credentials/":    ["/weakness/provenance-void/", "/weakness/robustness-weakness/"],
    "/component/disclosure-layer/":          ["/weakness/disclosure-failure/"],
    "/component/scope-usage-binding/":       ["/weakness/identity-drift/", "/weakness/context-collapse/"],
    "/component/anti-impersonation-controls/": ["/weakness/impersonation-exposure/"],
    "/component/rights-chain-documentation/": ["/weakness/rights-ambiguity/"],
    "/component/revocation-mechanism/":      ["/weakness/revocation-gap/"],
    "/component/attribution-binding/":       ["/weakness/attribution-loss/"],
}

PROHIBITED_CONTENT_TERMS = [
    "todo", "tbd", "lorem ipsum", "coming soon", "affiliate",
    "google analytics", "google tag manager", "tracking pixel",
]

JAVASCRIPT_EXTENSIONS = {".js", ".mjs", ".cjs", ".jsx", ".ts", ".tsx"}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico", ".avif"}


def html_path_to_route(output_dir: Path, html_path: Path) -> str:
    """Convert output/weakness/consent-absence/index.html to /weakness/consent-absence/."""
    rel = html_path.relative_to(output_dir)
    parts = rel.parts
    if len(parts) == 1 and parts[0] == "index.html":
        return "/"
    # Remove trailing index.html
    if parts[-1] == "index.html":
        parts = parts[:-1]
    return "/" + "/".join(parts) + "/"


def extract_links_from_html(html: str) -> list[str]:
    """Extract all href values from <a href="..."> tags."""
    return re.findall(r'<a\s[^>]*href="([^"]*)"', html)


def is_internal_route(href: str) -> bool:
    return href.startswith("/") and not href.startswith("//")


def is_anchor(href: str) -> bool:
    return href.startswith("#")


def main() -> None:
    root = repo_root()
    errors: list[str] = []

    # Check 1: launch_set.json flags
    ls_path = root / "site" / "data" / "launch_set.json"
    if not ls_path.exists():
        fail("site/data/launch_set.json does not exist")
    try:
        launch_set = json.loads(ls_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"site/data/launch_set.json is not valid JSON: {exc}")

    if launch_set.get("output_generation_enabled") is not True:
        fail("output_generation_enabled must be true for output integrity validation")
    if launch_set.get("public_generation_enabled") is not True:
        errors.append("public_generation_enabled must be true")
    if launch_set.get("indexing_enabled") is not True:
        errors.append("indexing_enabled must be true")
    if launch_set.get("monetization_enabled") is not False:
        errors.append("monetization_enabled must be false")
    if launch_set.get("diagnostic_engine_enabled") is not False:
        errors.append("diagnostic_engine_enabled must be false")
    if launch_set.get("javascript_enabled") is not False:
        errors.append("javascript_enabled must be false")
    if launch_set.get("external_assets_enabled") is not False:
        errors.append("external_assets_enabled must be false")

    allowed_routes: set[str] = set(launch_set.get("allowed_routes", []))
    output_dir = root / "output"

    # Check 3: output/index.html exists
    if not (output_dir / "index.html").exists():
        errors.append("output/index.html does not exist")

    # Check 4: output/sitemap.xml exists
    if not (output_dir / "sitemap.xml").exists():
        errors.append("output/sitemap.xml does not exist")

    # Check 5: output/robots.txt exists
    if not (output_dir / "robots.txt").exists():
        errors.append("output/robots.txt does not exist")

    # Check 13: output/static/css/main.css exists and matches source
    src_css = root / "site" / "static" / "css" / "main.css"
    dst_css = output_dir / "static" / "css" / "main.css"
    if not dst_css.exists():
        errors.append("output/static/css/main.css does not exist")
    elif src_css.exists() and dst_css.read_bytes() != src_css.read_bytes():
        errors.append("output/static/css/main.css is not identical to site/static/css/main.css")

    # Check 11: no .js files in output/
    js_files = [p for p in output_dir.rglob("*") if p.is_file() and p.suffix.lower() in JAVASCRIPT_EXTENSIONS]
    if js_files:
        found = ", ".join(str(p.relative_to(root)) for p in js_files)
        errors.append(f"JavaScript files found in output/: {found}")

    # Check 12: no image files in output/
    img_files = [p for p in output_dir.rglob("*") if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS]
    if img_files:
        found = ", ".join(str(p.relative_to(root)) for p in img_files)
        errors.append(f"image files found in output/: {found}")

    # Check 14: no unauthorized CSS in output/
    css_files = [p for p in output_dir.rglob("*.css") if p.is_file()]
    authorized_output_css = {(output_dir / "static" / "css" / "main.css").resolve()}
    for css_file in css_files:
        if css_file.resolve() not in authorized_output_css:
            errors.append(f"unauthorized CSS file in output/: {css_file.relative_to(root)}")

    # Collect all HTML files in output/
    html_files = [p for p in output_dir.rglob("*.html") if p.is_file()]

    # Check 2 & 6: every launch_set route has output HTML; no HTML for routes outside launch_set
    html_routes: set[str] = set()
    for html_file in html_files:
        route = html_path_to_route(output_dir, html_file)
        html_routes.add(route)

    # Check 2: every route in launch_set has output HTML
    for route in sorted(allowed_routes):
        if route not in html_routes:
            errors.append(f"launch_set route {route} has no generated HTML in output/")

    # Check 6: no HTML for routes outside launch_set
    for route in sorted(html_routes):
        if route not in allowed_routes:
            errors.append(f"output HTML exists for non-launch-set route: {route}")

    # Per-HTML-file checks
    for html_file in sorted(html_files):
        route = html_path_to_route(output_dir, html_file)
        html = html_file.read_text(encoding="utf-8")
        html_lower = html.lower()
        rel_path = str(html_file.relative_to(root))

        # Check 7a: has <title>
        if "<title>" not in html_lower:
            errors.append(f"{rel_path}: missing <title>")

        # Check 7b: has <meta name="description"
        if '<meta name="description"' not in html_lower:
            errors.append(f"{rel_path}: missing <meta name=\"description\">")

        # Check 7c: has <link rel="canonical"
        if '<link rel="canonical"' not in html_lower:
            errors.append(f"{rel_path}: missing <link rel=\"canonical\">")

        # Check 7d: has <meta name="robots"
        if '<meta name="robots"' not in html_lower:
            errors.append(f"{rel_path}: missing <meta name=\"robots\">")

        # Check 7e: exactly 1 <h1>
        h1_count = len(re.findall(r"<h1[^>]*>", html_lower))
        if h1_count != 1:
            errors.append(f"{rel_path}: expected exactly 1 <h1>, found {h1_count}")

        # Check 7f: no <script
        if "<script" in html_lower:
            errors.append(f"{rel_path}: contains <script> tag")

        # Check 8: canonical URL matches route
        expected_canonical = f'href="https://strongavatar.com{route}"'
        if expected_canonical not in html:
            errors.append(f"{rel_path}: canonical href does not match expected https://strongavatar.com{route}")

        # Check 10: no prohibited content terms
        for term in PROHIBITED_CONTENT_TERMS:
            if term in html_lower:
                errors.append(f"{rel_path}: contains prohibited term: {term}")

        # Check 9: internal links point only to launch_set routes or anchors
        links = extract_links_from_html(html)
        for link in links:
            if is_anchor(link):
                continue
            if is_internal_route(link):
                # Strip anchor from link
                link_route = link.split("#")[0]
                if link_route not in allowed_routes:
                    errors.append(f"{rel_path}: internal link to non-launch-set route: {link_route}")

    # Check 15: sitemap.xml contains only launch_set routes
    sitemap_path = output_dir / "sitemap.xml"
    if sitemap_path.exists():
        sitemap_content = sitemap_path.read_text(encoding="utf-8")
        sitemap_locs = re.findall(r"<loc>(https://strongavatar\.com([^<]*?))</loc>", sitemap_content)
        sitemap_routes = {path for _, path in sitemap_locs}
        # Normalize: ensure trailing slash
        for sr in sitemap_routes:
            sr_normalized = sr if sr.endswith("/") else sr + "/"
            if sr_normalized not in allowed_routes and sr not in allowed_routes:
                errors.append(f"sitemap.xml contains non-launch-set route: {sr}")
        for route in allowed_routes:
            expected_url = f"https://strongavatar.com{route}"
            if expected_url not in sitemap_content:
                errors.append(f"sitemap.xml missing route: {route}")

    # Check 16: robots.txt references sitemap
    robots_path = output_dir / "robots.txt"
    if robots_path.exists():
        robots_content = robots_path.read_text(encoding="utf-8")
        if "https://strongavatar.com/sitemap.xml" not in robots_content:
            errors.append("robots.txt does not reference https://strongavatar.com/sitemap.xml")

        # Check 17: robots.txt does not expose internal paths insecurely
        # It should Disallow /site/ etc - having Disallow is good, not bad
        if "Sitemap: https://strongavatar.com/sitemap.xml" not in robots_content:
            errors.append("robots.txt missing Sitemap directive")

    # Check 18: homepage links to /ontology/, /standard/, /protocol/
    homepage_path = output_dir / "index.html"
    if homepage_path.exists():
        homepage_html = homepage_path.read_text(encoding="utf-8")
        for hub_route in ["/ontology/", "/standard/", "/protocol/"]:
            if f'href="{hub_route}"' not in homepage_html:
                errors.append(f"homepage (index.html) does not link to {hub_route}")

    # Check 19: /ontology/, /standard/, /protocol/ link back to /
    for hub in ["/ontology/", "/standard/", "/protocol/"]:
        hub_html_path = output_dir / hub.strip("/") / "index.html"
        if hub_html_path.exists():
            hub_html = hub_html_path.read_text(encoding="utf-8")
            if 'href="/"' not in hub_html:
                errors.append(f"{hub} page does not link to /")

    # Check 20: W-class pages link to primary C-component
    for w_route, required_c_list in W_TO_C_REQUIRED.items():
        if w_route not in allowed_routes:
            continue
        parts = w_route.strip("/").split("/")
        w_html_path = output_dir / Path(*parts) / "index.html"
        if w_html_path.exists():
            w_html = w_html_path.read_text(encoding="utf-8")
            for required_c in required_c_list:
                if f'href="{required_c}"' not in w_html:
                    errors.append(f"{w_route} page does not link to required component {required_c}")

    # Check 21: C-component pages link to their W-classes
    for c_route, required_w_list in C_TO_W_REQUIRED.items():
        if c_route not in allowed_routes:
            continue
        parts = c_route.strip("/").split("/")
        c_html_path = output_dir / Path(*parts) / "index.html"
        if c_html_path.exists():
            c_html = c_html_path.read_text(encoding="utf-8")
            for required_w in required_w_list:
                if f'href="{required_w}"' not in c_html:
                    errors.append(f"{c_route} page does not link to required weakness {required_w}")

    # Check 22: non-launch-set pages in pages.json must remain indexable=false, publication_allowed=false
    pages_data = load_json("site/data/pages.json")
    for page in pages_data.get("pages", []):
        slug = page.get("slug")
        if slug not in allowed_routes:
            if page.get("indexable") is True:
                errors.append(f"non-launch-set page {slug} has indexable=true in pages.json")
            if page.get("publication_allowed") is True:
                errors.append(f"non-launch-set page {slug} has publication_allowed=true in pages.json")

    if errors:
        fail("; ".join(errors))

    pass_message("output integrity: all 22 generated HTML files verified, sitemap and robots valid")


if __name__ == "__main__":
    main()
