from __future__ import annotations

import json
import sys
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def main() -> None:
    root = repo_root()

    # Load launch_set.json
    ls_path = root / "site" / "data" / "launch_set.json"
    if not ls_path.exists():
        print("FAIL: site/data/launch_set.json does not exist")
        sys.exit(1)
    try:
        launch_set = json.loads(ls_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"FAIL: site/data/launch_set.json is not valid JSON: {exc}")
        sys.exit(1)

    if launch_set.get("output_generation_enabled") is not True:
        print("FAIL: output_generation_enabled is not true; sitemap generation not authorized")
        sys.exit(1)

    allowed_routes: list[str] = launch_set.get("allowed_routes", [])

    # Load pages.json to confirm indexable
    pages_path = root / "site" / "data" / "pages.json"
    try:
        pages_data = json.loads(pages_path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"FAIL: could not load pages.json: {exc}")
        sys.exit(1)

    slug_to_page = {p["slug"]: p for p in pages_data.get("pages", [])}

    base_url = "https://strongavatar.com"
    sitemap_routes: list[str] = []
    errors: list[str] = []

    for route in allowed_routes:
        page = slug_to_page.get(route)
        if not page:
            errors.append(f"route {route} not found in pages.json")
            continue
        if not page.get("indexable"):
            errors.append(f"route {route} is not indexable in pages.json")
            continue

        # Confirm output HTML exists
        if route == "/":
            html_path = root / "output" / "index.html"
        else:
            parts = route.strip("/").split("/")
            html_path = root / "output" / Path(*parts) / "index.html"

        if not html_path.exists():
            errors.append(f"route {route}: output HTML not found at {html_path.relative_to(root)}")
            continue

        sitemap_routes.append(route)

    if errors:
        for err in errors:
            print(f"FAIL: {err}")
        sys.exit(1)

    # Generate sitemap XML
    xml_lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml_lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for route in sitemap_routes:
        url = base_url + route
        xml_lines.append(f"  <url><loc>{url}</loc></url>")
    xml_lines.append("</urlset>")
    sitemap_xml = "\n".join(xml_lines) + "\n"

    output_path = root / "output" / "sitemap.xml"
    output_path.write_text(sitemap_xml, encoding="utf-8")
    print(f"PASS: sitemap.xml generated with {len(sitemap_routes)} URLs")


if __name__ == "__main__":
    main()
