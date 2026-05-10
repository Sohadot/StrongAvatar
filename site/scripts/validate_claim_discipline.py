from __future__ import annotations

from validation_utils import ensure_keys, fail, load_json, pass_message


REQUIRED_CLAIM_TYPES = [
    "conceptual_analysis",
    "definition_claim",
    "legal_claim",
    "regulatory_claim",
    "market_claim",
    "technical_claim",
    "platform_capability_claim",
    "company_claim",
    "comparative_claim",
    "risk_claim",
    "monetization_claim",
    "acquisition_claim",
]

REQUIRED_CLAIM_KEYS = [
    "claim_type",
    "status",
    "public_enabled",
    "description",
    "source_required",
    "allowed_source_types",
    "disclaimer_required",
    "prohibited_without_source",
    "notes",
]

REQUIRED_SOURCE_TYPES = [
    "regulatory",
    "legal_analysis",
    "market_research",
    "platform_documentation",
    "technical_documentation",
    "academic",
    "company_primary_source",
]

SOURCE_REQUIRED_TYPES = [
    "legal_claim",
    "regulatory_claim",
    "market_claim",
    "technical_claim",
    "platform_capability_claim",
    "company_claim",
    "comparative_claim",
]


def main() -> None:
    errors: list[str] = []
    claim_registry = load_json("site/data/claim_types.json")
    source_registry = load_json("site/data/source_registry.json")

    source_types = source_registry.get("source_types")
    if not isinstance(source_types, list):
        fail("source_registry.json must contain source_types array")

    source_type_map = {source.get("type"): source for source in source_types}
    for required_source in REQUIRED_SOURCE_TYPES:
        if required_source not in source_type_map:
            errors.append(f"source_registry.json missing source type: {required_source}")
            continue
        source = source_type_map[required_source]
        if source.get("citation_required") is not True:
            errors.append(f"source type {required_source} must require citations")
        if source.get("public_claim_gate") != "required":
            errors.append(f"source type {required_source} must have public_claim_gate required")

    claim_types = claim_registry.get("claim_types")
    if not isinstance(claim_types, list):
        fail("claim_types.json must contain claim_types array")

    claim_type_map = {claim.get("claim_type"): claim for claim in claim_types}
    for required_claim in REQUIRED_CLAIM_TYPES:
        if required_claim not in claim_type_map:
            errors.append(f"claim_types.json missing claim type: {required_claim}")

    for claim in claim_types:
        claim_type = claim.get("claim_type", "<missing claim_type>")
        context = f"claim type {claim_type}"
        errors.extend(ensure_keys(claim, REQUIRED_CLAIM_KEYS, context))

        if claim.get("status") != "governed":
            errors.append(f"{context} status must be governed")
        if claim.get("public_enabled") is not False:
            errors.append(f"{context} public_enabled must be false")

        allowed_sources = claim.get("allowed_source_types")
        if not isinstance(allowed_sources, list):
            errors.append(f"{context} allowed_source_types must be an array")
            allowed_sources = []
        for source_type in allowed_sources:
            if source_type not in source_type_map:
                errors.append(f"{context} references unknown source type: {source_type}")

    for claim_type in ["legal_claim", "regulatory_claim"]:
        claim = claim_type_map.get(claim_type, {})
        if claim.get("source_required") is not True:
            errors.append(f"{claim_type} must require source support")
        if claim.get("disclaimer_required") is not True:
            errors.append(f"{claim_type} must require disclaimer discipline")

    for claim_type in SOURCE_REQUIRED_TYPES:
        claim = claim_type_map.get(claim_type, {})
        if claim.get("source_required") is not True:
            errors.append(f"{claim_type} must require source support")

    conceptual = claim_type_map.get("conceptual_analysis", {})
    conceptual_notes = " ".join(
        str(conceptual.get(key, "")) for key in ["description", "notes", "prohibited_without_source"]
    ).lower()
    if conceptual.get("source_required") is not False:
        errors.append("conceptual_analysis may not require sources by default")
    if "analysis" not in conceptual_notes or "factual proof" not in conceptual_notes:
        errors.append("conceptual_analysis must be analysis-framed and not factual proof")

    acquisition = claim_type_map.get("acquisition_claim", {})
    acquisition_text = " ".join(
        str(acquisition.get(key, "")) for key in ["description", "notes", "prohibited_without_source"]
    ).lower()
    if "valuation promises" not in acquisition_text:
        errors.append("acquisition_claim must prohibit valuation promises without source")
    if "strategic posture" not in acquisition_text:
        errors.append("acquisition_claim must be framed as strategic posture unless sourced")

    if any(claim.get("public_enabled") is True for claim in claim_types):
        errors.append("no claim type may be public-enabled during the current foundation stage")

    if errors:
        fail("; ".join(errors))

    pass_message("claim discipline registry is governed, source-aware, and non-public")


if __name__ == "__main__":
    main()
