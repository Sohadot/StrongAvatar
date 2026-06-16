---
route: /weakness/identity-drift/
title: W-04: Identity Drift — Avatar Governance Weakness Class
meta_description: W-04 Identity Drift classifies synthetic avatar deployments where the avatar acts, appears, or is used in ways that diverge from its authorized identity scope.
canonical: https://strongavatar.com/weakness/identity-drift/
seo_cluster: avatar identity integrity, digital identity drift, synthetic persona governance
template: reference_page
publication_state: reserved, non-public, non-indexable
source_requirement: internal doctrine; legal and regulatory claims require external sources before publication
last_reviewed: 2026-06-16
ontology_ref: W-04
---

# W-04: Identity Drift

## Definition

The avatar acts, appears, or is used in ways that diverge from its authorized identity scope. The deployed behavior, appearance, or statements differ materially from what consent, provenance, and scope documentation authorize.

---

## Why This Matters

Identity drift represents the failure of scope governance after the foundational consent and provenance questions are resolved. An avatar may have documented consent and clear provenance but still drift because nobody enforced the authorized boundary. Over time, identity drift erodes trust in the governance system: if the avatar behaves in ways the documented scope doesn't authorize, the documentation becomes meaningless. Drift is also a leading indicator of impersonation risk — an avatar that already exceeds its authorized scope is more easily repurposed for impersonation.

---

## Observable Signals

A deployment exhibits W-04: Identity Drift when one or more of the following is present:

- Avatar is used in contexts, roles, or statements beyond those covered by its consent basis
- Appearance has been modified beyond authorized parameters
- Avatar is attributed to a real person in situations the person did not authorize

---

## Compounding Relationships

W-04: Identity Drift compounds with:

- [W-01 Consent Absence](/weakness/consent-absence/)
- [W-08 Context Collapse](/weakness/context-collapse/)

Identity drift compounds with consent absence (W-01) because drift is only detectable when a consent basis exists to compare against — without consent, every use is potentially unauthorized, making drift assessment impossible. It compounds with context collapse (W-08) because an avatar that has drifted from its authorized scope is likely operating in unauthorized contexts, and each new context further expands the scope of the drift.

---

## Remediation Path

The primary remediation is [C-04 Scope and Usage Binding](/component/scope-binding/): a documented boundary that constrains the avatar's authorized use across contexts, platforms, audiences, behaviors, and statements. Any use outside the binding requires explicit re-authorization.

---

## Band Implication

W-04 active → at minimum **Provisional** (assuming W-01, W-02, W-03 are mitigated). Identity drift with no W-01/W-02/W-03 indicates a baseline-compliant but insufficiently bounded deployment.

See the [Strong Avatar Standard](/standard/) for full band determination rules.

---

## Protocol Assessment

**Questions mapping to this class:** A2 (Consent Scope), D1 (Usage Scope Binding)

Protocol inputs A2 and D1 both map to W-04. W-04 is active if either A2 or D1 is N. W-04 is partial if both are P, or one is P and the other is Y.

**Assessment dimension mapping:** Long-Term Narrative Coherence (primary), Identity Integrity (secondary), Likeness Control (secondary)

---

## Source Note

This weakness class definition is internal doctrine under the Sovereign Asset System, governed by the [Avatar Integrity Ontology](/ontology/). The identifier W-04 is permanent. Legal and regulatory claims require external source documentation before publication.

See also: [Avatar Strength Assessment Protocol](/protocol/) · [Strong Avatar Standard](/standard/)
