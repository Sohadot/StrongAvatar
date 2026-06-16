---
route: /protocol/
title: Avatar Strength Assessment Protocol — Deterministic Governance Assessment
meta_description: The Avatar Strength Assessment Protocol defines the bounded questionnaire, deterministic rule table, and output specification for assessing the governance strength band of any deployed synthetic avatar.
canonical: https://strongavatar.com/protocol/
seo_cluster: avatar governance protocol, synthetic avatar assessment, digital identity audit
template: protocol_page
publication_state: reserved, non-public, non-indexable
source_requirement: internal doctrine; technical and regulatory claims require external sources before publication
last_reviewed: 2026-06-16
ontology_ref: protocol
---

# Avatar Strength Assessment Protocol

The Avatar Strength Assessment Protocol defines the structured procedure for assessing a deployed avatar's governance strength band. It specifies what inputs are collected, how inputs map to weakness classes, how weakness classes determine the strength band, and what the output contains.

The protocol is deterministic. Given the same ten input values, two competent operators must reach the same band, the same dominant weakness class, and the same remediating components. Any deviation is a protocol defect, not an operator judgment call.

---

## What the Protocol Assesses

The protocol assesses a single avatar deployment — one instance of a synthetic avatar or digital likeness in one deployment context. A multi-context deployment requires one protocol run per context.

The protocol does not assess realism, aesthetic quality, engagement metrics, or commercial performance. It assesses only governance integrity: whether the identity, consent, provenance, disclosure, scope, revocability, and accountability of the deployment are documented and verifiable.

---

## Input Structure

The protocol collects ten bounded-choice inputs across five sections. Every input is single-select with three possible answers: Y (fully satisfied), P (partially satisfied), or N (not satisfied). No free text is scored.

### Section A — Consent
**A1** — Does a documented consent basis exist?
**A2** — Does the consent basis specify permitted contexts, platforms, and duration?
**A3** — Is there a documented revocation mechanism?

### Section B — Provenance
**B1** — Is the origin of the avatar documented and traceable?
**B2** — Are content credentials or provenance metadata attached in tamper-evident form?

### Section C — Disclosure
**C1** — Is synthetic disclosure present in all material deployment contexts?

### Section D — Scope and Attribution
**D1** — Are the avatar's authorized behaviors, roles, and statements bounded?
**D2** — Is there a named, contactable accountable party bound to this deployment?

### Section E — Rights and Anti-Impersonation
**E1** — Is the chain of title for the likeness complete, current, and clear?
**E2** — Are technical or procedural barriers in place against cloning or impersonation?

---

## Weakness Class Activation

Each input maps to one or more weakness classes from the [Avatar Integrity Ontology](/ontology/). An `-N` answer activates the corresponding class as active. A `-P` answer activates it as partial. A `-Y` answer deactivates it.

Where multiple inputs map to the same class, the class is active if any contributing input is `-N`, and partial if all are at minimum `-P` with none at `-N`.

Key multi-input rules:
- **[W-04 Identity Drift](/weakness/identity-drift/):** active if A2 or D1 is `-N`; partial if both are `-P`, or one is `-P` and the other is `-Y`
- **[W-08 Context Collapse](/weakness/context-collapse/):** active if D1 is `-N`; partial if A2 is `-P` or `-N` while D1 is `-P`
- **[W-10 Robustness Weakness](/weakness/robustness-weakness/):** active if B2 or E2 is `-N`; partial if either is `-P` with the other at `-Y` or `-P`

---

## Band Determination

After applying the rule table:

1. If [W-01](/weakness/consent-absence/), [W-02](/weakness/provenance-void/), or [W-03](/weakness/disclosure-failure/) is active → **Ungoverned** (unconditional)
2. Else if any of [W-04](/weakness/identity-drift/), [W-07](/weakness/revocation-gap/), [W-08](/weakness/context-collapse/), [W-09](/weakness/attribution-loss/) is active → **Provisional**
3. Else if W-05, W-06, W-07, W-08, W-10 are partial but W-01–W-04, W-09 are deactivated → **Governed**
4. If all inputs are `-Y` → **Sovereign**

Rule 1 is evaluated before all others. See the [Strong Avatar Standard](/standard/) for full band criteria and stakeholder implications.

---

## Protocol Output

The protocol returns exactly:

1. **Strength Band** — Ungoverned, Provisional, Governed, or Sovereign
2. **Dominant Weakness Class** — the highest-severity active class, using priority order W-01 > W-02 > W-03 > W-04 > W-07 > W-08 > W-09 > W-05 > W-06 > W-10
3. **All Active Weakness Classes** — full list of active and partial W-classes
4. **Ranked Remediating Components** — C-components addressing active weaknesses, ordered by impact on band elevation
5. **Band Elevation Path** — the minimum set of C-components whose full implementation would raise the band by one level

The output does not include a numeric score (that is the Avatar Trust Score API, Phase 3), subjective commentary on realism, or recommendations outside the C-01…C-08 set.

**Output link rule:** Every band links to the Strong Avatar Standard. Every weakness class in the output links to its reference page. Every component links to its reference page. An output element that points nowhere is a protocol violation.

---

## Reproducibility

The mapping from any input combination to a band output is fully determined by this document. No operator discretion, model inference, or external data source enters the assessment. An implementation that produces different results for the same inputs is defective.

---

## Return

[StrongAvatar.com](/)

---

## Source Note

This protocol is internal doctrine under the Sovereign Asset System, governed by the [Avatar Integrity Ontology](/ontology/) and the [Strong Avatar Standard](/standard/). Technical and regulatory claims require external source documentation before publication. Protocol inputs map to weakness classes as documented in the Avatar Integrity Ontology; any deviation requires a DECISION_LOG entry.
