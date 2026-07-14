#!/usr/bin/env python3
"""Exhaustive determinism verification for the Avatar Strength Assessment
Protocol reference implementation.

The protocol's reproducibility guarantee is a falsifiable claim: every one
of the 59,049 possible input combinations (10 bounded inputs x 3 values)
must resolve to exactly one band with no fall-through, and repeated runs
must produce identical output. This suite enumerates the full input space
and verifies:

  1. Totality      — every combination yields a valid band (no undefined case)
  2. Determinism   — two independent runs agree on every combination
  3. Boundary law  — any of A1/B1/C1 = N forces Ungoverned, unconditionally
  4. Apex law      — all-Y is the only combination that yields Sovereign
  5. Elevation law — applying the band elevation path raises the band
  6. Link law      — every output element resolves to a registered route
  7. Vector law    — canonical test vectors in spec/test_vectors.json match

Run: python3 tests/test_protocol_determinism.py
"""

import itertools
import json
import os
import sys
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO_ROOT, "spec"))

import reference_implementation as engine  # noqa: E402

ALL_COMBINATIONS = [
    dict(zip(engine.INPUT_IDS, values))
    for values in itertools.product(engine.INPUT_VALUES, repeat=len(engine.INPUT_IDS))
]


class TestTotality(unittest.TestCase):
    def test_every_combination_resolves_to_exactly_one_band(self):
        for inputs in ALL_COMBINATIONS:
            result = engine.assess(inputs)
            self.assertIn(result["strength_band"], engine.BANDS, inputs)

    def test_no_combination_raises(self):
        for inputs in ALL_COMBINATIONS:
            engine.assess(inputs)  # any exception fails the test


class TestDeterminism(unittest.TestCase):
    def test_repeated_runs_are_identical(self):
        for inputs in ALL_COMBINATIONS:
            first = json.dumps(engine.assess(inputs), sort_keys=True)
            second = json.dumps(engine.assess(inputs), sort_keys=True)
            self.assertEqual(first, second, inputs)


class TestBoundaryLaws(unittest.TestCase):
    def test_ungoverned_is_unconditional(self):
        """A1, B1, or C1 = N (consent, provenance, or disclosure absent)
        forces Ungoverned regardless of every other input."""
        for inputs in ALL_COMBINATIONS:
            if "N" in (inputs["A1"], inputs["B1"], inputs["C1"]):
                self.assertEqual(
                    engine.assess(inputs)["strength_band"], "Ungoverned", inputs
                )

    def test_sovereign_only_from_all_yes(self):
        for inputs in ALL_COMBINATIONS:
            band = engine.assess(inputs)["strength_band"]
            if all(v == "Y" for v in inputs.values()):
                self.assertEqual(band, "Sovereign", inputs)
            else:
                self.assertNotEqual(band, "Sovereign", inputs)

    def test_dominant_class_present_unless_all_inactive(self):
        for inputs in ALL_COMBINATIONS:
            result = engine.assess(inputs)
            has_weakness = bool(
                result["active_weakness_classes"]
                or result["partial_weakness_classes"]
            )
            self.assertEqual(
                result["dominant_weakness_class"] is not None,
                has_weakness,
                inputs,
            )


class TestElevationLaw(unittest.TestCase):
    def test_elevation_path_raises_band(self):
        for inputs in ALL_COMBINATIONS:
            states = engine.derive_weakness_states(inputs)
            band = engine.determine_band(states)
            path = engine.band_elevation_path(states)
            if band == "Sovereign":
                self.assertEqual(path, [], inputs)
                continue
            self.assertTrue(path, inputs)
            simulated = dict(states)
            for component in path:
                for w in engine.COMPONENT_DEACTIVATES[component]:
                    simulated[w] = "inactive"
            self.assertGreater(
                engine.BANDS.index(engine.determine_band(simulated)),
                engine.BANDS.index(band),
                inputs,
            )


class TestLinkLaw(unittest.TestCase):
    """Protocol output link rule: an output element that points nowhere is
    a protocol violation. Every referenced route must be in the registered
    launch set."""

    @classmethod
    def setUpClass(cls):
        launch_set_path = os.path.join(REPO_ROOT, "site", "data", "launch_set.json")
        with open(launch_set_path, "r", encoding="utf-8") as handle:
            cls.registered_routes = set(json.load(handle)["allowed_routes"])

    def test_all_output_references_are_registered_routes(self):
        for inputs in ALL_COMBINATIONS:
            refs = engine.assess(inputs)["references"]
            self.assertIn(refs["strength_band"], self.registered_routes)
            for route in refs["weakness_classes"].values():
                self.assertIn(route, self.registered_routes)
            for route in refs["components"].values():
                self.assertIn(route, self.registered_routes)


class TestCanonicalVectors(unittest.TestCase):
    def test_vectors_match(self):
        vectors_path = os.path.join(REPO_ROOT, "spec", "test_vectors.json")
        with open(vectors_path, "r", encoding="utf-8") as handle:
            document = json.load(handle)
        self.assertEqual(document["protocol_version"], engine.PROTOCOL_VERSION)
        self.assertGreaterEqual(len(document["vectors"]), 8)
        for vector in document["vectors"]:
            result = engine.assess(vector["input"])
            self.assertEqual(
                result,
                vector["expected_output"],
                "vector %r diverged" % vector["id"],
            )


class TestInputValidation(unittest.TestCase):
    def test_rejects_missing_unknown_and_invalid(self):
        with self.assertRaises(ValueError):
            engine.assess({})
        with self.assertRaises(ValueError):
            engine.assess({**ALL_COMBINATIONS[0], "Z9": "Y"})
        bad = dict(ALL_COMBINATIONS[0])
        bad["A1"] = "MAYBE"
        with self.assertRaises(ValueError):
            engine.assess(bad)


if __name__ == "__main__":
    unittest.main(verbosity=2)
