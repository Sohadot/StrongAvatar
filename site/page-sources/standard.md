---
route: /standard/
title: Strong Avatar Standard — Four-Band Governance Classification
meta_description: The Strong Avatar Standard defines four strength bands—Ungoverned, Provisional, Governed, Sovereign—that classify the governance integrity of deployed synthetic avatars and digital likenesses.
canonical: https://strongavatar.com/standard/
seo_cluster: avatar governance standard, digital identity trust, synthetic avatar compliance
template: reference_page
publication_state: reserved, non-public, non-indexable
source_requirement: internal doctrine; legal and regulatory claims require external sources before publication
last_reviewed: 2026-06-16
ontology_ref: hub
---

# Strong Avatar Standard

The Strong Avatar Standard defines what *good* means for a deployed avatar or digital likeness. It establishes four governance strength bands — Ungoverned, Provisional, Governed, and Sovereign — that any practitioner can determine without author involvement, given the same structured inputs.

The standard governs **identity integrity**: the trustworthiness and accountability of a deployed avatar, independent of its visual realism. An avatar may be photorealistic and fail this standard. An avatar may be stylized and pass it. Realism is not the variable; governance is.

---

## The Four Bands

### Ungoverned

An avatar is Ungoverned when one or more of the following is absent with no mitigation in place:

- Documented consent for the use of the likeness ([W-01 Consent Absence](/weakness/consent-absence/) is active)
- Traceable provenance from source identity to deployment ([W-02 Provenance Void](/weakness/provenance-void/) is active)
- Synthetic disclosure in at least one material deployment context ([W-03 Disclosure Failure](/weakness/disclosure-failure/) is active)

The Ungoverned classification is unconditional. No other governance component compensates for an active W-01, W-02, or W-03. A sophisticated anti-impersonation system does not offset the absence of consent documentation. Provenance infrastructure does not offset the absence of disclosure. The rule is absolute by design: these three foundations are preconditions for any governance claim.

**What this means in practice:** A platform deploying an Ungoverned avatar has no documentation to defend the deployment against legal, regulatory, or trust-and-safety scrutiny. The likeness is in use without established authority, traceability, or transparency.

---

### Provisional

An avatar is Provisional when W-01, W-02, and W-03 are mitigated — consent, provenance, and disclosure are present — but one or more of the following remains unresolved:

- [W-04 Identity Drift](/weakness/identity-drift/): the avatar operates outside its authorized scope
- [W-07 Revocation Gap](/weakness/revocation-gap/): no mechanism exists to withdraw the avatar from deployment
- [W-08 Context Collapse](/weakness/context-collapse/): the avatar has moved into unauthorized contexts
- [W-09 Attribution Loss](/weakness/attribution-loss/): no accountable owner is durably bound to the deployment

Provisional deployments have cleared the foundational threshold but have unresolved gaps that reduce defensibility under audit. The governance language is adopted; the implementation is incomplete.

**What this means in practice:** A Provisional deployment has documentation a legal team can start with but would not survive a formal governance audit. Gap identification — knowing which W-classes are active — is the actionable output at this stage.

---

### Governed

An avatar is Governed when all of the following are documented and verifiable:

- [C-01 Consent Infrastructure](/component/consent-infrastructure/): consent record is producible, scoped, and dated
- [C-02 Provenance and Content Credentials Layer](/component/provenance-chain/): origin chain is established and verifiable
- [C-03 Disclosure Layer](/component/disclosure-protocol/): synthetic origin is communicated in all material deployment contexts
- [C-04 Scope and Usage Binding](/component/scope-binding/): authorized contexts and behaviors are specified
- [C-08 Attribution and Accountable-Owner Binding](/component/attribution-binding/): an accountable owner is identified and bound to the deployment

W-01, W-02, W-03, W-04, and W-09 are all mitigated. Residual weakness classes, if any, are limited to W-05, W-06, W-07, W-08, or W-10 in non-critical dimensions.

**What this means in practice:** A Governed deployment is trustworthy for standard deployment. Its governance can be explained, defended, and audited. It meets the threshold the standard defines as *strong*.

---

### Sovereign

A Governed avatar reaches Sovereign when it also implements:

- [C-07 Revocation and Kill-Switch Mechanism](/component/revocation-mechanism/): a documented revocation process with a defined response time that has been tested
- [C-05 Anti-Impersonation Controls](/component/anti-impersonation-layer/): technical and procedural barriers prevent unauthorized replication
- [C-06 Rights Chain Documentation](/component/rights-registry/): chain of title is complete, current, and producible
- Tamper-evident provenance signals (full C-02 implementation)

No active weakness class W-01 through W-09. W-10 may be present only if a documented mitigation plan is in place and being executed.

**What this means in practice:** A Sovereign deployment is defensible under adversarial scrutiny — by a regulator, a platform trust-and-safety review, or a rights holder asserting a claim. Sovereign is not a permanent designation; governance infrastructure must be maintained to retain it.

---

## Band Determination Rules

1. Assess all weakness classes using the [Avatar Strength Assessment Protocol](/protocol/).
2. If W-01 is active, or W-02 is active, or W-03 is active → **Ungoverned** (unconditional, no exceptions).
3. If W-01, W-02, W-03 are all mitigated, but any of W-04, W-07, W-08, W-09 is active → **Provisional**.
4. If W-01 through W-04, W-08, and W-09 are all mitigated, and W-05, W-06, W-07, W-10 are at most partial → **Governed**.
5. If all Governed criteria are met and C-05, C-06, C-07 are fully implemented with tamper-evident provenance → **Sovereign**.

Rule 2 is evaluated first. No subsequent rules modify its outcome.

---

## What the Standard Does Not Assess

The standard is explicitly silent on: rendering quality, realism, aesthetic coherence, platform engagement, conversion, user experience quality, AI model capability, generation fidelity, brand alignment, and commercial success.

These exclusions are not omissions — they are the thesis. The standard's position is that these variables are irrelevant to governance integrity. A buyer, regulator, or trust-and-safety reviewer who needs to assess an avatar needs the governance classification, not the aesthetic one.

---

## Relationship to the Ontology and Protocol

The standard uses the weakness classes defined in the [Avatar Integrity Ontology](/ontology/) as its classification input. The [Avatar Strength Assessment Protocol](/protocol/) provides the deterministic procedure for determining which weakness classes are active for a given deployment. The three documents form a complete, self-contained assessment system.

---

## Source Note

This standard is internal doctrine under the Sovereign Asset System. Legal and regulatory claims require external source documentation before publication. Band criteria are not set by common practice; they are set by what is defensible under external scrutiny.
