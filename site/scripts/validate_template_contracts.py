from __future__ import annotations

import re
from pathlib import Path

from validation_utils import fail, load_json, pass_message, repo_root


AUTHORIZED_HTML_TEMPLATE = "base.html"
AUTHORIZED_IMPLEMENTED_FILE = "site/templates/base.html"
AUTHORIZED_IMPLEMENTATION_SCOPE = "base_shell_only"
AUTHORIZED_CSS_DEPENDENCY = "site/static/css/main.css"
AUTHORIZED_CSS_PUBLIC_PATH = "/static/css/main.css"

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

BASE_REQUIRED_PLACEHOLDERS = [
    "{{ lang }}",
    "{{ page_title }}",
    "{{ meta_description }}",
    "{{ canonical_url }}",
    "{{ robots_directive }}",
    "{{ og_title }}",
    "{{ og_description }}",
    "{{ og_url }}",
    "{{ og_type }}",
    "{{ twitter_title }}",
    "{{ twitter_description }}",
    "{{ structured_data }}",
    "{{ header }}",
    "{{ main_content }}",
    "{{ footer }}",
]

BASE_PROHIBITED_TERMS = [
    "create your ai avatar",
    "generate your avatar",
    "start now",
    "buy now",
    "affiliate",
    "sponsored placement",
    "ad scripts",
    "google analytics",
    "google tag manager",
    "tracking pixel",
    "tracking pixels",
    "external cdn",
    "cdn",
    "javascript",
    "webxr",
    "webgl",
    "three.js",
    "avatar maker",
    "gaming hud",
    "cyberpunk",
    "neon chaos",
    "fandom",
    "cheap luxury",
    "lorem ipsum",
    "todo",
    "tbd",
    "coming soon",
    "placeholder article content",
]

BASE_PUBLIC_CONTENT_PATTERNS = [
    r"<article\b",
    r"\bhero\b",
    r"\bcta\b",
    r"\bmarketing\b",
]


def site_templates_files(root: Path) -> list[Path]:
    templates_dir = root / "site" / "templates"
    if not templates_dir.exists():
        return []
    return sorted(path for path in templates_dir.rglob("*") if path.is_file())


