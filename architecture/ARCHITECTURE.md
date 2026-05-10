# Architecture

StrongAvatar.com is a sovereign digital asset system, not a simple website repository.

The repository separates doctrine, governance, architecture, source data, controlled content, generated output, workflow documentation, tests, and future deployment enforcement. This separation protects the asset from premature publishing, uncontrolled SEO expansion, and low-trust monetization.

## Core Thesis

StrongAvatar.com is the global reference layer for avatar strength, synthetic likeness governance, and digital identity trust.

A weak avatar is generated. A strong avatar is governed.

The Avatar Strength Protocol is the core conceptual frame. The strategic category is Digital Identity x Synthetic Likeness x AI Avatars, with expansion into Digital Humans, AI Interfaces, Spatial Computing, Creator Identity, Brand Representation, Virtual Personas, Synthetic Media Trust, and Likeness Governance.

## Repository Layer Model

- Root doctrine files define strategic control, asset thesis, quality doctrine, monetization posture, and acquisition posture.
- `governance/` defines content governance, indexing control, publishing control, buyer logic, script doctrine, and prohibited directions.
- `architecture/` defines technical structure, visual system, UI component concepts, and page planning.
- `site/` is the source system for the future public website.
- `site/data/` controls registries for pages, navigation, protocol dimensions, sources, buyer segments, monetization products, redirects, and indexing status.
- `site/content/` will hold controlled content only after page approval.
- `site/templates/` will hold templates only after the publishing system is defined.
- `site/scripts/` will hold build and validation scripts after they are authorized.
- `site/reports/` will hold generated audits and pre-deployment review outputs.
- `output/` is generated deployable output only and must never be edited manually.
- `docs/` documents workflow, SEO, monetization, deployment, and acquisition readiness.
- `.cursor/rules/` preserves agent doctrine.
- `.github/workflows/` will later enforce validation and deployment.
- `tests/` will hold future validation tests and must not imply public publishing readiness.

## Source-Of-Truth Rules

Doctrine defines why the asset exists. Governance defines whether something may be published. Data registries define what may be rendered. Content files provide approved substance. Templates and scripts may only transform approved sources into generated output.

No public page may exist unless it is registered, validated, internally linked, SEO-controlled, sourced where required, and quality-gated.

## Future Data-To-Output Flow

The authorized future flow is:

`site/data/` registry -> approved `site/content/` file -> approved `site/templates/` template -> `site/scripts/` build and validation -> `site/reports/` audit outputs -> generated `output/` files -> `.github/workflows/` deployment.

Any build must fail before output when a page is unregistered, strategically unclear, internally orphaned, SEO-incomplete, unsourced where needed, placeholder, thin, duplicate in intent, or monetization-violating.

## Current Architecture State

No public website is built. No templates, CSS, JavaScript, publishing logic, generated site files, or deployment workflow are active. `output/` is reserved and must remain manually untouched except for preservation files such as `.gitkeep`.
