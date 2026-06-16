---
route: /weakness/rights-ambiguity/
title: W-06: Rights Ambiguity — Avatar Governance Weakness Class
meta_description: W-06 Rights Ambiguity classifies synthetic avatar deployments where the chain of title for the identity or likeness is unclear, incomplete, or contested.
canonical: https://strongavatar.com/weakness/rights-ambiguity/
seo_cluster: avatar rights, likeness rights, digital identity rights chain
template: reference_page
publication_state: reserved, non-public, non-indexable
source_requirement: internal doctrine; legal and regulatory claims require external sources before publication
last_reviewed: 2026-06-16
ontology_ref: W-06
---

# W-06: Rights Ambiguity

## Definition

The chain of title for the identity or likeness used in the avatar is unclear, incomplete, or contested. It cannot be established who holds rights over the likeness, what those rights permit, and whether they have been properly assigned or licensed.

---

## Why This Matters

Rights ambiguity is the legal layer of governance failure. Even when consent is documented, if the person who gave consent did not actually hold rights over the likeness, the consent is invalid. Rights chain documentation is particularly important for synthetic avatars derived from training data, composite identities, or licensed personas — each step in the creation chain potentially introduces a rights claim that must be cleared. For commercial deployment, rights ambiguity creates unquantified exposure that prevents the avatar from being used in commercial contexts, licensed to third parties, or transferred as part of an acquisition.

---

## Observable Signals

A deployment exhibits W-06: Rights Ambiguity when one or more of the following is present:

- No rights documentation exists covering the likeness source
- Rights ownership is disputed or has not been transferred from a prior holder
- Licensing terms are absent, expired, or conflict with the deployment context

---

## Compounding Relationships

W-06: Rights Ambiguity compounds with:

- [W-01 Consent Absence](/weakness/consent-absence/)
- [W-07 Revocation Gap](/weakness/revocation-gap/)

Rights ambiguity compounds with consent absence (W-01) because a consent basis without clear rights documentation cannot establish who is actually authorized to consent. It compounds with revocation gap (W-07) because rights ambiguity makes it unclear who holds the authority to revoke — there is no identified rights holder to exercise withdrawal.

---

## Remediation Path

The primary remediation is [C-06 Rights Chain Documentation](/component/rights-registry/): a documented chain of title establishing who holds rights over the likeness, what those rights permit, and how they have been assigned or licensed to the deploying party. Secondary remediation includes [C-01 Consent Infrastructure](/component/consent-infrastructure/) to ensure the consent basis aligns with the documented rights chain.

---

## Band Implication

W-06 active prevents **Sovereign** classification. W-06 partial allows **Governed** classification. W-06 does not cause Ungoverned or Provisional by itself.

See the [Strong Avatar Standard](/standard/) for full band determination rules.

---

## Protocol Assessment

**Questions mapping to this class:** E1 (Rights Chain)

Protocol input E1 determines W-06 status. E1-N (no rights documentation) activates W-06 as active. E1-P (documentation exists but has gaps) activates W-06 as partial. E1-Y deactivates W-06.

**Assessment dimension mapping:** Likeness Control (primary), Commercial Readiness (secondary)

---

## Source Note

This weakness class definition is internal doctrine under the Sovereign Asset System, governed by the [Avatar Integrity Ontology](/ontology/). The identifier W-06 is permanent. Legal and regulatory claims require external source documentation before publication.

See also: [Avatar Strength Assessment Protocol](/protocol/) · [Strong Avatar Standard](/standard/)
