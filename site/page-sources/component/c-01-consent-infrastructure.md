---
route: /component/consent-infrastructure/
title: C-01: Consent Infrastructure — Avatar Governance Component
meta_description: C-01 Consent Infrastructure is the governance component that documents the authority under which a synthetic avatar likeness is used — recording scope, duration, and conditions for renewal or withdrawal.
canonical: https://strongavatar.com/component/consent-infrastructure/
seo_cluster: avatar consent management, synthetic avatar authorization, digital likeness consent
template: reference_page
publication_state: reserved, non-public, non-indexable
source_requirement: internal doctrine; legal and technical claims require external sources before publication
last_reviewed: 2026-06-16
ontology_ref: C-01
---

# C-01: Consent Infrastructure

## Definition

A documented system for recording, scoping, and maintaining the authority under which a likeness is used. At minimum: identity of the consenting party, scope of permitted use, duration, and conditions for renewal or withdrawal.

---

## Why This Matters

Consent infrastructure is the starting point of governed avatar deployment. Before a likeness can be governed, it must be authorized. Before it can be authorized, that authorization must be documented in a form that is producible, scoped, and time-bounded. The infrastructure requirement is not satisfied by an informal agreement, a general terms of service acceptance, or an oral authorization — it requires a documented record specific to the likeness and the deployment.

---

## Remediates

- [W-01 Consent Absence](/weakness/consent-absence/) (primary)
- [W-06 Rights Ambiguity](/weakness/rights-ambiguity/) (secondary)
- [W-07 Revocation Gap](/weakness/revocation-gap/) (secondary)

---

## Implementation Indicators

A deployment has implemented C-01: Consent Infrastructure when:

- A consent record exists, is dated, and specifies the authorized use scope
- The consent record is producible on request by the subject, the deploying platform, or a regulator
- The record includes an expiry date or a renewal mechanism

---

## Full Implementation Requirements

Full implementation of C-01 satisfies A1-Y and A2-Y in the assessment protocol: the consent record exists, is dated, specifies contexts, platforms, and duration, and is producible on request. Secondary contribution to W-06 mitigation requires that the consent basis aligns with a documented rights chain (C-06). Secondary contribution to W-07 mitigation requires that the consent basis includes withdrawal and expiry terms (which also supports C-07).

---

## Integration with Other Components

C-01 integrates with [C-06 Rights Chain Documentation](/component/rights-registry/) to ensure that the person granting consent holds or has been assigned the rights to do so. C-01 also integrates with [C-07 Revocation and Kill-Switch Mechanism](/component/revocation-mechanism/) — the consent infrastructure must include withdrawal terms that the revocation mechanism can enforce.

---

## Band Contribution

C-01 implemented deactivates W-01. W-01 deactivated is required to exit **Ungoverned** band. Without C-01, no other component can prevent Ungoverned classification.

See the [Strong Avatar Standard](/standard/) for full band determination criteria.

---

## Source Note

This governance component definition is internal doctrine under the Sovereign Asset System, governed by the [Avatar Integrity Ontology](/ontology/). The identifier C-01 is permanent. Legal and technical claims require external source documentation before publication.

See also: [Avatar Strength Assessment Protocol](/protocol/) · [Strong Avatar Standard](/standard/)
