---
route: /ontology/
title: Avatar Integrity Ontology — Weakness Classes and Governance Components
meta_description: The Avatar Integrity Ontology defines ten weakness classes (W-01–W-10) and eight governance components (C-01–C-08) that classify and remediate governance failures in synthetic avatar deployments.
canonical: https://strongavatar.com/ontology/
seo_cluster: avatar governance ontology, digital identity governance, synthetic avatar integrity
template: reference_page
publication_state: reserved, non-public, non-indexable
source_requirement: internal doctrine; legal, technical, and regulatory claims require external sources before publication
last_reviewed: 2026-06-16
ontology_ref: hub
---

# Avatar Integrity Ontology

The Avatar Integrity Ontology is the classification framework that underlies the Strong Avatar Standard and the Avatar Strength Assessment Protocol. It defines what governance failure looks like for a deployed synthetic avatar, and what structural mechanisms remediate each failure.

The ontology is not an aesthetic standard. It does not classify whether an avatar looks good, sounds convincing, or performs well on a platform. It classifies whether the avatar's identity, consent, provenance, disclosure, scope, revocability, and accountability are governed and verifiable.

---

## What the Ontology Classifies

The ontology consists of two tables:

**Weakness classes (W-01–W-10)** name observable governance failures. A weakness class is active when a specific governance gap exists in a deployed avatar — when a protocol assessment produces an answer that indicates the gap is present. Weakness classes are not subjective; they are determined by structured protocol inputs.

**Governance components (C-01–C-08)** name structural mechanisms that eliminate or reduce weakness classes. A component is a remediating action or system — something the deploying party can build or document to close a governance gap.

The relationship between weakness classes and governance components is deterministic: each weakness class maps to a primary remediating component (and sometimes a secondary one). Implementing the primary component for a given weakness class is the direct path to resolving it.

---

## Weakness Classes

Ten weakness classes classify the observable governance failures of synthetic avatar deployments. Each class has a stable identifier (W-01 through W-10) that is permanent once assigned.

### W-01 — Consent Absence
No documented authority exists for the use of the likeness or identity represented by the avatar. The deployment proceeds without an explicit, reviewable consent basis. Remediates via [C-01 Consent Infrastructure](/component/consent-infrastructure/).

### W-02 — Provenance Void
No traceable chain exists from the source identity to the deployed avatar. The avatar's origin cannot be established or verified. Remediates via [C-02 Provenance and Content Credentials Layer](/component/provenance-chain/).

### W-03 — Disclosure Failure
The synthetic nature of the avatar is not communicated in contexts where a viewer or user would reasonably need to know. Remediates via [C-03 Disclosure Layer](/component/disclosure-protocol/).

### W-04 — Identity Drift
The avatar acts, appears, or is used in ways that diverge from its authorized identity scope. Remediates via [C-04 Scope and Usage Binding](/component/scope-binding/).

### W-05 — Impersonation Exposure
The avatar can be cloned or repurposed to impersonate a real person without detection. Remediates via [C-05 Anti-Impersonation Controls](/component/anti-impersonation-layer/).

### W-06 — Rights Ambiguity
The chain of title for the identity or likeness is unclear, incomplete, or contested. Remediates via [C-06 Rights Chain Documentation](/component/rights-registry/).

### W-07 — Revocation Gap
No mechanism exists to withdraw consent or decommission the avatar. Remediates via [C-07 Revocation and Kill-Switch Mechanism](/component/revocation-mechanism/).

### W-08 — Context Collapse
The avatar is reused outside its authorized context, platform, or audience without re-authorization. Remediates via [C-04 Scope and Usage Binding](/component/scope-binding/).

### W-09 — Attribution Loss
No durable binding exists between the avatar and an accountable owner or responsible party. Remediates via [C-08 Attribution and Accountable-Owner Binding](/component/attribution-binding/).

### W-10 — Robustness Weakness
The avatar or its governance infrastructure is vulnerable to adversarial tampering or spoofing. Remediates via [C-02 Provenance and Content Credentials Layer](/component/provenance-chain/).

Full definitions, observable signals, compounding relationships, and assessment mappings for each class are on the individual weakness class reference pages linked above.

---

## Governance Components

Eight governance components define the structural mechanisms that close governance gaps.

| Component | Remediates |
|---|---|
| [C-01 Consent Infrastructure](/component/consent-infrastructure/) | W-01, W-06 (secondary), W-07 (secondary) |
| [C-02 Provenance and Content Credentials Layer](/component/provenance-chain/) | W-02, W-10 |
| [C-03 Disclosure Layer](/component/disclosure-protocol/) | W-03 |
| [C-04 Scope and Usage Binding](/component/scope-binding/) | W-04, W-08 |
| [C-05 Anti-Impersonation Controls](/component/anti-impersonation-layer/) | W-05, W-10 (secondary) |
| [C-06 Rights Chain Documentation](/component/rights-registry/) | W-06 |
| [C-07 Revocation and Kill-Switch Mechanism](/component/revocation-mechanism/) | W-07 |
| [C-08 Attribution and Accountable-Owner Binding](/component/attribution-binding/) | W-09 |

---

## Compounding Relationships

Weakness classes do not exist in isolation. Some classes compound: when one is present, it increases the severity or probability of another. The compounding relationships documented in this ontology are:

- W-01 compounds with W-06 and W-07: consent absence creates rights ambiguity and makes revocation undefined
- W-02 compounds with W-01 and W-09: provenance void makes consent verification impossible and breaks attribution
- W-03 compounds with W-04 and W-08: disclosure failure enables identity drift and context collapse
- W-04 compounds with W-01 and W-08: identity drift indicates scope violation and accelerates context collapse
- W-05 compounds with W-02 and W-10: impersonation exposure is enabled by provenance gaps and robustness failures
- W-06 compounds with W-01 and W-07: rights ambiguity undermines consent validity and revocability
- W-09 compounds with W-02 and W-06: attribution loss compounds provenance void and rights ambiguity

Compounding relationships are identified in the protocol output when multiple weakness classes are active simultaneously.

---

## Entry Criteria

A weakness class or governance component may not be added to this ontology without meeting documented entry criteria. For weakness classes: the failure must be distinct, observable, detectable through structured protocol inputs, and deterministically assessable. For governance components: the mechanism must be distinct, demonstrably remediating, and independently implementable.

The identifiers W-01 through W-10 and C-01 through C-08 are permanent. No identifier may be reassigned or deleted; deprecated classes carry a superseding note.

---

## Relationship to the Standard and Protocol

The ontology defines *what is wrong* and *what remediates it*. The [Strong Avatar Standard](/standard/) uses these classes to define four strength bands (Ungoverned, Provisional, Governed, Sovereign). The [Avatar Strength Assessment Protocol](/protocol/) uses structured inputs to determine which weakness classes are active for a given deployment.

These three documents form a complete, deterministic assessment system: protocol inputs → weakness class activations → band determination → component remediation path.

---

## Source Note

This ontology is internal doctrine under the Sovereign Asset System. Legal, regulatory, and technical claims require external source documentation before publication. No external sources are currently active. Methodology claims are governed by the Avatar Strength Assessment Protocol and the Decision Log.
