from __future__ import annotations

import subprocess
import sys
from pathlib import Path


VALIDATORS = [
    "validate_content.py",
    "validate_content_contracts.py",
    "validate_template_contracts.py",
    "validate_design_tokens.py",
    "validate_links.py",
    "validate_seo.py",
    "validate_sources.py",
    "validate_claim_discipline.py",
    "validate_monetization.py",
    "validate_buyer_logic.py",
    "validate_no_thin_pages.py",
    "validate_no_dead_routes.py",
    "validate_page_source_integrity.py",
    "validate_output_integrity.py",
]


def main() -> None:
    script_dir = Path(__file__).resolve().parent
    failures: list[str] = []

    print("StrongAvatar.com sovereign quality gate")
    print("Running validators in deterministic order.")

    for validator in VALIDATORS:
        validator_path = script_dir / validator
        print(f"\n[{validator}]")
        result = subprocess.run([sys.executable, str(validator_path)], cwd=script_dir.parent.parent)
        if result.returncode != 0:
            failures.append(validator)

    print("\nQuality gate summary")
    if failures:
        print("FAIL: " + ", ".join(failures))
        sys.exit(1)

    print("PASS: all validators passed")
    sys.exit(0)


if __name__ == "__main__":
    main()
