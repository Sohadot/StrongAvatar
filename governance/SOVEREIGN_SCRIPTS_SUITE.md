# Sovereign Scripts Suite

The scripts suite is a future automation layer for validation, registry checks, controlled builds, generated audits, and quality-gate enforcement.

Sprint 3 is documentation only. No scripts are implemented.

## Future Script Inventory

- `build.py`: generate approved deployable output from validated registries, content, and templates.
- `generate_sitemap.py`: generate sitemap entries only for approved published indexable pages.
- `generate_robots.py`: generate robots directives from indexing policy.
- `validate_content.py`: verify content purpose, status, structure, and prohibited patterns.
- `validate_links.py`: check internal links, orphan status, and route integrity.
- `validate_seo.py`: verify title, description, canonical URL, SEO cluster, and duplicate intent.
- `validate_assets.py`: verify authorized static asset usage and prevent unmanaged public assets.
- `validate_sources.py`: verify source requirements and source registry references.
- `validate_monetization.py`: reject unauthorized monetization, affiliate links, ads, popups, and sponsorships.
- `validate_buyer_logic.py`: verify reference authority or buyer logic alignment.
- `validate_no_thin_pages.py`: reject thin glossary, comparison, tool, or SEO pages.
- `validate_no_dead_routes.py`: reject broken routes, stale redirects, and missing destination records.
- `quality_gate.py`: aggregate validations and determine whether build or deployment may proceed.

## Script Governance

No script may publish, index, monetize, deploy, or generate public pages without explicit governance rules and review outputs.

Scripts must fail closed. Missing registry data, ambiguous status, incomplete SEO, missing source status, orphaned links, unauthorized monetization, or low-value content must stop the build.

## Current Status

`site/scripts/` is reserved. No executable automation is included. Do not create these scripts until implementation is explicitly authorized.
