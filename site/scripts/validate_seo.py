from __future__ import annotations

import json
from pathlib import Path

from validation_utils import assert_all_site_data_json_valid, fail, load_json, load_pages, pass_message, repo_root


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

    site = load_json("site/data/site.json")

    if gen_auth:
        if site.get("public_publishing_enabled") is not True:
            errors.append("site public_publishing_enabled must be true when generation is authorized")
        allowed_indexing = {"foundation_launch_set_only", "disabled_until_quality_gate_exists"}
        if site.get("indexing_status") not in allowed_indexing:
            errors.append(f"site indexing_status must be one of: {allowed_indexing}")
    else:
        if site.get("public_publishing_enabled") is not False:
            errors.append("site public_publishing_enabled must be false")
        if site.get("indexing_status") != "disabled_until_quality_gate_exists":
            errors.append("site indexing_status must be disabled_until_quality_gate_exists")

    seen_slugs: set[str] = set()
    for page in load_pages():
        slug = page.get("slug")
        if slug in seen_slugs:
            errors.append(f"duplicate page slug: {slug}")
        seen_slugs.add(slug)

        is_launch_set = slug in ls_routes

        if gen_auth and is_launch_set:
            # Launch-set pages are allowed to be indexable when authorized
            pass
        else:
            if page.get("indexable") is not False:
                errors.append(f"page {slug} must be indexable false")

        if not str(page.get("title", "")).strip():
            errors.append(f"page {slug} has empty title")
        if not str(page.get("seo_cluster", "")).strip():
            errors.append(f"page {slug} has empty seo_cluster")
        if not str(page.get("strategic_purpose", "")).strip():
            errors.append(f"page {slug} has empty strategic_purpose")

    if errors:
        fail("; ".join(errors))

    pass_message("SEO and indexing registries remain disabled and controlled")


if __name__ == "__main__":
    main()
