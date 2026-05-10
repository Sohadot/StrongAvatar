from __future__ import annotations

from validation_utils import fail, load_json, load_pages, pass_message


def main() -> None:
    site = load_json("site/data/site.json")

    if site.get("public_publishing_enabled") is True:
        fail("public_publishing_enabled is true, but sitemap generation rules are not authorized")
    if site.get("public_publishing_enabled") is not False:
        fail("public_publishing_enabled must be false during sovereign foundation mode")

    errors: list[str] = []
    for page in load_pages():
        slug = page.get("slug", "<missing slug>")
        if page.get("indexable") is True:
            errors.append(f"{slug} is indexable before publishing is authorized")
        if page.get("status") == "published":
            errors.append(f"{slug} is published before publishing is authorized")
        if page.get("publication_allowed") is True:
            errors.append(f"{slug} has publication_allowed true before publishing is authorized")

    if errors:
        fail("; ".join(errors))

    pass_message("sitemap generation intentionally disabled until approved indexable pages exist; no sitemap.xml written")


if __name__ == "__main__":
    main()
