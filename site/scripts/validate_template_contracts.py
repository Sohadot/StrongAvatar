from __future__ import annotations

from pathlib import Path

from validation_utils import fail, load_json, pass_message, repo_root


REQUIRED_PLANNED_FILES = [
    "base.html",
    "homepage.html",
    "reference-page.html",
    "protocol-page.html",
    "comparison-page.html",
    "glossary-term.html",
    "brief-page.html",
    "strategic-asset-page.html",
]

REQUIRED_TEMPLATE_KEYS = [
    "template_id",
    "planned_file",
    "contract",
    "status",
    "html_exists",
    "public_enabled",
    "output_allowed",
    "allowed_page_types",
    "required_data_inputs",
    "required_seo_elements",
    "required_trust_elements",
    "prohibited_behaviors",
    "notes",
]

REQUIRED_HEADINGS = [
    "# Template Contract",
    "## Template Name",
    "## Template File Planned",
    "## Construction State",
    "## Purpose",
    "## Allowed Page Types",
    "## Required Data Inputs",
    "## Required SEO Elements",
    "## Required Trust Elements",
    "## Required Internal Link Elements",
    "## Required Buyer Logic Elements",
    "## Monetization Boundary",
    "## Prohibited Template Behavior",
    "## Accessibility and Performance Requirements",
    "## Indexing Conditions",
    "## Notes",
]

PLACEHOLDER_TERMS = ["lorem ipsum", "todo", "tbd", "placeholder", "coming soon"]
PUBLIC_READY_PHRASES = [
    "html template is live",
    "template is live",
    "ready for public rendering",
    "public template exists",
    "now generates output",
]
REQUIRED_STATE_PHRASES = [
    "contract-only",
    "no html template exists yet",
    "non-public",
    "non-generative",
]
PROHIBITED_BEHAVIORS = [
    "generic blog layout",
    "avatar generator landing page layout",
    "affiliate directory layout",
    "fandom page layout",
    "thin seo landing page layout",
    "hype-heavy startup landing page layout",
    "unsourced claim presentation",
]


def site_templates_files(root: Path) -> list[Path]:
    templates_dir = root / "site" / "templates"
    if not templates_dir.exists():
        return []
    return sorted(path for path in templates_dir.rglob("*") if path.is_file())


def main() -> None:
    root = repo_root()
    contract_root = (root / "site" / "template-contracts").resolve()
    template_registry = load_json("site/data/template_registry.json")
    errors: list[str] = []

    templates = template_registry.get("templates")
    if not isinstance(templates, list):
        fail("template_registry.json must contain a templates array")

    planned_files = {template.get("planned_file") for template in templates}
    for planned_file in REQUIRED_PLANNED_FILES:
        if planned_file not in planned_files:
            errors.append(f"template_registry.json missing planned template: {planned_file}")

    template_files = site_templates_files(root)
    non_gitkeep_template_files = [path for path in template_files if path.name != ".gitkeep"]
    if non_gitkeep_template_files:
        errors.append("site/templates/ must remain .gitkeep-only")
    html_templates = [path for path in template_files if path.suffix.lower() == ".html"]
    if html_templates:
        errors.append("no .html files may exist under site/templates/")

    for template in templates:
        planned_file = template.get("planned_file", "<missing planned_file>")
        context = f"template {planned_file}"
        for key in REQUIRED_TEMPLATE_KEYS:
            if key not in template:
                errors.append(f"{context} missing required key: {key}")

        if template.get("status") != "contract_created":
            errors.append(f"{context} status must be contract_created")
        if template.get("html_exists") is not False:
            errors.append(f"{context} html_exists must be false")
        if template.get("public_enabled") is not False:
            errors.append(f"{context} public_enabled must be false")
        if template.get("output_allowed") is not False:
            errors.append(f"{context} output_allowed must be false")

        contract_value = template.get("contract")
        if not contract_value:
            errors.append(f"{context} missing contract path")
            continue

        contract_path = (root / str(contract_value)).resolve()
        try:
            contract_path.relative_to(contract_root)
        except ValueError:
            errors.append(f"{context} contract path is outside site/template-contracts/: {contract_value}")
            continue
        if not contract_path.exists():
            errors.append(f"{context} contract file does not exist: {contract_value}")
            continue

        content = contract_path.read_text(encoding="utf-8")
        lower_content = content.lower()
        contract_context = f"contract {contract_path.relative_to(root).as_posix()}"

        for term in PLACEHOLDER_TERMS:
            if term in lower_content:
                errors.append(f"{contract_context} contains placeholder language: {term}")
        for phrase in PUBLIC_READY_PHRASES:
            if phrase in lower_content:
                errors.append(f"{contract_context} suggests HTML template is public-ready: {phrase}")

        for heading in REQUIRED_HEADINGS:
            if heading not in content:
                errors.append(f"{contract_context} missing heading: {heading}")
        for phrase in REQUIRED_STATE_PHRASES:
            if phrase not in lower_content:
                errors.append(f"{contract_context} missing construction-state phrase: {phrase}")
        for behavior in PROHIBITED_BEHAVIORS:
            if behavior not in lower_content:
                errors.append(f"{contract_context} must reject: {behavior}")
        if "templates do not control indexability" not in lower_content:
            errors.append(f"{contract_context} must state templates do not control indexability")
        if not ("monetization registry" in lower_content or "policy approval" in lower_content):
            errors.append(f"{contract_context} must require monetization registry or policy approval")

    if errors:
        fail("; ".join(errors))

    pass_message("template contracts and registry are reserved, non-public, and non-generative")


if __name__ == "__main__":
    main()
