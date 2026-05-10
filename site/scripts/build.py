from __future__ import annotations

from validation_utils import fail, list_non_gitkeep_files, load_json, pass_message


def main() -> None:
    site = load_json("site/data/site.json")

    if site.get("public_publishing_enabled") is True:
        fail("public_publishing_enabled is true, but no real publishing engine has been authorized")
    if site.get("public_publishing_enabled") is not False:
        fail("public_publishing_enabled must be false during sovereign foundation mode")
    if site.get("asset_stage") != "sovereign_foundation":
        fail("asset_stage must remain sovereign_foundation")
    if site.get("indexing_status") != "disabled_until_quality_gate_exists":
        fail("indexing_status must remain disabled_until_quality_gate_exists")

    output_files = list_non_gitkeep_files("output")
    if output_files:
        fail("output/ must contain only .gitkeep or remain empty during sovereign foundation mode")

    pass_message("build intentionally disabled during sovereign foundation mode; no files generated")


if __name__ == "__main__":
    main()
