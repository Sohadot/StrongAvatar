from __future__ import annotations

from pathlib import Path
from typing import Any

from validation_utils import fail, load_json, pass_message, repo_root


REQUIRED_TOP_LEVEL_FIELDS = [
    "status", "css_exists", "public_enabled", "output_allowed",
    "visual_doctrine", "color_tokens", "typography_tokens", "spacing_tokens",
    "layout_tokens", "component_token_expectations", "accessibility_requirements",
    "performance_requirements", "prohibited_visual_directions",
    "css_activation_conditions", "notes",
    "visual_sovereignty", "proprietary_visual_standard", "violet_gold_identity_field",
    "warm_spatial_institutional_ux", "prohibited_generic_conventions",
    "spatial_ux_doctrine", "depth_principles", "motion_principles",
    "spatial_component_expectations", "prohibited_immersive_shortcuts",
    "future_activation_conditions",
]
REQUIRED_COLOR_TOKENS = [
    "background_primary", "background_secondary", "surface_primary", "surface_elevated",
    "text_primary", "text_secondary", "text_muted", "accent_primary", "accent_secondary",
    "border_subtle", "border_active", "warning", "trust", "source_note", "disabled",
]
REQUIRED_TYPOGRAPHY_TOKENS = [
    "display", "headline", "section_title", "body", "small", "metadata", "code_or_registry",
]
REQUIRED_SPACING_TOKENS = ["xs", "sm", "md", "lg", "xl", "section", "page"]
REQUIRED_PROHIBITED_DIRECTIONS = [
    "cartoon avatar maker", "gaming toy interface", "generic SaaS gradient template",
    "affiliate directory look", "hype-heavy AI startup style", "neon chaos",
    "fandom aesthetic", "cheap tool website", "childish mascot identity",
    "black-blue dominance", "cold cyberpunk darkness", "childish purple/yellow gaming style",
    "cheap luxury gold", "conventional SaaS landing page style",
    "consumer avatar-maker visual language", "borrowed category conventions",
    "decorative novelty without strategic authority", "visual trend-chasing",
]
REQUIRED_GENERIC_CONVENTIONS = [
    "generic AI website", "consumer avatar maker", "gaming interface",
    "cyberpunk dashboard", "conventional SaaS landing page",
    "luxury-tech cliché", "borrowed market convention",
]
REQUIRED_VIOLET_GOLD_TERMS = [
    "warm violet", "muted purple", "plum", "pale gold", "amber", "cream-gold",
]
REQUIRED_CSS_ACTIVATION_TERMS = [
    "design token registry", "template contracts", "explicitly authorized",
    "quality gate", "decision log",
]
REQUIRED_DOCUMENT_HEADINGS = [
    "# Design Tokens Contract", "## Purpose", "## Construction State",
    "## Visual Doctrine", "## Color System", "## Typography System",
    "## Spacing System", "## Layout System", "## Component Token Expectations",
    "## Accessibility Requirements", "## Performance Requirements",
    "## Prohibited Visual Directions", "## CSS Activation Conditions", "## Notes",
]
REQUIRED_DOCUMENT_STATE = [
    "token-contract-only", "no css exists yet", "non-public", "non-generative",
]
PROHIBITED_REGISTRY_REFERENCES = [
    ".woff", ".woff2", ".ttf", ".otf", "fonts.googleapis.com", "cdn.",
    "http://", "https://", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp",
]
CSS_DECLARATION_PATTERNS = [
    "color:", "background:", "font-family:", "margin:", "padding:", "display:", "{", "}",
]


