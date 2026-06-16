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
        print("FAIL: output_generation_enabled is not true; robots.txt generation not authorized")
        sys.exit(1)

    robots_content = """User-agent: *
Allow: /
Disallow: /site/
Disallow: /site/data/
Disallow: /site/page-sources/
Disallow: /.git/
Sitemap: https://strongavatar.com/sitemap.xml
"""

    output_path = root / "output" / "robots.txt"
    output_path.write_text(robots_content, encoding="utf-8")
    print("PASS: robots.txt generated")


if __name__ == "__main__":
    main()
