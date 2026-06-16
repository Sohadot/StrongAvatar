---
route: /component/scope-usage-binding/
title: C-04: Scope and Usage Binding — Avatar Governance Component
meta_description: C-04 Scope and Usage Binding documents the boundary constraining an avatar's authorized use — permitted contexts, platforms, audiences, behaviors, and statements — requiring explicit re-authorization for any use outside the binding.
canonical: https://strongavatar.com/component/scope-usage-binding/
seo_cluster: avatar scope governance, digital identity usage control, synthetic avatar boundary
template: reference_page
publication_state: reserved, non-public, non-indexable
source_requirement: internal doctrine; legal and technical claims require external sources before publication
last_reviewed: 2026-06-16
ontology_ref: C-04
---

# C-04: Scope and Usage Binding

## Definition

A documented boundary that constrains the avatar's authorized use: permitted contexts, platforms, audiences, behaviors, and statements. Any use outside the binding requires explicit re-authorization.

---

## Why This Matters

Scope and usage binding is the operational governance layer that determines whether consent remains valid over time. A consent basis established at deployment begins to erode the moment the avatar operates in a context the consent did not cover. Scope binding is the mechanism that keeps the deployment within the consent boundaries. Without it, the governance framework exists at the moment of consent but does not govern subsequent behavior.

---

## Remediates

- [W-04 Identity Drift](/weakness/identity-drift/) (primary)
- [W-08 Context Collapse](/weakness/context-collapse/) (primary)

---

## Implementation Indicators

A deployment has implemented C-04: Scope and Usage Binding when:

- The consent basis or deployment agreement specifies permitted contexts and behaviors
- A review mechanism exists to detect and flag uses outside the authorized scope
- Platform or distribution re-authorization is required when the avatar moves to a new context

---

## Full Implementation Requirements

Full implementation requires both documented scope boundaries (D1-Y in the assessment protocol) and adequate consent scope specification (A2-Y). D1-Y confirms that authorized behaviors, roles, and statements are documented with a review mechanism. A2-Y confirms that contexts, platforms, and duration are all specified in the consent basis.

---

## Integration with Other Components

C-04 integrates with [C-01 Consent Infrastructure](/component/consent-infrastructure/) — scope binding without a documented consent basis has no authority to reference. C-04 also integrates with [C-03 Disclosure Layer](/component/disclosure-layer/) — disclosure requirements must be context-specific, and scope binding defines what contexts exist and what disclosure is required for each.

---

## Band Contribution

C-04 implemented deactivates W-04 and W-08. W-04 and W-08 deactivated together with W-07 and W-09 are required for **Governed** classification. C-04 is among the five components required for Governed.

See the [Strong Avatar Standard](/standard/) for full band determination criteria.

---

## Source Note

This governance component definition is internal doctrine under the Sovereign Asset System, governed by the [Avatar Integrity Ontology](/ontology/). The identifier C-04 is permanent. Legal and technical claims require external source documentation before publication.

See also: [Avatar Strength Assessment Protocol](/protocol/) · [Strong Avatar Standard](/standard/)
