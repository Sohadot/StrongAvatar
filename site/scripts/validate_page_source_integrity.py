from __future__ import annotations

import json
import re
from pathlib import Path

from validation_utils import fail, load_json, pass_message, repo_root

PROHIBITED_TERMS = [
    "todo", "tbd", "lorem ipsum", "coming soon", "placeholder page",
    "fake source", "sample content", "example content",
]
PROHIBITED_REFS = [
    "javascript", "google analytics", "google tag manager", "tracking pixel",
    "tracking pixels", "external cdn", "cdn", "gtm", "ga4", "webxr", "webgl",
    "affiliate", "sponsored placement", "ad slot", "monetization script",
]
MONETIZATION_TERMS = [
    "buy now", "purchase", "subscribe now", "payment", "pricing plan",
    "affiliate link", "sponsored",
]

# Route→C-component mapping: W-class slug → required C-component slug
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

# Route→W-class mapping: C-component slug → required W-class slugs
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

HUB_ROUTES = {"/ontology/", "/standard/", "/protocol/"}


def extract_frontmatter_route(text: str) -> str | None:
    """Extract route: value from YAML frontmatter block."""
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return None
    for line in match.group(1).splitlines():
        if line.startswith("route:"):
            return line.split(":", 1)[1].strip()
    return None


def extract_markdown_links(text: str) -> list[str]:
    """Return all href values from markdown links: [text](href)."""
    return re.findall(r"\[(?:[^\[\]]*)\]\(([^)]+)\)", text)


def is_internal_route(href: str) -> bool:
    return href.startswith("/") and not href.startswith("//")


def is_anchor(href: str) -> bool:
    return href.startswith("#")


def main() -> None:
    root = repo_root()
    errors: list[str] = []

    # ── Load launch_set.json ─────────────────────────────────────────────────
    launch_set_path = root / "site" / "data" / "launch_set.json"
    if not launch_set_path.exists():
        fail("site/data/launch_set.json does not exist")
    try:
        launch_set = json.loads(launch_set_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"site/data/launch_set.json is not valid JSON: {exc}")

    # Check 2: output_generation_enabled must be false
    if launch_set.get("output_generation_enabled") is not False:
        errors.append("launch_set.json output_generation_enabled must be false in prebuild alignment phase")

    allowed_routes: set[str] = set(launch_set.get("allowed_routes", []))

    # ── Load pages.json routes ───────────────────────────────────────────────
    pages_data = load_json("site/data/pages.json")
    registered_routes: set[str] = {p["slug"] for p in pages_data.get("pages", [])}

    # Check 3: every allowed route must exist in pages.json
    for route in sorted(allowed_routes):
        if route not in registered_routes:
            errors.append(f"launch_set allowed route not in pages.json: {route}")

    # ── Scan page-sources directory ──────────────────────────────────────────
    page_sources_dir = root / "site" / "page-sources"
    source_files = sorted(page_sources_dir.rglob("*.md"))
    route_to_file: dict[str, Path] = {}
    file_to_route: dict[Path, str] = {}

    for source_file in source_files:
        text = source_file.read_text(encoding="utf-8")
        route = extract_frontmatter_route(text)
        if not route:
            errors.append(f"page source missing frontmatter route: {source_file.relative_to(root)}")
            continue
        # Check 5: source route must be in pages.json
        if route not in registered_routes:
            errors.append(f"page source route not registered in pages.json: {route} ({source_file.relative_to(root)})")
        route_to_file[route] = source_file
        file_to_route[source_file] = route

    # Check 4: every allowed route must have a source file
    for route in sorted(allowed_routes):
        if route not in route_to_file:
            errors.append(f"launch_set route has no page source file: {route}")

    # Check 12: homepage source must exist
    if "/" not in route_to_file:
        errors.append("homepage source (route: /) not found in site/page-sources/")

    # ── Per-file content checks ──────────────────────────────────────────────
    for source_file in source_files:
        text = source_file.read_text(encoding="utf-8")
        lower = text.lower()
        route = file_to_route.get(source_file, "<unknown>")
        ctx = f"{source_file.relative_to(root)} ({route})"

        # Check 9: no prohibited placeholder terms
        for term in PROHIBITED_TERMS:
            if term in lower:
                errors.append(f"{ctx}: contains prohibited term: {term!r}")

        # Check 10: no monetization activation
        for term in MONETIZATION_TERMS:
            if term in lower:
                errors.append(f"{ctx}: contains monetization language: {term!r}")

        # Check 11: no JS/analytics/external refs
        for ref in PROHIBITED_REFS:
            if ref in lower:
                errors.append(f"{ctx}: contains prohibited reference: {ref!r}")

        # Check 6, 7, 8: validate all Markdown links
        links = extract_markdown_links(text)
        for href in links:
            if is_anchor(href):
                continue  # same-page anchors are always OK
            if not is_internal_route(href):
                # External links — allowed in source (they go in source notes)
                # but flag if they look like JS/tracking
                if any(bad in href.lower() for bad in ["javascript:", "data:"]):
                    errors.append(f"{ctx}: link uses prohibited scheme: {href}")
                continue
            # Internal route — strip anchor if present
            internal_route = href.split("#")[0]
            if not internal_route:
                continue
            # Check 6 + 8: must be a registered route
            if internal_route not in registered_routes:
                errors.append(f"{ctx}: internal link points to unregistered route: {internal_route}")
            # Check 7: if file is in launch_set, link target must also be in launch_set or be /
            if route in allowed_routes:
                if internal_route not in allowed_routes and internal_route != "/":
                    errors.append(
                        f"{ctx}: launch-set source links to non-launch-set route: {internal_route}"
                    )

        # Check 13: homepage must link to /ontology/, /standard/, /protocol/
        if route == "/":
            all_links = set(
                href.split("#")[0] for href in links if is_internal_route(href)
            )
            for required in ["/ontology/", "/standard/", "/protocol/"]:
                if required not in all_links:
                    errors.append(f"homepage source missing required link to {required}")

        # Check 14: hub pages must link back to /
        if route in HUB_ROUTES:
            all_links = set(
                href.split("#")[0] for href in links if is_internal_route(href)
            )
            if "/" not in all_links:
                errors.append(f"{ctx}: hub page does not link back to /")

        # Check 15: W-class pages must link to their primary C-component
        if route in W_TO_C_REQUIRED:
            all_links = set(
                href.split("#")[0] for href in links if is_internal_route(href)
            )
            for required_c in W_TO_C_REQUIRED[route]:
                if required_c not in all_links:
                    errors.append(
                        f"{ctx}: W-class page missing required C-component link: {required_c}"
                    )

        # Check 16: C-component pages must link to their remediated W-classes
        if route in C_TO_W_REQUIRED:
            all_links = set(
                href.split("#")[0] for href in links if is_internal_route(href)
            )
            for required_w in C_TO_W_REQUIRED[route]:
                if required_w not in all_links:
                    errors.append(
                        f"{ctx}: C-component page missing required W-class link: {required_w}"
                    )

    if errors:
        fail("; ".join(errors))

    pass_message(
        f"page source integrity confirmed: {len(route_to_file)} sources, "
        f"{len(allowed_routes)} launch-set routes, all links registered and closed"
    )


if __name__ == "__main__":
    main()
