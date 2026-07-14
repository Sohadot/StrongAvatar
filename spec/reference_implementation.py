#!/usr/bin/env python3
"""Avatar Strength Assessment Protocol — Reference Implementation.

This module is the normative executable expression of
AVATAR_STRENGTH_ASSESSMENT_PROTOCOL.md (v0.2). It exists to prove, not
merely assert, the protocol's determinism guarantee: every one of the
59,049 possible input combinations (10 bounded inputs x 3 values) resolves
to exactly one strength band, one dominant weakness class, and one
remediation set, with no operator discretion, model inference, or external
data source.

Any divergence between this implementation and the protocol document is a
defect that must be recorded in DECISION_LOG.md and resolved before either
artifact is versioned forward.

Deployment note: launch_set.json keeps `diagnostic_engine_enabled: false`.
This file is a repository-internal reference artifact. It is not a public
page, is never copied into output/, and its public deployment requires a
separate DECISION_LOG.md authorization.

Usage:
    python3 spec/reference_implementation.py '{"A1":"Y","A2":"Y","A3":"Y","B1":"Y","B2":"Y","C1":"Y","D1":"Y","D2":"Y","E1":"Y","E2":"Y"}'
    python3 spec/reference_implementation.py path/to/input.json
"""

import json
import sys

PROTOCOL_VERSION = "0.2.0"

INPUT_IDS = ("A1", "A2", "A3", "B1", "B2", "C1", "D1", "D2", "E1", "E2")
INPUT_VALUES = ("Y", "P", "N")

WEAKNESS_CLASSES = (
    "W-01", "W-02", "W-03", "W-04", "W-05",
    "W-06", "W-07", "W-08", "W-09", "W-10",
)

BANDS = ("Ungoverned", "Provisional", "Governed", "Sovereign")

# Protocol output section: dominant-class severity priority order.
SEVERITY_PRIORITY = (
    "W-01", "W-02", "W-03", "W-04", "W-07",
    "W-08", "W-09", "W-05", "W-06", "W-10",
)

# Single-input weakness classes: N -> active, P -> partial, Y -> inactive.
SINGLE_INPUT_CLASS = {
    "W-01": "A1",
    "W-02": "B1",
    "W-03": "C1",
    "W-05": "E2",
    "W-06": "E1",
    "W-07": "A3",
    "W-09": "D2",
}

# Primary remediation mapping (AVATAR_INTEGRITY_ONTOLOGY.md mapping table).
PRIMARY_REMEDIATION = {
    "W-01": "C-01",
    "W-02": "C-02",
    "W-03": "C-03",
    "W-04": "C-04",
    "W-05": "C-05",
    "W-06": "C-06",
    "W-07": "C-07",
    "W-08": "C-04",
    "W-09": "C-08",
    "W-10": "C-02",
}

COMPONENT_IDS = ("C-01", "C-02", "C-03", "C-04", "C-05", "C-06", "C-07", "C-08")

# Inverse of PRIMARY_REMEDIATION: classes fully deactivated when a
# component is fully implemented (used for band elevation search).
COMPONENT_DEACTIVATES = {}
for _w, _c in PRIMARY_REMEDIATION.items():
    COMPONENT_DEACTIVATES.setdefault(_c, []).append(_w)

# Registered reference routes (site/data/launch_set.json). The protocol's
# output link rule: an output element that points nowhere is a violation.
STANDARD_ROUTE = "/standard/"
WEAKNESS_ROUTES = {
    "W-01": "/weakness/consent-absence/",
    "W-02": "/weakness/provenance-void/",
    "W-03": "/weakness/disclosure-failure/",
    "W-04": "/weakness/identity-drift/",
    "W-05": "/weakness/impersonation-exposure/",
    "W-06": "/weakness/rights-ambiguity/",
    "W-07": "/weakness/revocation-gap/",
    "W-08": "/weakness/context-collapse/",
    "W-09": "/weakness/attribution-loss/",
    "W-10": "/weakness/robustness-weakness/",
}
COMPONENT_ROUTES = {
    "C-01": "/component/consent-infrastructure/",
    "C-02": "/component/provenance-credentials/",
    "C-03": "/component/disclosure-layer/",
    "C-04": "/component/scope-usage-binding/",
    "C-05": "/component/anti-impersonation-controls/",
    "C-06": "/component/rights-chain-documentation/",
    "C-07": "/component/revocation-mechanism/",
    "C-08": "/component/attribution-binding/",
}


def validate_input(inputs):
    """Reject anything that is not exactly the 10 bounded inputs."""
    if not isinstance(inputs, dict):
        raise ValueError("input must be a JSON object")
    unknown = sorted(set(inputs) - set(INPUT_IDS))
    if unknown:
        raise ValueError("unknown input identifiers: %s" % ", ".join(unknown))
    missing = sorted(set(INPUT_IDS) - set(inputs))
    if missing:
        raise ValueError("missing input identifiers: %s" % ", ".join(missing))
    for key in INPUT_IDS:
        if inputs[key] not in INPUT_VALUES:
            raise ValueError(
                "input %s has value %r; must be one of Y, P, N"
                % (key, inputs[key])
            )


