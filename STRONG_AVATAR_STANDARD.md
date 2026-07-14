# Strong Avatar Standard

**Version:** 0.2
**Status:** Draft — version 0.2 authorized by DECISION_LOG.md entry dated 2026-07-14 (determinism closure)
**Governed by:** `AVATAR_INTEGRITY_ONTOLOGY.md`, `ASSET_THESIS.md`
**Applied by:** `AVATAR_STRENGTH_ASSESSMENT_PROTOCOL.md`

---

## Purpose

This standard defines what *good* is for a deployed avatar or digital likeness. It translates the Avatar Integrity Ontology's weakness classes and governance components into a published strength determination that any practitioner can apply without the author present.

The standard governs **identity integrity** — the trustworthiness and accountability of a deployed avatar, independent of its realism. An avatar may be photorealistic and fail this standard. An avatar may be stylized and pass it.

---

## Strength Bands

### Ungoverned

**Criterion:** One or more of the following is absent with no mitigation in place:
- Documented consent (C-01)
- Traceable provenance (C-02)
- Synthetic disclosure in at least one material deployment context (C-03)

**What this means:** The avatar is deployed without the minimum governance infrastructure that allows it to be trusted, attributed, or held accountable. Realistic presentation does not offset the absence of these foundations. An Ungoverned classification is immediate and is not moderated by the presence of other governance components.

**Dominant weakness class(es):** W-01, W-02, or W-03. Any one of these, active and unmitigated, is sufficient for Ungoverned classification.

**Stakeholder implications:**

- *Platform:* Deploying an Ungoverned avatar creates unquantified legal, regulatory, and reputational exposure with no documentation to defend the deployment.
- *Legal and trust and safety:* No basis for compliance or accountability exists; the deployment cannot be explained under external scrutiny.
- *Rights holder:* The likeness is in use without documented authority; no revocation path has been established.
- *Acquirer:* An asset whose product validates Ungoverned deployments cannot be positioned as a governance authority. This band is evidence of the category problem the asset exists to solve.

---

### Provisional

**Criterion:** Consent (C-01) and provenance (C-02) both exist but one or more of the following is unverified or incomplete:
- Scope and usage binding (C-04)
- Revocation mechanism (C-07)
- Attribution binding (C-08)

Disclosure (C-03) is present in primary deployment contexts but may not cover all contexts where synthetic origin is material.

**What this means:** The avatar has cleared the minimum threshold — consent and provenance are documented — but its governance is incomplete. It cannot be defended under close scrutiny because key failure modes remain unmitigated.

**Dominant weakness class(es):** W-04, W-07, W-08, or W-09 — one or more present. W-01, W-02, and W-03 are mitigated.

**Stakeholder implications:**

- *Platform:* The deployment has a defensible foundation but would not withstand a formal governance audit.
- *Legal and trust and safety:* Documentation exists, but gaps mean exposure in edge cases or adversarial review.
- *Rights holder:* Revocation or scope enforcement may not be reliable.
- *Acquirer:* Provisional deployments indicate the governance language is adopted and the standard is applicable. The gap identification is the product, not the verdict.

---

### Governed

**Criterion:** All of the following are documented and verifiable:
- Consent infrastructure (C-01): consent record is producible, scoped, and dated
- Provenance layer (C-02): origin chain is established and verifiable
- Disclosure layer (C-03): synthetic origin is communicated in all material deployment contexts
- Scope and usage binding (C-04): authorized contexts and behaviors are specified
- Attribution binding (C-08): an accountable owner is identified and bound to the deployment

No active W-01, W-02, W-03, W-04, or W-09. Residual weaknesses, if any, are limited to W-05, W-06, W-07, W-08, or W-10 in non-critical dimensions.

**What this means:** The avatar is trustworthy for standard deployment. Its governance can be explained, defended, and audited. A Governed avatar meets the threshold the standard defines as *strong*.

**Stakeholder implications:**

- *Platform:* The deployment is defensible under standard scrutiny and audit.
- *Legal and trust and safety:* A Governed deployment produces documentation a legal team can work with.
- *Rights holder:* The likeness is used within documented authority with an attribution trail.
- *Acquirer:* A platform that deploys Governed avatars has adopted the language and the standard. The asset's category position is validated by use.

---

### Sovereign

**Criterion:** All Governed criteria are met, plus:
- Revocation and kill-switch mechanism (C-07): a documented revocation process with a defined response time exists and has been tested
- Anti-impersonation controls (C-05): technical and procedural barriers prevent unauthorized replication
- Rights chain documentation (C-06): chain of title is complete, current, and producible
- Provenance signals are tamper-evident (C-02 at full implementation)

No active or partial weakness classes W-01 through W-10 may remain. A documented W-10 mitigation plan may support improvement toward Sovereign, but does not itself satisfy Sovereign classification unless W-10 is deactivated under the protocol.

**What this means:** The avatar is defensible under adversarial scrutiny — by a regulator, a platform's trust-and-safety review, or a rights holder asserting a claim. This is the highest band the standard defines. Sovereign is not a permanent designation; governance infrastructure must be maintained to retain it.

**Stakeholder implications:**

- *Platform:* Sovereign deployments can be cited in regulatory compliance documentation and platform governance reports.
- *Legal and trust and safety:* Full documentation, revocation capability, anti-impersonation controls, and rights chain provide the basis for a formal legal defense.
- *Rights holder:* Maximum control and enforceability over the likeness.
- *Acquirer:* A platform whose product can produce Sovereign-band assessments holds a defensible governance standard — the highest-value position this asset creates. Sovereign-capable tooling is what a buyer acquires, not just the vocabulary.

---

## Band Determination Rules

1. Assess all weakness classes (W-01…W-10) using the Avatar Strength Assessment Protocol.
2. **Rule 2 is unconditional:** If W-01 is active, or W-02 is active, or W-03 is active → **Ungoverned**. No combination of other governance components compensates for an active Ungoverned-class weakness.
3. If no Ungoverned-class weakness is active, but any weakness class is active, or any of W-01, W-02, W-03, W-04, or W-09 is partial → **Provisional**.
4. If no weakness class is active, and residual partial weaknesses are limited to W-05, W-06, W-07, W-08, W-10 → **Governed**.
5. If every weakness class is fully deactivated — consent, provenance, disclosure, scope, attribution, revocation, anti-impersonation, and rights chain all documented, verifiable, and tamper-evident → **Sovereign**.

Band determination is total (v0.2): the rules above partition the entire weakness-state space, so every assessment resolves to exactly one band. The determination is machine-verified across all 59,049 protocol input combinations by `tests/test_protocol_determinism.py`.

---

## What the Standard Does Not Assess

- Rendering quality, realism, or aesthetic coherence
- Platform engagement, conversion, or user experience quality
- AI model capability or generation fidelity
- Brand alignment or creative direction
- Commercial success metrics

These are excluded by design. The standard's silence on realism is not an omission — it is the thesis.

---

## Versioning

The standard is versioned independently of the ontology. A band criterion may be refined when new observable failure modes are added to the ontology (new W-classes). Band criteria may not be relaxed to accommodate common practice; the standard defines what is defensible, not what is common.

*Standard maintained under Sovereign Asset System. Version history tracked in `DECISION_LOG.md`.*
