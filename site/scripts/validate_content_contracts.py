from __future__ import annotations

import re
from pathlib import Path

from validation_utils import fail, load_pages, pass_message, repo_root


REQUIRED_HEADINGS = [
    "# Page Contract",
    "## Route",
    "## Planned Title",
    "## Publication State",
    "## Strategic Purpose",
    "## Category Role",
    "## SEO Role",
    "## Buyer Logic Role",
    "## Monetization Role",
    "## Required Internal Links",
    "## Source Requirements",
    "## Content Boundaries",
    "## Reference-Grade Requirements",
    "## Indexing Conditions",
    "## Notes",
]

PLACEHOLDER_TERMS = ["lorem ipsum", "todo", "tbd", "placeholder", "coming soon"]
LIVE_PUBLICATION_PHRASES = [
    "is now live",
    "is live",
    "published at",
    "available at https://strongavatar.com",
    "public page is live",
    "now published",
]
BOUNDARY_CONCEPTS = {
    "generic blog post": [
        "generic blog post",
        "generic blog content",
        "generic ai blog post",
        "generic ai explainer",
        "generic identity article",
        "generic ai dictionary",
        "generic startup pitch",
        "vague principles page",
    ],
    "avatar generator landing page": [
        "avatar generator landing page",
        "avatar generator page",
        "avatar maker page",
        "avatar maker",
        "automated score tool",
    ],
    "affiliate page": [
        "affiliate page",
        "affiliate content",
        "affiliate roundup",
        "affiliate funnel",
    ],
    "fandom page": [
        "fandom page",
        "fandom content",
        "celebrity likeness article",
    ],
    "thin SEO page": [
        "thin seo page",
        "thin seo glossary substitute",
        "thin tool page",
        "thin seo page collection",
    ],
}


def section_text(content: str, heading: str) -> str:
    pattern = rf"^{re.escape(heading)}\s*$([\s\S]*?)(?=^## |\Z)"
    match = re.search(pattern, content, flags=re.MULTILINE)
    return match.group(1).strip() if match else ""


def route_like_strings(text: str) -> list[str]:
    return re.findall(r"`(/(?:[a-z0-9-]+/)*)`", text)


def main() -> None:
    root = repo_root()
    contract_root = (root / "site" / "content-contracts").resolve()
    registered_routes = {page.get("slug") for page in load_pages()}
    errors: list[str] = []

    for page in load_pages():
        slug = page.get("slug", "<missing slug>")
        context = f"page {slug}"
        contract_value = page.get("content_contract")

        if not contract_value:
            errors.append(f"{context} missing content_contract")
            continue
        if page.get("content_contract_status") != "created":
            errors.append(f"{context} content_contract_status must be created")
        if page.get("publication_allowed") is not False:
            errors.append(f"{context} publication_allowed must remain false")
        if page.get("indexable") is not False:
            errors.append(f"{context} indexable must remain false")
        if page.get("status") not in {"reserved", "planned"}:
            errors.append(f"{context} status must remain reserved or planned")

        contract_path = (root / str(contract_value)).resolve()
        try:
            contract_path.relative_to(contract_root)
        except ValueError:
            errors.append(f"{context} content_contract is outside site/content-contracts: {contract_value}")
            continue
        if not contract_path.exists():
            errors.append(f"{context} content_contract does not exist: {contract_value}")
            continue

        content = contract_path.read_text(encoding="utf-8")
        lower_content = content.lower()
        contract_context = f"contract {contract_path.relative_to(root).as_posix()}"

        for heading in REQUIRED_HEADINGS:
            if heading not in content:
                errors.append(f"{contract_context} missing heading: {heading}")

        for term in PLACEHOLDER_TERMS:
            if term in lower_content:
                errors.append(f"{contract_context} contains placeholder language: {term}")
        for phrase in LIVE_PUBLICATION_PHRASES:
            if phrase in lower_content:
                errors.append(f"{contract_context} suggests public publication is live: {phrase}")

        top_text = "\n".join(content.splitlines()[:16])
        if str(slug) not in top_text:
            errors.append(f"{contract_context} does not include registered route near the top: {slug}")
        state_text = section_text(content, "## Publication State").lower()
        for required_state in ["reserved", "non-public", "non-indexable"]:
            if required_state not in state_text:
                errors.append(f"{contract_context} Publication State missing: {required_state}")

        required_links_text = section_text(content, "## Required Internal Links")
        for route in route_like_strings(required_links_text):
            if route not in registered_routes:
                errors.append(f"{contract_context} Required Internal Links references unregistered route: {route}")

        indexing_text = section_text(content, "## Indexing Conditions").lower()
        if "quality gate" not in indexing_text:
            errors.append(f"{contract_context} Indexing Conditions must mention quality gate")
        if "explicit publishing decision" not in indexing_text:
            errors.append(f"{contract_context} Indexing Conditions must mention explicit publishing decision")

        boundaries_text = section_text(content, "## Content Boundaries").lower()
        for concept, phrases in BOUNDARY_CONCEPTS.items():
            if not any(phrase in boundaries_text for phrase in phrases):
                errors.append(f"{contract_context} Content Boundaries must reject {concept}")

    if errors:
        fail("; ".join(errors))

    pass_message("content contracts are complete, reserved, non-public, and quality-gated")


if __name__ == "__main__":
    main()
