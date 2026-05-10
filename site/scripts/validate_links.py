from __future__ import annotations

from validation_utils import assert_all_site_data_json_valid, fail, load_json, load_pages, pass_message


def main() -> None:
    assert_all_site_data_json_valid()
    errors: list[str] = []
    pages = load_pages()
    registered_slugs = {page.get("slug") for page in pages}

    for page in pages:
        slug = page.get("slug", "<missing slug>")
        required_links = page.get("required_links")
        if not isinstance(required_links, list):
            errors.append(f"page {slug} required_links must be an array")
            continue
        if not required_links and slug != "/":
            errors.append(f"page {slug} has empty required_links")
        for link in required_links:
            if link not in registered_slugs:
                errors.append(f"page {slug} links to unregistered route: {link}")

    navigation = load_json("site/data/navigation.json")
    if navigation.get("public_navigation_enabled") is not False:
        errors.append("navigation public_navigation_enabled must be false")
    for item in navigation.get("items", []):
        label = item.get("label", "<missing label>")
        if item.get("enabled") is True:
            errors.append(f"navigation item {label} is enabled")
        if item.get("publication_allowed") is True:
            errors.append(f"navigation item {label} has publication_allowed true")

    if errors:
        fail("; ".join(errors))

    pass_message("internal links and reserved navigation remain controlled")


if __name__ == "__main__":
    main()
