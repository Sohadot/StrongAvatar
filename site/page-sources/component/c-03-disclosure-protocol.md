---
route: /component/disclosure-protocol/
title: C-03: Disclosure Layer — Avatar Governance Component
meta_description: C-03 Disclosure Layer is the governance component that communicates the synthetic nature of an avatar in all deployment contexts where a viewer or counterparty would reasonably need to know.
canonical: https://strongavatar.com/component/disclosure-protocol/
seo_cluster: synthetic media disclosure, avatar transparency, AI avatar disclosure requirement
template: reference_page
publication_state: reserved, non-public, non-indexable
source_requirement: internal doctrine; legal and technical claims require external sources before publication
last_reviewed: 2026-06-16
ontology_ref: C-03
---

# C-03: Disclosure Layer

## Definition

A mechanism for communicating the synthetic nature of the avatar in all deployment contexts where a viewer, user, or counterparty would reasonably need to know. Disclosure must be context-appropriate in form and placement.

---

## Why This Matters

The disclosure layer is the interface between governance and the public. All of the consent, provenance, and scope governance that exists behind a deployment is invisible to viewers unless it is communicated. Disclosure is the governance mechanism that reaches the audience. As synthetic media becomes indistinguishable from real-person media, the disclosure requirement becomes more critical — not less. Audiences, users, and regulators are increasingly focused on whether synthetic origin is communicated, and regulatory frameworks in multiple jurisdictions are moving toward mandatory disclosure requirements.

---

## Remediates

- [W-03 Disclosure Failure](/weakness/disclosure-failure/) (primary)

---

## Implementation Indicators

A deployment has implemented C-03: Disclosure Layer when:

- A disclosure mechanism (label, watermark, metadata, verbal disclosure) is present in every deployment context where synthetic origin is material
- Disclosure is not buried, minimized, or conditioned on user action
- Disclosure adapts to context: a video avatar discloses differently from a conversational AI interface

---

## Full Implementation Requirements

Full implementation requires context-appropriate disclosure in all material deployment contexts. The disclosure mechanism must be prominent enough that a viewer would not reasonably miss it, and must adapt to the deployment medium. C1-Y in the assessment protocol confirms full disclosure layer implementation.

---

## Integration with Other Components

C-03 integrates with [C-04 Scope and Usage Binding](/component/scope-binding/) — when the avatar moves to a new context, the disclosure layer must be reassessed and adapted for that context. The disclosure requirement is not satisfied by importing a prior disclosure into a new deployment without reviewing its appropriateness.

---

## Band Contribution

C-03 implemented deactivates W-03. W-03 deactivated is required to exit **Ungoverned** band. Without C-03 in at least one material context, the deployment is unconditionally Ungoverned.

See the [Strong Avatar Standard](/standard/) for full band determination criteria.

---

## Source Note

This governance component definition is internal doctrine under the Sovereign Asset System, governed by the [Avatar Integrity Ontology](/ontology/). The identifier C-03 is permanent. Legal and technical claims require external source documentation before publication.

See also: [Avatar Strength Assessment Protocol](/protocol/) · [Strong Avatar Standard](/standard/)