def flatten_strings(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        result: list[str] = []
        for item in value:
            result.extend(flatten_strings(item))
        return result
    if isinstance(value, dict):
        result = []
        for key, item in value.items():
            result.append(str(key))
            result.extend(flatten_strings(item))
        return result
    return []


def gitkeep_only(path: Path) -> bool:
    if not path.exists():
        return False
    files = [file for file in path.rglob("*") if file.is_file()]
    return all(file.name == ".gitkeep" for file in files)


def main() -> None:
    root = repo_root()
    errors: list[str] = []
    design_doc = root / "architecture" / "DESIGN_TOKENS.md"
    registry = load_json("site/data/design_tokens.json")

    if not design_doc.exists():
        errors.append("architecture/DESIGN_TOKENS.md must exist")
    for field in REQUIRED_TOP_LEVEL_FIELDS:
        if field not in registry:
            errors.append(f"design_tokens.json missing required field: {field}")
    if registry.get("status") != "contract_created":
        errors.append("design_tokens.json status must be contract_created")
    if registry.get("css_exists") is not False:
        errors.append("design_tokens.json css_exists must be false")
    if registry.get("public_enabled") is not False:
        errors.append("design_tokens.json public_enabled must be false")
    if registry.get("output_allowed") is not False:
        errors.append("design_tokens.json output_allowed must be false")

    css_dir = root / "site" / "static" / "css"
    if not gitkeep_only(css_dir):
        errors.append("site/static/css/ must remain .gitkeep-only")
    if css_dir.exists() and list(css_dir.rglob("*.css")):
        errors.append("no .css files may exist under site/static/css/")
    if [path for path in root.rglob("*.css") if ".git" not in path.parts]:
        errors.append("no CSS files may exist anywhere in the repository")

    for token in REQUIRED_COLOR_TOKENS:
        if token not in registry.get("color_tokens", {}):
            errors.append(f"color_tokens missing role: {token}")
    for token in REQUIRED_TYPOGRAPHY_TOKENS:
        if token not in registry.get("typography_tokens", {}):
            errors.append(f"typography_tokens missing role: {token}")
    for token in REQUIRED_SPACING_TOKENS:
        if token not in registry.get("spacing_tokens", {}):
            errors.append(f"spacing_tokens missing role: {token}")

    prohibited = [str(item).lower() for item in registry.get("prohibited_visual_directions", [])]
    for direction in REQUIRED_PROHIBITED_DIRECTIONS:
        if direction.lower() not in prohibited:
            errors.append(f"prohibited_visual_directions missing: {direction}")
    generic_conventions = [str(item).lower() for item in registry.get("prohibited_generic_conventions", [])]
    for convention in REQUIRED_GENERIC_CONVENTIONS:
        if convention.lower() not in generic_conventions:
            errors.append(f"prohibited_generic_conventions missing: {convention}")
    violet_gold_text = " ".join(str(item).lower() for item in registry.get("violet_gold_identity_field", []))
    for term in REQUIRED_VIOLET_GOLD_TERMS:
        if term not in violet_gold_text:
            errors.append(f"violet_gold_identity_field must mention: {term}")
    sovereignty_text = " ".join([str(registry.get("visual_sovereignty", "")).lower()] + [str(item).lower() for item in registry.get("proprietary_visual_standard", [])])
    for term in ["sovereign assets define category conventions", "proprietary", "invented"]:
        if term not in sovereignty_text:
            errors.append(f"visual sovereignty/proprietary standard must mention: {term}")
    activation = " ".join(str(item).lower() for item in registry.get("css_activation_conditions", []))
    for term in REQUIRED_CSS_ACTIVATION_TERMS:
        if term not in activation:
            errors.append(f"css_activation_conditions must mention: {term}")

    for text in [item.lower() for item in flatten_strings(registry)]:
        for prohibited_ref in PROHIBITED_REGISTRY_REFERENCES:
            if prohibited_ref in text:
                errors.append(f"design_tokens.json must not reference fonts or external assets: {prohibited_ref}")
        for pattern in CSS_DECLARATION_PATTERNS:
            if pattern in text:
                errors.append(f"design_tokens.json must not contain actual CSS declaration syntax: {pattern}")

    if design_doc.exists():
        content = design_doc.read_text(encoding="utf-8")
        lower_content = content.lower()
        for heading in REQUIRED_DOCUMENT_HEADINGS:
            if heading not in content:
                errors.append(f"architecture/DESIGN_TOKENS.md missing heading: {heading}")
        for phrase in REQUIRED_DOCUMENT_STATE:
            if phrase not in lower_content:
                errors.append(f"architecture/DESIGN_TOKENS.md missing construction-state phrase: {phrase}")

    if errors:
        fail("; ".join(errors))
    pass_message("design token contract and registry are reserved, non-public, and CSS-free")


if __name__ == "__main__":
    main()
