from __future__ import annotations

import json
from pathlib import Path

from validation_utils import assert_all_site_data_json_valid, fail, list_non_gitkeep_files, load_pages, pass_message, repo_root


DISALLOWED_QUALITY_STATUSES = {"approved", "published"}


def _load_launch_set(root: Path) -> dict:
    ls = root / "site" / "data" / "launch_set.json"
    if not ls.exists():
        return {}
    try:
        return json.loads(ls.read_text(encoding="utf-8"))
    except Exception:
        return {}


def main() -> None:
    assert_all_site_data_json_valid()
    errors: list[str] = []

    root = repo_root()
    launch_set = _load_launch_set(root)
    gen_auth = (
        launch_set.get("output_generation_enabled") is True
        and launch_set.get("public_generation_enabled") is True
    )
    ls_routes: set[str] = set(launch_set.get("allowed_routes", []))

    content_files = list_non_gitkeep_files("site/content")
    if content_files:
        errors.append("content files exist before governance is ready: " + ", ".join(str(path) for path in content_files))

    for page in load_pages():
        slug = page.get("slug", "<missing slug>")
        is_launch_set = slug in ls_routes

        if page.get("status") == "published":
            errors.append(f"page {slug} is published")

        if gen_auth and is_launch_set:
            # Launch-set pages are allowed to be indexable when generation is authorized
            pass
        else:
            if page.get("indexable") is True:
                errors.append(f"page {slug} is indexable")

        if page.get("status") in {"reserved", "planned"} and page.get("quality_status") in DISALLOWED_QUALITY_STATUSES:
            errors.append(f"page {slug} has premature quality_status: {page.get('quality_status')}")

    if errors:
        fail("; ".join(errors))

    pass_message("thin-page prevention confirms no public content or indexable pages")


if __name__ == "__main__":
    main()
