from __future__ import annotations

from validation_utils import assert_all_site_data_json_valid, ensure_keys, fail, load_json, pass_message


REQUIRED_SOURCE_KEYS = ["type", "allowed", "use_case", "citation_required", "public_claim_gate"]
GOVERNED_CLAIM_TERMS = ["legal", "regulatory", "market", "technical", "comparative", "company"]


def main() -> None:
    assert_all_site_data_json_valid()
    errors: list[str] = []
    registry = load_json("site/data/source_registry.json")

    if registry.get("external_source_claims_active") is not False:
        errors.append("external_source_claims_active must be false")
    rule = str(registry.get("rule", "")).lower()
    for term in GOVERNED_CLAIM_TERMS:
        if term not in rule:
            errors.append(f"source policy rule must govern {term} claims")

    source_types = registry.get("source_types")
    if not isinstance(source_types, list) or not source_types:
        errors.append("source_registry.json must contain a non-empty source_types array")
    else:
        for source_type in source_types:
            context = f"source type {source_type.get('type', '<missing type>')}"
            errors.extend(ensure_keys(source_type, REQUIRED_SOURCE_KEYS, context))
            if source_type.get("citation_required") is not True:
                errors.append(f"{context} must require citations")
            if source_type.get("public_claim_gate") != "required":
                errors.append(f"{context} public_claim_gate must be required")

    if registry.get("sources") not in ([], None):
        errors.append("no active external source claims should be present")

    if errors:
        fail("; ".join(errors))

    pass_message("source governance registry remains reserved and claim-gated")


if __name__ == "__main__":
    main()
