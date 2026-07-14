# Machine-Readable Specification Layer

This directory is the executable proof layer for the Avatar Strength Assessment Protocol. The doctrine documents state that the protocol is deterministic; this layer makes that claim falsifiable and continuously verified instead of merely asserted.

## Contents

| File | Role |
|---|---|
| `avatar-strength-protocol.schema.json` | JSON Schema (draft 2020-12) interchange format for assessment inputs and outputs. The contract any conforming implementation must satisfy. |
| `reference_implementation.py` | Normative executable expression of the protocol rule table and band determination. Zero dependencies, standard library only. |
| `test_vectors.json` | Canonical input/output vectors generated from and verified against the reference implementation. |

Verification lives in `tests/test_protocol_determinism.py`, which enumerates all 59,049 possible input combinations (10 bounded inputs × 3 values) and proves totality, determinism, the unconditional Ungoverned rule, the all-Y Sovereign rule, elevation-path validity, and the output link rule.

## Conformance

An implementation conforms to the protocol if and only if, for every valid `assessment_input`, it produces the same `strength_band`, `dominant_weakness_class`, `active_weakness_classes`, `partial_weakness_classes`, `ranked_remediating_components`, and `band_elevation_path` as `reference_implementation.py`. The canonical vectors in `test_vectors.json` are necessary but not sufficient for conformance; the full input space is the standard.

## Governance

- Normative text: `AVATAR_STRENGTH_ASSESSMENT_PROTOCOL.md`, `STRONG_AVATAR_STANDARD.md`, `AVATAR_INTEGRITY_ONTOLOGY.md`.
- Any divergence between this layer and the normative text is a defect and must be recorded in `DECISION_LOG.md` before either artifact is versioned forward.
- Version changes to the schema, reference implementation, or vectors require a `DECISION_LOG.md` entry, matching the versioning rules that govern the protocol documents.
- Public deployment of any assessment engine remains gated by `site/data/launch_set.json` (`diagnostic_engine_enabled: false`). Nothing in this directory is copied into `output/`.
