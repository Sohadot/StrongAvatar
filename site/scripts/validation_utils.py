from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Iterable


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_json(relative_path: str) -> Any:
    path = repo_root() / relative_path
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        fail(f"Missing JSON file: {relative_path}")
    except json.JSONDecodeError as exc:
        fail(f"Invalid JSON in {relative_path}: {exc}")


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def pass_message(message: str) -> None:
    print(f"PASS: {message}")


def ensure_keys(obj: dict[str, Any], required_keys: Iterable[str], context: str) -> list[str]:
    return [f"{context} missing required key: {key}" for key in required_keys if key not in obj]


def list_non_gitkeep_files(path: str | Path) -> list[Path]:
    root = Path(path)
    if not root.is_absolute():
        root = repo_root() / root
    if not root.exists():
        return []
    return sorted(file for file in root.rglob("*") if file.is_file() and file.name != ".gitkeep")


def is_gitkeep_only_directory(path: str | Path) -> bool:
    return len(list_non_gitkeep_files(path)) == 0


def load_site_data() -> dict[str, Any]:
    data_dir = repo_root() / "site" / "data"
    data: dict[str, Any] = {}
    for path in sorted(data_dir.glob("*.json")):
        data[path.name] = load_json(str(path.relative_to(repo_root())))
    return data


def load_pages() -> list[dict[str, Any]]:
    pages_data = load_json("site/data/pages.json")
    pages = pages_data.get("pages")
    if not isinstance(pages, list):
        fail("site/data/pages.json must contain a pages array")
    return pages


def assert_all_site_data_json_valid() -> None:
    load_site_data()
