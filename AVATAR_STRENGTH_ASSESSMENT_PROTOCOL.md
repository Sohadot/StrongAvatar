# Avatar Strength Assessment Protocol

**Version:** 0.2
**Status:** Draft — version 0.2 authorized by DECISION_LOG.md entry dated 2026-07-14 (determinism closure)
**Governed by:** `AVATAR_INTEGRITY_ONTOLOGY.md`, `STRONG_AVATAR_STANDARD.md`
**Implemented by:** `spec/reference_implementation.py` (normative reference implementation)
**Machine-readable form:** `spec/avatar-strength-protocol.schema.json`
**Verification:** `tests/test_protocol_determinism.py` (exhaustive, all 59,049 input combinations)

---

## Purpose

This protocol defines the structured procedure for assessing a deployed avatar's strength band. It specifies what inputs are collected (the bounded questionnaire), how inputs map to weakness classes (the deterministic rule table), how weakness classes determine the strength band, and what the output contains.

The protocol is deterministic: two competent operators assessing the same deployment from the same inputs must reach the same band, the same dominant weakness class, and the same remediating components. Any input combination that does not resolve deterministically is a protocol defect, not an operator judgment call.

---

## Scope

The protocol assesses a single avatar deployment — one instance of a synthetic avatar or digital likeness in one deployment context. Multi-context or multi-avatar assessments require one protocol run per deployment context.

---

## Inputs — Bounded Questionnaire

All inputs are bounded-choice (single select). No free text is scored. Every question maps directly to one or more weakness classes.

### Section A — Consent

**A1. Consent Documentation**
Does a documented consent basis exist for the use of this likeness?

- `A1-Y` — Yes: a consent record exists, is dated, and specifies the authorized use scope
- `A1-P` — Partial: a consent record exists but lacks scope specification, dating, or other required elements
- `A1-N` — No: no consent documentation exists or is producible

*Maps to: W-01*

**A2. Consent Scope**
Does the consent basis specify the permitted use contexts, platforms, and duration?

- `A2-Y` — Yes: all three (contexts, platforms, duration) are specified
- `A2-P` — Partial: one or two of the three are specified
- `A2-N` — No: none are specified, or no consent basis exists

*Maps to: W-01, W-04, W-08*

**A3. Revocation Mechanism**
Is there a documented process for the subject or rights holder to withdraw consent and remove the avatar from deployment?

- `A3-Y` — Yes: a revocation procedure exists with a defined response time
- `A3-P` — Partial: a withdrawal process exists but response time is undefined or untested
- `A3-N` — No: no revocation mechanism exists

*Maps to: W-07*

---

### Section B — Provenance

**B1. Origin Documentation**
Is the origin of this avatar (capture, generation, or training source) documented and traceable?

- `B1-Y` — Yes: origin chain is documented and verifiable
- `B1-P` — Partial: origin is partially documented but cannot be fully verified
- `B1-N` — No: no origin documentation exists

*Maps to: W-02*

**B2. Content Credentials**
Are content credentials or provenance metadata attached to the avatar in a tamper-evident form?

- `B2-Y` — Yes: tamper-evident provenance signals persist through distribution
- `B2-P` — Partial: provenance metadata exists but is not tamper-evident or does not persist through distribution
- `B2-N` — No: no content credentials or provenance metadata exist

*Maps to: W-02, W-10*

---

### Section C — Disclosure

**C1. Synthetic Disclosure**
Is the synthetic nature of this avatar disclosed in contexts where a viewer would reasonably need to know?

- `C1-Y` — Yes: disclosure is present in all material deployment contexts
- `C1-P` — Partial: disclosure is present in some but not all material contexts
- `C1-N` — No: no disclosure exists in material deployment contexts

*Maps to: W-03*

---

### Section D — Scope and Attribution

**D1. Usage Scope Binding**
Are the avatar's authorized behaviors, roles, and statements documented and bounded?

- `D1-Y` — Yes: scope is fully documented and a review mechanism exists for out-of-scope use
- `D1-P` — Partial: some scope boundaries are documented but the full authorized scope is unclear
- `D1-N` — No: no scope binding exists

*Maps to: W-04, W-08*

**D2. Accountable Owner**
Is there a named, contactable accountable party bound to this avatar's governance and behavior?

- `D2-Y` — Yes: accountable owner is identified, contactable, and has accepted documented responsibility
- `D2-P` — Partial: an owner is identified but accountability binding is incomplete or undocumented
- `D2-N` — No: no accountable owner is identified

*Maps to: W-09*

---

### Section E — Rights and Anti-Impersonation

**E1. Rights Chain**
Is the chain of title for the likeness or identity clear, current, and complete?

- `E1-Y` — Yes: rights documentation covers all assignments and matches the deployment context
- `E1-P` — Partial: rights documentation exists but has gaps (expired, incomplete assignment, or contested)
- `E1-N` — No: no rights documentation exists or the chain is unclear

*Maps to: W-06*

**E2. Anti-Impersonation Controls**
Are there technical or procedural barriers that prevent this avatar from being cloned or repurposed for impersonation?

- `E2-Y` — Yes: authentication mechanism and replication barriers are in place
- `E2-P` — Partial: some barriers exist but do not cover all impersonation vectors
- `E2-N` — No: no anti-impersonation controls exist

*Maps to: W-05, W-10*

