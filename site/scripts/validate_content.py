from __future__ import annotations

import json
from pathlib import Path

from validation_utils import assert_all_site_data_json_valid, fail, list_non_gitkeep_files, load_pages, pass_message, repo_root


REQUIRED_PAGE_KEYS = [
    "slug",
    "title",
    "status",
    "indexable",
    "publication_allowed",
    "template_planned",
    "strategic_purpose",
    "seo_cluster",
    "buyer_logic_role",
    "monetization_role",
    "required_links",
    "source_requirement",
    "quality_status",
    "notes",
]

PLACEHOLDER_TERMS = ["lorem ipsum", "coming soon", "todo", "tbd", "placeholder"]


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
        errors.append("site/content contains public content files: " + ", ".join(str(path) for path in content_files))

    for page in load_pages():
        context = f"page {page.get('slug', '<missing slug>')}"
        for key in REQUIRED_PAGE_KEYS:
            if key not in page:
                errors.append(f"{context} missing required governance field: {key}")

        slug = page.get("slug")
        is_launch_set = slug in ls_routes

        if page.get("status") == "published":
            errors.append(f"{context} is marked published")

        if gen_auth and is_launch_set:
            # Launch-set pages are allowed to have publication_allowed: true and indexable: true
            pass
        else:
            if page.get("publication_allowed") is True:
                errors.append(f"{context} has publication_allowed true")
            if page.get("indexable") is True:
                errors.append(f"{context} has indexable true")

        page_text = " ".join(str(value) for value in page.values()).lower()
        for term in PLACEHOLDER_TERMS:
            if term in page_text:
                errors.append(f"{context} contains placeholder wording: {term}")

    if errors:
        fail("; ".join(errors))

    pass_message("content registry and reserved content directories remain non-publishing")


if __name__ == "__main__":
    main()
