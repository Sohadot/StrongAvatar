from __future__ import annotations

from validation_utils import fail, load_json, pass_message


def main() -> None:
    site = load_json("site/data/site.json")

    if site.get("public_publishing_enabled") is True:
        fail("public_publishing_enabled is true, but robots generation rules are not authorized")
    if site.get("public_publishing_enabled") is not False:
        fail("public_publishing_enabled must be false during sovereign foundation mode")

    pass_message("robots generation intentionally disabled during sovereign foundation mode; no robots.txt written")


if __name__ == "__main__":
    main()