---

## Deterministic Rule Table

For each input, an `-N` response activates the corresponding weakness class as **active**. A `-P` response activates it as **partial**. A `-Y` response deactivates it.

Where multiple inputs map to the same weakness class, the class is active if any contributing input is `-N`, and partial if all contributing inputs are at minimum `-P` with none at `-N`.

| Input | `-N` activates | `-P` activates |
|---|---|---|
| A1 | W-01 (active) | W-01 (partial) |
| A2 | W-04 (per W-04 rule), W-08 (per W-08 rule) | W-04 (per W-04 rule), W-08 (per W-08 rule) |
| A3 | W-07 (active) | W-07 (partial) |
| B1 | W-02 (active) | W-02 (partial) |
| B2 | W-10 (per W-10 rule) | W-10 (per W-10 rule) |
| C1 | W-03 (active) | W-03 (partial) |
| D1 | W-04 (per W-04 rule), W-08 (per W-08 rule) | W-04 (per W-04 rule), W-08 (per W-08 rule) |
| D2 | W-09 (active) | W-09 (partial) |
| E1 | W-06 (active) | W-06 (partial) |
| E2 | W-05 (active), W-10 (per W-10 rule) | W-05 (partial), W-10 (per W-10 rule) |

For W-04, W-08, and W-10 — the classes fed by two inputs — the named activation rules below are the sole authority. (v0.2 correction: v0.1 table annotations for the D1/W-04 and E2/W-10 cells conflicted with the named rules; the named rules govern.)

**W-04 activation rule:** Active if either A2 or D1 is `-N`. Partial if at least one is `-P` and neither is `-N`. Inactive if both are `-Y`.

**W-08 activation rule:** Active if D1 is `-N`. Partial if D1 is `-P`, or if A2 is `-P` or `-N` while D1 is `-Y`. Inactive if both are `-Y`.

**W-10 activation rule:** Active if B2 is `-N`, or if E2 is `-N`. Partial if either is `-P` and neither is `-N`. Inactive if both are `-Y`.

---

## Band Determination

After applying the rule table, determine the strength band. Band determination is **total**: the four rules below partition the entire state space, so every input combination resolves to exactly one band. (v0.2 closure: v0.1 left combinations such as an active W-05/W-06/W-10 with no other trigger, or a partial W-04/W-09, without an assigned band. The closure assigns every previously undefined combination the more conservative band; no combination that resolved under v0.1 changes band.)

1. If W-01 is active **or** W-02 is active **or** W-03 is active → **Ungoverned** (unconditional)
2. Else if any weakness class is active, **or** any of W-01, W-02, W-03, W-04, W-09 is partial → **Provisional**
3. Else if any of W-05, W-06, W-07, W-08, W-10 is partial → **Governed**
4. Else (all weakness classes fully deactivated, which occurs only when all inputs are `-Y`) → **Sovereign**

Rule 1 is unconditional and evaluated first. Rules are evaluated in order; the first rule whose condition holds determines the band.

---

## Protocol Output

The protocol returns exactly:

1. **Strength Band** — Ungoverned / Provisional / Governed / Sovereign
2. **Dominant Weakness Class** — the highest-severity active class, using this priority order:
   W-01 > W-02 > W-03 > W-04 > W-07 > W-08 > W-09 > W-05 > W-06 > W-10
3. **All Active Weakness Classes** — the full list of active and partial W-classes
4. **Ranked Remediating Components** — C-components addressing active weaknesses, ordered by impact on band elevation
5. **Band elevation path** — the minimum set of C-components whose full implementation would raise the band by one level

The output does not include:
- A numeric score (deferred to Avatar Trust Score API, Phase 3)
- Subjective commentary on realism or aesthetic presentation
- Recommendations outside the C-01…C-08 set
- Any output element that does not link to a registered reference page

**Output link rule:** Every band links to the Strong Avatar Standard page. Every weakness class links to its W-class reference page. Every component links to its C-class reference page. An output element that points nowhere is a protocol violation.

---

## Reproducibility Guarantee

The mapping from any input combination to a band output is fully determined by this document. No operator discretion, model inference, or external data source enters the assessment. Given the same 10 input values, the protocol must produce the same band, dominant weakness class, and component list on every run. If it does not, the discrepancy is a defect in the protocol or its implementation, not an operator judgment call.

As of v0.2 this guarantee is machine-verified, not merely declared: `tests/test_protocol_determinism.py` enumerates all 59,049 possible input combinations against `spec/reference_implementation.py` and proves totality (every combination resolves to exactly one band), determinism (repeated runs are identical), the unconditional Ungoverned rule, the all-`-Y` Sovereign rule, elevation-path validity, and the output link rule. A protocol revision that fails exhaustive verification may not be versioned forward.

---

## Machine-Readable Specification

The protocol's interchange format is defined in `spec/avatar-strength-protocol.schema.json` (JSON Schema, draft 2020-12). Canonical input/output vectors are published in `spec/test_vectors.json`. An implementation conforms if and only if it matches the reference implementation across the full input space; the canonical vectors are necessary but not sufficient. See `spec/README.md`.

---

*Protocol maintained under Sovereign Asset System. Version history tracked in `DECISION_LOG.md`. Engine implementation must conform to this rule table exactly and without exception; `spec/reference_implementation.py` is the normative reference.*
