---
route: /weakness/consent-absence/
title: W-01: Consent Absence — Avatar Governance Weakness Class
meta_description: W-01 Consent Absence classifies deployments where no documented authority exists for using a likeness in a synthetic avatar. Primary weakness in the Avatar Integrity Ontology.
canonical: https://strongavatar.com/weakness/consent-absence/
seo_cluster: avatar consent, digital likeness consent, synthetic avatar governance
template: reference_page
publication_state: reserved, non-public, non-indexable
source_requirement: internal doctrine; legal and regulatory claims require external sources before publication
last_reviewed: 2026-06-16
ontology_ref: W-01
---

# W-01: Consent Absence

## Definition

No documented authority exists for the use of the likeness or identity represented by the avatar. The deployment proceeds without an explicit, reviewable consent basis that specifies who authorized what, for what purpose, in what scope, and for what duration.

---

## Why This Matters

Consent is the foundational authorization claim for any likeness deployment. Without it, no governance framework can be said to exist — there is no authority to audit, no scope to enforce, and no accountability chain to trace. Legal and regulatory scrutiny of synthetic media focuses first on consent status because it is the precondition for every other governance claim.

---

## Observable Signals

A deployment exhibits W-01: Consent Absence when one or more of the following is present:

- No consent agreement, license, or authorization record is producible on request
- The avatar replicates a real person's appearance, voice, or manner without traceable permission
- Synthetic likeness is derived from a source whose consent status is undocumented or ambiguous

---

## Compounding Relationships

W-01: Consent Absence compounds with:

- [W-06 Rights Ambiguity](/weakness/rights-ambiguity/)
- [W-07 Revocation Gap](/weakness/revocation-gap/)

Consent absence creates rights ambiguity (W-06) because the basis for any rights claim is undefined. It also makes revocation undefined (W-07) because a withdrawal mechanism presupposes that consent was established in the first place.

---

## Remediation Path

The primary remediation is [C-01 Consent Infrastructure](/component/consent-infrastructure/): a documented system for recording who authorized what, under what scope, and for how long. Secondary remediation paths include [C-06 Rights Chain Documentation](/component/rights-chain-documentation/) to establish the chain of title that underlies any consent claim.

---

## Band Implication

W-01 active → **Ungoverned** (unconditional). No other governance component compensates for absent consent.

See the [Strong Avatar Standard](/standard/) for full band determination rules.

---

## Protocol Assessment

**Questions mapping to this class:** A1 (Consent Documentation), A2 (Consent Scope)

Protocol inputs A1 and A2 determine W-01 status. A1-N (no consent record) activates W-01 as active. A1-P (consent record exists but lacks scope, dating, or required elements) activates W-01 as partial. A1-Y and A2-Y together deactivate W-01.

**Assessment dimension mapping:** Consent Clarity (primary), Likeness Control (secondary)

---

## Source Note

This weakness class definition is internal doctrine under the Sovereign Asset System, governed by the [Avatar Integrity Ontology](/ontology/). The identifier W-01 is permanent. Legal and regulatory claims require external source documentation before publication.

See also: [Avatar Strength Assessment Protocol](/protocol/) · [Strong Avatar Standard](/standard/)
