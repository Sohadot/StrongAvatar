from __future__ import annotations

from validation_utils import assert_all_site_data_json_valid, fail, load_json, load_pages, pass_message


def main() -> None:
    assert_all_site_data_json_valid()
    errors: list[str] = []

    site = load_json("site/data/site.json")
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
