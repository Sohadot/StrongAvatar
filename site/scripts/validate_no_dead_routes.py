from __future__ import annotations

from validation_utils import assert_all_site_data_json_valid, fail, load_json, load_pages, pass_message


def valid_slug(slug: object) -> bool:
    if not isinstance(slug, str) or not slug.startswith("/"):
        return False
    return slug == "/" or slug.endswith("/")


def main() -> None:
    assert_all_site_data_json_valid()
    errors: list[str] = []
    pages = load_pages()
    slugs = [page.get("slug") for page in pages]
    registered_slugs = set(slugs)

    for slug in slugs:
        if not valid_slug(slug):
            errors.append(f"invalid page slug format: {slug}")
    if len(slugs) != len(registered_slugs):
        errors.append("page slugs must be unique")

    redirects = load_json("site/data/redirects.json")
    if "redirects" not in redirects or not isinstance(redirects.get("redirects"), list):
        errors.append("redirects.json must contain a redirects array")
    if redirects.get("redirects_active") is not False:
        errors.append("redirects_active must be false")
    for redirect in redirects.get("redirects", []):
        if redirect.get("active") is not False:
            errors.append(f"active redirect is not allowed: {redirect}")

    navigation = load_json("site/data/navigation.json")
    for item in navigation.get("items", []):
        target = item.get("target")
        label = item.get("label", "<missing label>")
        if target not in registered_slugs:
            errors.append(f"navigation item {label} points to unregistered route: {target}")
        if item.get("enabled") is not False:
            errors.append(f"navigation item {label} must remain disabled")
        if item.get("publication_allowed") is not False:
            errors.append(f"navigation item {label} publication_allowed must remain false")

    if errors:
        fail("; ".join(errors))

    pass_message("dead-route prevention confirms reserved routes and redirects are controlled")


if __name__ == "__main__":
    main()