def validate_base_html(root: Path, base_path: Path, errors: list[str]) -> None:
    content = base_path.read_text(encoding="utf-8")
    lower_content = content.lower()
    relative_path = base_path.relative_to(root).as_posix()

    if "<!doctype html>" not in lower_content:
        errors.append(f"{relative_path} missing document type")
    if '<html lang="{{ lang }}">' not in content:
        errors.append(f"{relative_path} missing html lang placeholder")
    if "<head>" not in lower_content:
        errors.append(f"{relative_path} missing head element")
    if '<meta charset="UTF-8">' not in content:
        errors.append(f"{relative_path} missing UTF-8 charset")
    if 'name="viewport"' not in lower_content:
        errors.append(f"{relative_path} missing viewport meta")
    if f'href="{AUTHORIZED_CSS_PUBLIC_PATH}"' not in content:
        errors.append(f"{relative_path} missing CSS link to {AUTHORIZED_CSS_PUBLIC_PATH}")
    if 'href="#main-content"' not in content or "skip" not in lower_content:
        errors.append(f"{relative_path} missing accessibility skip link")
    if "<main" not in lower_content:
        errors.append(f"{relative_path} missing main landmark")
    if "<footer" not in lower_content or "{{ footer }}" not in content:
        errors.append(f"{relative_path} missing footer placeholder region")
    if "<script" in lower_content or "</script" in lower_content:
        errors.append(f"{relative_path} must not contain script tags")
    if re.search(r"\b(?:src|href)=['\"]https?://", content, flags=re.IGNORECASE):
        errors.append(f"{relative_path} must not reference external asset URLs")
    if re.search(r"\b(?:src|href)=['\"]//", content, flags=re.IGNORECASE):
        errors.append(f"{relative_path} must not reference protocol-relative external URLs")
    if re.search(r"\b(?:src|href)=['\"][^'\"]+\.js(?:[?#][^'\"]*)?['\"]", content, flags=re.IGNORECASE):
        errors.append(f"{relative_path} must not reference JavaScript files")
    if "@import" in lower_content or "font" in lower_content and ("googleapis" in lower_content or "typekit" in lower_content):
        errors.append(f"{relative_path} must not contain font imports")

    for placeholder in BASE_REQUIRED_PLACEHOLDERS:
        if placeholder not in content:
            errors.append(f"{relative_path} missing required placeholder: {placeholder}")
    for term in BASE_PROHIBITED_TERMS:
        if term in lower_content:
            errors.append(f"{relative_path} contains prohibited language or reference: {term}")
    for pattern in BASE_PUBLIC_CONTENT_PATTERNS:
        if re.search(pattern, lower_content):
            errors.append(f"{relative_path} contains public-page or article-oriented structure: {pattern}")


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
    html_templates = [path for path in template_files if path.suffix.lower() == ".html"]
    unauthorized_template_files = [
        path for path in non_gitkeep_template_files if path.name != AUTHORIZED_HTML_TEMPLATE
    ]
    if unauthorized_template_files:
        unauthorized = ", ".join(path.relative_to(root).as_posix() for path in unauthorized_template_files)
        errors.append(f"site/templates/ contains unauthorized template files: {unauthorized}")
    unauthorized_html_templates = [
        path for path in html_templates if path.name != AUTHORIZED_HTML_TEMPLATE
    ]
    if unauthorized_html_templates:
        unauthorized = ", ".join(path.relative_to(root).as_posix() for path in unauthorized_html_templates)
        errors.append(f"site/templates/ contains unauthorized HTML templates: {unauthorized}")

    base_path = root / AUTHORIZED_IMPLEMENTED_FILE
    templates_by_file = {template.get("planned_file"): template for template in templates}
    base_template = templates_by_file.get(AUTHORIZED_HTML_TEMPLATE)
    if base_template and base_template.get("html_exists") is True and not base_path.exists():
        errors.append(f"{AUTHORIZED_IMPLEMENTED_FILE} is missing while registry html_exists is true")
    if base_path.exists():
        if not base_template:
            errors.append(f"{AUTHORIZED_IMPLEMENTED_FILE} exists but is missing from template_registry.json")
        else:
            if base_template.get("html_exists") is not True:
                errors.append(f"{AUTHORIZED_IMPLEMENTED_FILE} exists but registry html_exists is not true")
            if base_template.get("implementation_authorized") is not True:
                errors.append(f"{AUTHORIZED_IMPLEMENTED_FILE} exists but registry does not explicitly authorize it")
            if base_template.get("implemented_file") != AUTHORIZED_IMPLEMENTED_FILE:
                errors.append(f"{AUTHORIZED_IMPLEMENTED_FILE} exists but registry implemented_file is incorrect")
            if base_template.get("implementation_scope") != AUTHORIZED_IMPLEMENTATION_SCOPE:
                errors.append(f"{AUTHORIZED_IMPLEMENTED_FILE} exists but implementation_scope is not {AUTHORIZED_IMPLEMENTATION_SCOPE}")
            if base_template.get("public_enabled") is not False:
                errors.append(f"{AUTHORIZED_IMPLEMENTED_FILE} exists but public_enabled is not false")
            if base_template.get("output_allowed") is not False:
                errors.append(f"{AUTHORIZED_IMPLEMENTED_FILE} exists but output_allowed is not false")
            if base_template.get("css_dependency") != AUTHORIZED_CSS_DEPENDENCY:
                errors.append(f"{AUTHORIZED_IMPLEMENTED_FILE} exists but css_dependency is not {AUTHORIZED_CSS_DEPENDENCY}")
        validate_base_html(root, base_path, errors)

    for template in templates:
        planned_file = template.get("planned_file", "<missing planned_file>")
        context = f"template {planned_file}"
        for key in REQUIRED_TEMPLATE_KEYS:
            if key not in template:
                errors.append(f"{context} missing required key: {key}")

        is_base_template = planned_file == AUTHORIZED_HTML_TEMPLATE
        if not is_base_template:
            if template.get("status") != "contract_created":
                errors.append(f"{context} status must be contract_created")
            if template.get("html_exists") is not False:
                errors.append(f"{context} html_exists must be false")
            if template.get("implementation_authorized") is True:
                errors.append(f"{context} implementation_authorized must not be true")
            if "implemented_file" in template:
                errors.append(f"{context} must not define implemented_file")
        elif template.get("status") != "contract_created":
            errors.append(f"{context} status must remain contract_created")
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

    pass_message("template contracts and authorized base shell are non-public and non-generative")


if __name__ == "__main__":
    main()
