---
route: /weakness/context-collapse/
title: W-08: Context Collapse — Avatar Governance Weakness Class
meta_description: W-08 Context Collapse classifies synthetic avatar deployments reused outside their authorized context or platform without renewed consent, provenance verification, or scope confirmation.
canonical: https://strongavatar.com/weakness/context-collapse/
seo_cluster: avatar context governance, synthetic identity platform portability, digital likeness reuse
template: reference_page
publication_state: reserved, non-public, non-indexable
source_requirement: internal doctrine; legal and regulatory claims require external sources before publication
last_reviewed: 2026-06-16
ontology_ref: W-08
---

# W-08: Context Collapse

## Definition

The avatar is reused outside its authorized context, platform, or audience. A deployment authorized for one context is applied in another without renewal of consent, provenance verification, or scope confirmation.

---

## Why This Matters

Context collapse is the portability failure of governance. As avatars become more portable — usable across platforms, contexts, and audiences — the governance obligations of each context must travel with the avatar. An avatar governed for one platform is not automatically governed for another. Context collapse is particularly important in commercial deployment, where the same avatar may need to operate across jurisdictions, audience types, and platform environments with different regulatory requirements.

---

## Observable Signals

A deployment exhibits W-08: Context Collapse when one or more of the following is present:

- Avatar originally authorized for one platform or audience appears in another without documented re-authorization
- Context-specific disclosures are not adapted when the avatar moves to a new deployment context
- Consent basis does not specify permitted contexts, creating ambiguity that enables expansion

---

## Compounding Relationships

W-08: Context Collapse compounds with:

- [W-03 Disclosure Failure](/weakness/disclosure-failure/)
- [W-04 Identity Drift](/weakness/identity-drift/)

Context collapse compounds with disclosure failure (W-03) because an avatar redeployed in a new context carries old disclosure requirements that may not apply. A disclosure adequate for one context may be absent, misleading, or inadequate in another. It compounds with identity drift (W-04) because context change without re-authorization is a mechanism for identity drift — the avatar begins acting in contexts its authorized identity never covered.

---

## Remediation Path

The primary remediation is [C-04 Scope and Usage Binding](/component/scope-usage-binding/): a documented boundary specifying permitted contexts, platforms, and audiences. Any use outside the binding requires explicit re-authorization. Secondary remediation includes [C-03 Disclosure Layer](/component/disclosure-layer/) to ensure disclosure obligations are context-adapted when the avatar moves to a new deployment.

---

## Band Implication

W-08 active → at minimum **Provisional** (assuming W-01, W-02, W-03 are mitigated). Context collapse that is not caught by scope binding indicates an incomplete governance layer.

See the [Strong Avatar Standard](/standard/) for full band determination rules.

---

## Protocol Assessment

**Questions mapping to this class:** A2 (Consent Scope), D1 (Usage Scope Binding)

Protocol inputs A2 and D1 both map to W-08. W-08 is active if D1 is N. W-08 is partial if A2 is P or N while D1 is P.

**Assessment dimension mapping:** Platform Portability (primary), Long-Term Narrative Coherence (secondary)

---

## Source Note

This weakness class definition is internal doctrine under the Sovereign Asset System, governed by the [Avatar Integrity Ontology](/ontology/). The identifier W-08 is permanent. Legal and regulatory claims require external source documentation before publication.

See also: [Avatar Strength Assessment Protocol](/protocol/) · [Strong Avatar Standard](/standard/)
