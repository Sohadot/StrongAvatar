# Architecture

The architecture for StrongAvatar.com must separate doctrine, registries, content, templates, static assets, build outputs, and reports.

## Current Architecture State

This repository contains foundation structure only. No public website is built.

## Architectural Principles

- Registries define what may exist publicly.
- Content files do not self-authorize publication.
- Templates must eventually render only approved registry entries.
- Output must be generated, reviewable, and disposable.
- Reports must support quality control and acquisition diligence.
- Static assets must not precede design governance.

## Future Boundary

Any future build system must enforce the repository rule: no public page may be published unless it is registered, purposeful, sourced where needed, internally linked, SEO-controlled, and quality-gated.
