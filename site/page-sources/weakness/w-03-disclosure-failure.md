---
route: /weakness/disclosure-failure/
title: W-03: Disclosure Failure — Avatar Governance Weakness Class
meta_description: W-03 Disclosure Failure classifies synthetic avatar deployments where the synthetic nature of the avatar is not communicated in contexts where a viewer would reasonably need to know.
canonical: https://strongavatar.com/weakness/disclosure-failure/
seo_cluster: synthetic media disclosure, avatar disclosure requirement, digital identity transparency
template: reference_page
publication_state: reserved, non-public, non-indexable
source_requirement: internal doctrine; legal and regulatory claims require external sources before publication
last_reviewed: 2026-06-16
ontology_ref: W-03
---

# W-03: Disclosure Failure

## Definition

The synthetic nature of the avatar is not communicated in contexts where a viewer, user, or counterparty would reasonably need to know they are interacting with a synthetic representation rather than a real person.

---

## Why This Matters

Disclosure is the transparency claim that grounds every other governance assertion. Audiences, users, regulators, and counterparties have an interest in knowing whether they are interacting with a synthetic representation. Regulatory frameworks for synthetic media — including those emerging under AI governance and deepfake legislation — consistently require disclosure as a baseline obligation. An avatar that is undisclosed as synthetic cannot participate in any legitimate governance framework.

---

## Observable Signals

A deployment exhibits W-03: Disclosure Failure when one or more of the following is present:

- No disclosure label, indicator, or watermark is present in deployments where synthetic origin is material to the interaction
- Synthetic origin is actively concealed or implied to be human
- Disclosure is present in one channel but absent in others where the same avatar is deployed

---

## Compounding Relationships

W-03: Disclosure Failure compounds with:

- [W-04 Identity Drift](/weakness/identity-drift/)
- [W-08 Context Collapse](/weakness/context-collapse/)

Disclosure failure compounds with identity drift (W-04) because an undisclosed avatar has no enforced scope boundary — there is nothing preventing it from being used in roles or statements beyond its authorized identity. It compounds with context collapse (W-08) because an avatar without disclosure requirements can be redeployed in new contexts without the additional transparency obligations that would otherwise accompany context change.

---

## Remediation Path

The primary remediation is [C-03 Disclosure Layer](/component/disclosure-layer/): a mechanism for communicating synthetic origin in all deployment contexts where it is material. Disclosure must be context-appropriate — a video avatar requires different disclosure from a conversational AI interface — and cannot be buried, minimized, or conditioned on user action.

---

## Band Implication

W-03 active → **Ungoverned** (unconditional). Disclosure in at least one material deployment context is a minimum foundation requirement.

See the [Strong Avatar Standard](/standard/) for full band determination rules.

---

## Protocol Assessment

**Questions mapping to this class:** C1 (Synthetic Disclosure)

Protocol input C1 determines W-03 status. C1-N (no disclosure in material deployment contexts) activates W-03 as active. C1-P (disclosure present in some but not all material contexts) activates W-03 as partial. C1-Y deactivates W-03.

**Assessment dimension mapping:** Synthetic Trust (primary), Identity Integrity (secondary)

---

## Source Note

This weakness class definition is internal doctrine under the Sovereign Asset System, governed by the [Avatar Integrity Ontology](/ontology/). The identifier W-03 is permanent. Legal and regulatory claims require external source documentation before publication.

See also: [Avatar Strength Assessment Protocol](/protocol/) · [Strong Avatar Standard](/standard/)
