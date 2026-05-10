from __future__ import annotations

from validation_utils import assert_all_site_data_json_valid, ensure_keys, fail, load_json, load_pages, pass_message


REQUIRED_SEGMENT_KEYS = [
    "segment",
    "status",
    "strategic_need",
    "asset_relevance",
    "acquisition_logic",
    "public_enabled",
]


def main() -> None:
    assert_all_site_data_json_valid()
    errors: list[str] = []
    registry = load_json("site/data/buyer_segments.json")

    segments = registry.get("segments")
    if not isinstance(segments, list) or not segments:
        errors.append("buyer_segments.json must contain a non-empty segments array")
    else:
        for segment in segments:
            context = f"buyer segment {segment.get('segment', '<missing segment>')}"
            errors.extend(ensure_keys(segment, REQUIRED_SEGMENT_KEYS, context))
            if segment.get("public_enabled") is not False:
                errors.append(f"{context} public_enabled must be false")

    for page in load_pages():
        slug = page.get("slug", "<missing slug>")
        if "buyer_logic_role" not in page:
            errors.append(f"page {slug} missing buyer_logic_role")
        elif not str(page.get("buyer_logic_role", "")).strip():
            errors.append(f"page {slug} has empty buyer_logic_role")

    if errors:
        fail("; ".join(errors))

    pass_message("buyer logic registry remains complete and non-public")


if __name__ == "__main__":
    main()
