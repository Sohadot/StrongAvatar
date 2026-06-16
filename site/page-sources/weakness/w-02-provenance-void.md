---
route: /weakness/provenance-void/
title: W-02: Provenance Void — Avatar Governance Weakness Class
meta_description: W-02 Provenance Void classifies synthetic avatar deployments where no traceable chain exists from source identity to deployed avatar. The origin of the likeness cannot be verified.
canonical: https://strongavatar.com/weakness/provenance-void/
seo_cluster: avatar provenance, digital identity provenance, synthetic media governance
template: reference_page
publication_state: reserved, non-public, non-indexable
source_requirement: internal doctrine; legal and regulatory claims require external sources before publication
last_reviewed: 2026-06-16
ontology_ref: W-02
---

# W-02: Provenance Void

## Definition

No traceable chain exists from the source identity (real or synthetic) to the deployed avatar. The avatar's origin — who it was derived from, what training data or capture process created it, and what transformations were applied — cannot be established or verified.

---

## Why This Matters

Provenance is the technical and documentary foundation for all downstream governance claims. A consent record is only meaningful if the identity being consented to can be traced to the deployed avatar. Disclosure requirements depend on knowing what synthetic origin the avatar has. Rights documentation requires knowing what source material was used. Provenance void undermines every other governance claim because it eliminates the factual basis on which those claims rest.

---

## Observable Signals

A deployment exhibits W-02: Provenance Void when one or more of the following is present:

- No content credentials, provenance metadata, or origin documentation is attached to or associated with the avatar
- The generation or capture process is undocumented
- No binding exists between the deployed avatar and a verifiable source identity

---

## Compounding Relationships

W-02: Provenance Void compounds with:

- [W-01 Consent Absence](/weakness/consent-absence/)
- [W-09 Attribution Loss](/weakness/attribution-loss/)

Provenance void compounds with consent absence (W-01) because without a traceable origin, the consent basis cannot be verified. It compounds with attribution loss (W-09) because provenance is the mechanism through which attribution chains are constructed and maintained.

---

## Remediation Path

The primary remediation is [C-02 Provenance and Content Credentials Layer](/component/provenance-chain/): a mechanism for establishing and preserving the traceable origin chain, including content credentials aligned with provenance standards such as C2PA where applicable. The provenance layer must persist through distribution — not just exist at creation — to satisfy the full requirement.

---

## Band Implication

W-02 active → **Ungoverned** (unconditional). An avatar with no traceable origin cannot be governed regardless of what other documentation exists.

See the [Strong Avatar Standard](/standard/) for full band determination rules.

---

## Protocol Assessment

**Questions mapping to this class:** B1 (Origin Documentation), B2 (Content Credentials)

Protocol inputs B1 and B2 determine W-02 status. B1-N (no origin documentation) activates W-02 as active. B2-N (no content credentials) is a secondary activation signal. Full deactivation requires both B1-Y and B2-Y.

**Assessment dimension mapping:** Identity Integrity (primary), Synthetic Trust (secondary)

---

## Source Note

This weakness class definition is internal doctrine under the Sovereign Asset System, governed by the [Avatar Integrity Ontology](/ontology/). The identifier W-02 is permanent. Legal and regulatory claims require external source documentation before publication.

See also: [Avatar Strength Assessment Protocol](/protocol/) · [Strong Avatar Standard](/standard/)
