from __future__ import annotations

from validation_utils import assert_all_site_data_json_valid, fail, list_non_gitkeep_files, load_pages, pass_message


DISALLOWED_QUALITY_STATUSES = {"approved", "published"}


def main() -> None:
    assert_all_site_data_json_valid()
    errors: list[str] = []

    content_files = list_non_gitkeep_files("site/content")
    if content_files:
        errors.append("content files exist before governance is ready: " + ", ".join(str(path) for path in content_files))

    for page in load_pages():
        slug = page.get("slug", "<missing slug>")
        if page.get("status") == "published":
            errors.append(f"page {slug} is published")
        if page.get("indexable") is True:
            errors.append(f"page {slug} is indexable")
        if page.get("status") in {"reserved", "planned"} and page.get("quality_status") in DISALLOWED_QUALITY_STATUSES:
            errors.append(f"page {slug} has premature quality_status: {page.get('quality_status')}")

    if errors:
        fail("; ".join(errors))

    pass_message("thin-page prevention confirms no public content or indexable pages")


if __name__ == "__main__":
    main()