def derive_weakness_states(inputs):
    """Apply the deterministic rule table. Returns {class: state} where
    state is one of 'active', 'partial', 'inactive'."""
    states = {}

    for w_class, input_id in SINGLE_INPUT_CLASS.items():
        value = inputs[input_id]
        states[w_class] = {"N": "active", "P": "partial", "Y": "inactive"}[value]

    # W-04 activation rule: active if either A2 or D1 is N; partial if at
    # least one is P and neither is N; inactive if both are Y.
    a2, d1 = inputs["A2"], inputs["D1"]
    if "N" in (a2, d1):
        states["W-04"] = "active"
    elif "P" in (a2, d1):
        states["W-04"] = "partial"
    else:
        states["W-04"] = "inactive"

    # W-08 activation rule: active if D1 is N; partial if D1 is P, or if
    # A2 is P or N while D1 is Y; inactive if both are Y.
    if d1 == "N":
        states["W-08"] = "active"
    elif d1 == "P" or a2 in ("P", "N"):
        states["W-08"] = "partial"
    else:
        states["W-08"] = "inactive"

    # W-10 activation rule: active if B2 or E2 is N; partial if either is
    # P and neither is N; inactive if both are Y.
    b2, e2 = inputs["B2"], inputs["E2"]
    if "N" in (b2, e2):
        states["W-10"] = "active"
    elif "P" in (b2, e2):
        states["W-10"] = "partial"
    else:
        states["W-10"] = "inactive"

    return states


def determine_band(states):
    """Total band determination (protocol v0.2). Every state combination
    resolves to exactly one band; falling through is impossible."""
    ungoverned_classes = ("W-01", "W-02", "W-03")

    if any(states[w] == "active" for w in ungoverned_classes):
        return "Ungoverned"

    provisional_triggers = (
        any(states[w] == "active" for w in WEAKNESS_CLASSES)
        or any(states[w] == "partial" for w in ungoverned_classes)
        or states["W-04"] == "partial"
        or states["W-09"] == "partial"
    )
    if provisional_triggers:
        return "Provisional"

    if any(states[w] == "partial" for w in WEAKNESS_CLASSES):
        return "Governed"

    return "Sovereign"


def dominant_weakness(states):
    """Highest-severity active class; if none is active, highest-severity
    partial class; None when all classes are inactive."""
    for w in SEVERITY_PRIORITY:
        if states[w] == "active":
            return w
    for w in SEVERITY_PRIORITY:
        if states[w] == "partial":
            return w
    return None


def ranked_remediating_components(states):
    """Primary components for active classes first (severity order), then
    components for partial classes, deduplicated preserving order."""
    ranked = []
    for phase in ("active", "partial"):
        for w in SEVERITY_PRIORITY:
            if states[w] == phase:
                component = PRIMARY_REMEDIATION[w]
                if component not in ranked:
                    ranked.append(component)
    return ranked


def band_elevation_path(states):
    """Minimum set of components whose full implementation raises the band
    by at least one level. Full implementation of a component sets its
    primarily remediated classes to inactive. Deterministic tie-break:
    smallest set size, then lexicographic component order. Empty for
    Sovereign (no higher band exists)."""
    current_band = determine_band(states)
    current_rank = BANDS.index(current_band)
    if current_band == "Sovereign":
        return []

    candidate_sets = []
    for mask in range(1, 2 ** len(COMPONENT_IDS)):
        subset = [
            COMPONENT_IDS[i]
            for i in range(len(COMPONENT_IDS))
            if mask & (1 << i)
        ]
        candidate_sets.append(subset)
    candidate_sets.sort(key=lambda s: (len(s), s))

    for subset in candidate_sets:
        simulated = dict(states)
        for component in subset:
            for w in COMPONENT_DEACTIVATES[component]:
                simulated[w] = "inactive"
        if BANDS.index(determine_band(simulated)) > current_rank:
            return subset

    # Unreachable: implementing all eight components deactivates every
    # class, which is Sovereign.
    raise AssertionError("no elevation path found; protocol defect")


def assess(inputs):
    """Run one full protocol assessment. Returns the protocol output as a
    plain dict conforming to spec/avatar-strength-protocol.schema.json."""
    validate_input(inputs)
    states = derive_weakness_states(inputs)
    band = determine_band(states)
    dominant = dominant_weakness(states)
    components = ranked_remediating_components(states)
    elevation = band_elevation_path(states)

    return {
        "protocol_version": PROTOCOL_VERSION,
        "strength_band": band,
        "dominant_weakness_class": dominant,
        "active_weakness_classes": [
            w for w in WEAKNESS_CLASSES if states[w] == "active"
        ],
        "partial_weakness_classes": [
            w for w in WEAKNESS_CLASSES if states[w] == "partial"
        ],
        "ranked_remediating_components": components,
        "band_elevation_path": elevation,
        "references": {
            "strength_band": STANDARD_ROUTE,
            "weakness_classes": {
                w: WEAKNESS_ROUTES[w]
                for w in WEAKNESS_CLASSES
                if states[w] != "inactive"
            },
            "components": {
                c: COMPONENT_ROUTES[c]
                for c in sorted(set(components) | set(elevation))
            },
        },
    }


def main(argv):
    if len(argv) != 2:
        sys.stderr.write(__doc__ + "\n")
        return 2
    raw = argv[1]
    try:
        if raw.strip().startswith("{"):
            inputs = json.loads(raw)
        else:
            with open(raw, "r", encoding="utf-8") as handle:
                inputs = json.load(handle)
        result = assess(inputs)
    except (ValueError, OSError) as exc:
        sys.stderr.write("error: %s\n" % exc)
        return 1
    json.dump(result, sys.stdout, indent=2, sort_keys=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
