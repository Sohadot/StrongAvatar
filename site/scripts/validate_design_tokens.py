from __future__ import annotations

from pathlib import Path
from typing import Any

from validation_utils import fail, load_json, pass_message, repo_root


REQUIRED_TOP_LEVEL_FIELDS = [
    "status", "css_exists", "public_enabled", "output_allowed",
    "css_authorized", "css_authorized_file", "css_authorization_scope",
    "css_public_surface", "css_output_allowed", "css_constraints",
    "css_validation_expectations",
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
AUTHORIZED_CSS_FILE = Path("site/static/css/main.css")
AUTHORIZED_HTML_FILES = {
    Path("site/templates/base.html"),
    Path("site/templates/homepage.html"),
}
PLANNED_TEMPLATE_FILES = {
    "reference-page.html",
    "protocol-page.html",
    "comparison-page.html",
    "glossary-term.html",
    "brief-page.html",
    "strategic-asset-page.html",
}
PUBLIC_HTML_PATTERNS = [
    "<article",
    "create your ai avatar",
    "generate your avatar",
    "start now",
    "buy now",
    "affiliate",
    "sponsored placement",
    "google analytics",
    "google tag manager",
    "tracking pixel",
    "lorem ipsum",
    "coming soon",
]
JAVASCRIPT_EXTENSIONS = {".js", ".mjs", ".cjs", ".jsx", ".ts", ".tsx"}
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico", ".avif"}
CSS_PROHIBITED_PATTERNS = [
    "@import",
    "url(",
    "http://",
    "https://",
    ".woff",
    ".woff2",
    ".ttf",
    ".otf",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".webp",
    "webxr",
    "webgl",
    "three.js",
    "threejs",
    "tracking",
    "ads",
    "affiliate",
    "monetization script",
    "javascript dependency",
    ".homepage",
    ".homepage-hero",
    "cyberpunk",
    "neon chaos",
    "gaming hud",
    "avatar generator",
    "fandom styling",
    "cheap luxury gold",
    "generic saas gradient",
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


def gitkeep_or_authorized_css_only(path: Path, authorized_css: Path) -> bool:
    if not path.exists():
        return False
    files = [file for file in path.rglob("*") if file.is_file()]
    allowed = {".gitkeep", authorized_css.name}
    return all(file.name in allowed for file in files)


def tracked_files(root: Path, pattern: str) -> list[Path]:
    return sorted(path for path in root.rglob(pattern) if ".git" not in path.parts and path.is_file())


def main() -> None:
    root = repo_root()
    errors: list[str] = []
    design_doc = root / "architecture" / "DESIGN_TOKENS.md"
    registry = load_json("site/data/design_tokens.json")
    site = load_json("site/data/site.json")

    if site.get("public_publishing_enabled") is not False:
        errors.append("public_publishing_enabled must remain false during sovereign foundation mode")

    if not design_doc.exists():
        errors.append("architecture/DESIGN_TOKENS.md must exist")
    for field in REQUIRED_TOP_LEVEL_FIELDS:
        if field not in registry:
            errors.append(f"design_tokens.json missing required field: {field}")
    if registry.get("status") != "contract_created":
        errors.append("design_tokens.json status must be contract_created")
    if registry.get("css_exists") is not True:
        errors.append("design_tokens.json css_exists must be true for the authorized foundation CSS")
    if registry.get("css_authorized") is not True:
        errors.append("design_tokens.json css_authorized must be true when css_exists is true")
    if registry.get("css_authorized_file") != "site/static/css/main.css":
        errors.append("css_authorized_file must be site/static/css/main.css")
    if registry.get("css_authorization_scope") != "foundation_only":
        errors.append("css_authorization_scope must be foundation_only")
    if registry.get("css_public_surface") is not False:
        errors.append("css_public_surface must be false")
    if registry.get("css_output_allowed") is not False:
        errors.append("css_output_allowed must be false")
    if registry.get("public_enabled") is not False:
        errors.append("design_tokens.json public_enabled must be false")
    if registry.get("output_allowed") is not False:
        errors.append("design_tokens.json output_allowed must be false")

    css_dir = root / "site" / "static" / "css"
    authorized_css = root / AUTHORIZED_CSS_FILE
    if not gitkeep_or_authorized_css_only(css_dir, authorized_css):
        errors.append("site/static/css/ must contain only .gitkeep and main.css")
    css_files = [path for path in root.rglob("*.css") if ".git" not in path.parts]
    if sorted(path.relative_to(root).as_posix() for path in css_files) != ["site/static/css/main.css"]:
        errors.append("site/static/css/main.css must be the only CSS file in the repository")
    if not authorized_css.exists():
        errors.append("site/static/css/main.css must exist when css_exists is true")

    output_dir = root / "output"
    if not gitkeep_only(output_dir):
        errors.append("output/ must remain .gitkeep-only")

    authorized_html_files = {root / html_file for html_file in AUTHORIZED_HTML_FILES}
    html_files = tracked_files(root, "*.html")
    allowed_html = {path.resolve() for path in authorized_html_files}
    unauthorized_html = [path for path in html_files if path.resolve() not in allowed_html]
    if unauthorized_html:
        unauthorized = ", ".join(path.relative_to(root).as_posix() for path in unauthorized_html)
        errors.append(f"unauthorized HTML files exist: {unauthorized}")
    for authorized_html in authorized_html_files:
        if authorized_html.exists():
            html_text = authorized_html.read_text(encoding="utf-8").lower()
            for pattern in PUBLIC_HTML_PATTERNS:
                if pattern in html_text:
                    relative_html = authorized_html.relative_to(root).as_posix()
                    errors.append(f"{relative_html} suggests a public page was created: {pattern}")
    templates_dir = root / "site" / "templates"
    template_html = tracked_files(templates_dir, "*.html") if templates_dir.exists() else []
    unauthorized_template_html = [path for path in template_html if path.resolve() not in allowed_html]
    if unauthorized_template_html:
        unauthorized = ", ".join(path.relative_to(root).as_posix() for path in unauthorized_template_html)
        errors.append(f"site/templates/ contains unauthorized HTML templates: {unauthorized}")
    content_html = tracked_files(root / "site" / "content", "*.html")
    if content_html:
        unauthorized = ", ".join(path.relative_to(root).as_posix() for path in content_html)
        errors.append(f"site/content/ contains unauthorized HTML: {unauthorized}")
    output_html = tracked_files(output_dir, "*.html")
    if output_html:
        unauthorized = ", ".join(path.relative_to(root).as_posix() for path in output_html)
        errors.append(f"output/ contains generated HTML: {unauthorized}")
    for planned_template in PLANNED_TEMPLATE_FILES:
        if (templates_dir / planned_template).exists():
            errors.append(f"unauthorized planned template exists: site/templates/{planned_template}")
    index_files = [path for path in tracked_files(root, "index.html") if path.resolve() not in allowed_html]
    if index_files:
        found = ", ".join(path.relative_to(root).as_posix() for path in index_files)
        errors.append(f"index.html must not exist as generated output: {found}")
    sitemap_files = tracked_files(root, "sitemap.xml")
    if sitemap_files:
        found = ", ".join(path.relative_to(root).as_posix() for path in sitemap_files)
        errors.append(f"sitemap.xml must not exist: {found}")
    robots_files = tracked_files(root, "robots.txt")
    if robots_files:
        found = ", ".join(path.relative_to(root).as_posix() for path in robots_files)
        errors.append(f"robots.txt must not exist: {found}")
    javascript_files = [
        path for path in tracked_files(root, "*")
        if path.suffix.lower() in JAVASCRIPT_EXTENSIONS
    ]
    if javascript_files:
        found = ", ".join(path.relative_to(root).as_posix() for path in javascript_files)
        errors.append(f"JavaScript website files must not exist: {found}")
    image_files = [
        path for path in tracked_files(root, "*")
        if path.suffix.lower() in IMAGE_EXTENSIONS
    ]
    if image_files:
        found = ", ".join(path.relative_to(root).as_posix() for path in image_files)
        errors.append(f"image assets must not exist: {found}")

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

    if authorized_css.exists():
        css_text = authorized_css.read_text(encoding="utf-8").lower()
        for pattern in CSS_PROHIBITED_PATTERNS:
            if pattern in css_text:
                errors.append(f"main.css contains prohibited foundation CSS content: {pattern}")
        if ".page-shell" not in css_text or ".protocol-card" not in css_text:
            errors.append("main.css must remain a foundation primitive layer")

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
    pass_message("design token contract and authorized foundation CSS remain controlled and non-public")


if __name__ == "__main__":
    main()
