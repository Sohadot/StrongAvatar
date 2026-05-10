# Sovereign Publishing Engine

The publishing engine is a future system for turning approved registries and governed content into a controlled public website.

Public publishing remains disabled in Sprint 3. This document defines the required future flow only.

## Future Publishing Flow

`data registry -> content file -> template -> build script -> validation scripts -> reports -> output -> workflow deployment`

The flow must be deterministic, auditable, and registry-controlled. A file's existence must never imply public authorization.

## Future Responsibilities

- Read approved records from `site/data/`.
- Resolve approved content files from `site/content/`.
- Render only through approved templates in `site/templates/`.
- Run validation scripts before output generation.
- Generate review reports in `site/reports/`.
- Write generated deployable files only to `output/`.
- Allow workflow deployment only after quality-gate approval.

## Required Failure Conditions

Publishing must fail if any page is:

- Unregistered.
- Missing strategic purpose.
- Missing required internal links.
- Missing SEO fields.
- Missing canonical URL.
- Unsourced where factual, legal, technical, comparative, or market claims require support.
- Placeholder.
- Thin.
- Duplicate in intent.
- Orphaned.
- Monetization-violating.
- Outside buyer logic or reference authority.

## Output Rule

`output/` is generated deployable output only. It must not be edited manually, used for drafting, or treated as source of truth.

## Current Status

No publishing engine is implemented. No templates, scripts, public pages, generated files, or deployment workflow are active.
