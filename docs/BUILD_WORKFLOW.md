# Build Workflow

No build workflow is active in Sprint 3. This document defines the future workflow that must exist before public site construction or deployment.

GitHub is the source of truth for committed repository state. Local changes are not authoritative until reviewed, committed, and pushed.

## Future Workflow

1. Doctrine check: confirm the proposed work aligns with StrongAvatar.com as the global reference layer for avatar strength, synthetic likeness governance, and digital identity trust.
2. Registry update: add or update records in `site/data/` before any page, content file, route, or navigation item is created.
3. Content drafting: draft only approved content in the correct `site/content/` area after registry approval.
4. Source review: verify factual, legal, technical, comparative, and market claims against the source registry.
5. Internal link planning: define required inbound, outbound, and contextual links before publication.
6. SEO review: confirm title, description, canonical URL, SEO cluster, intent uniqueness, and indexing status.
7. Build: run the approved publishing engine only after registries, content, templates, and scripts exist.
8. Validation: run content, links, SEO, sources, monetization, buyer logic, thin-page, dead-route, and quality-gate checks.
9. Report review: inspect generated audits in `site/reports/`.
10. Commit: commit only approved source files and reviewed generated outputs when applicable.
11. Deployment: deploy only after the quality gate passes.

## Failure Standard

The workflow must stop when a page is unregistered, unsourced where needed, internally orphaned, SEO-incomplete, strategically unclear, thin, placeholder, duplicate in intent, or monetization-violating.

## Current Stop Condition

Do not build the website yet. Do not create public pages, CSS, HTML templates, JavaScript, generated site files, monetization scripts, affiliate links, placeholder content, or thin SEO pages.
