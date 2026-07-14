#!/usr/bin/env python3
"""Validate HydraSafe manifests, schemas, and example artifacts.

This validator enforces both JSON Schema validity and HydraSafe-specific safety
invariants that must remain true even when schemas evolve.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError as exc:  # pragma: no cover - dependency failure is explicit
    raise SystemExit(
        "jsonschema is required. Install with: python -m pip install jsonschema"
    ) from exc

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_SCHEMA = ROOT / "schemas" / "hydrasafe-artifact.schema.json"
EVENT_SCHEMA = ROOT / "schemas" / "hydrasafe-event.schema.json"
MANIFEST = ROOT / "hydrasafe.manifest.json"
EXAMPLE_ARTIFACTS = ROOT / "examples" / "artifacts"
EXAMPLE_EVENTS = ROOT / "examples" / "events"
HANDOFF = ROOT / "docs" / "HYDRASAFE_MIRROR_HANDOFF.md"
CANONICAL_EVIDENCE = ROOT / "docs" / "EVIDENCE_PACK.md"

DENIED_AUTHORITY_FIELDS = (
    "physical_control",
    "permit_issuance",
    "engineering_approval",
)


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError(f"missing required file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"invalid JSON in {path.relative_to(ROOT)}: line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc


def schema_errors(instance: Any, schema: dict[str, Any]) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors: list[str] = []
    for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in error.path) or "<root>"
        errors.append(f"{location}: {error.message}")
    return errors


def validate_manifest(manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    product = manifest.get("product", {})
    authority = manifest.get("authority", {})

    if product.get("parent_ecosystem") != "DiamondOps":
        errors.append("manifest product.parent_ecosystem must be DiamondOps")
    if product.get("canonical_dependency") != "StegVerse-Labs/DiamondOps-Core":
        errors.append("manifest canonical_dependency must remain StegVerse-Labs/DiamondOps-Core")
    if product.get("posture") != "documentation-only":
        errors.append("manifest product.posture must remain documentation-only")

    for field in DENIED_AUTHORITY_FIELDS:
        if authority.get(field) is not False:
            errors.append(f"manifest authority.{field} must be false")

    if manifest.get("handoff") != "docs/HYDRASAFE_MIRROR_HANDOFF.md":
        errors.append("manifest handoff must identify docs/HYDRASAFE_MIRROR_HANDOFF.md")
    return errors


def validate_artifact_semantics(artifact: dict[str, Any], path: Path) -> list[str]:
    errors: list[str] = []
    label = path.relative_to(ROOT)
    boundary = artifact.get("authority_boundary")

    if boundary is None:
        errors.append(f"{label}: authority_boundary is required by repository policy")
    else:
        for field in DENIED_AUTHORITY_FIELDS:
            if boundary.get(field) is not False:
                errors.append(f"{label}: authority_boundary.{field} must be false")

    canonical_refs = artifact.get("canonical_references", [])
    if not any(
        ref.get("reference_type") == "diamondops-canonical"
        and "DiamondOps-Core" in ref.get("identifier", "")
        for ref in canonical_refs
        if isinstance(ref, dict)
    ):
        errors.append(f"{label}: at least one DiamondOps-Core canonical reference is required")

    scope = artifact.get("scope", {})
    if scope.get("sensitive_data_embedded") is not False:
        errors.append(f"{label}: scope.sensitive_data_embedded must be false")

    if artifact.get("status") == "complete":
        review_state = artifact.get("review_posture", {}).get("state")
        if review_state not in {"externally-reviewed", "superseded"}:
            errors.append(f"{label}: complete artifacts require external review or supersession")

    return errors


def collect_examples(directory: Path) -> list[Path]:
    if not directory.exists():
        return []
    return sorted(directory.glob("*.json"))


def main() -> int:
    failures: list[str] = []

    for required in (HANDOFF, CANONICAL_EVIDENCE):
        if not required.is_file():
            failures.append(f"missing required file: {required.relative_to(ROOT)}")

    try:
        manifest = load_json(MANIFEST)
        artifact_schema = load_json(ARTIFACT_SCHEMA)
        event_schema = load_json(EVENT_SCHEMA)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 1

    failures.extend(validate_manifest(manifest))

    artifact_examples = collect_examples(EXAMPLE_ARTIFACTS)
    if not artifact_examples:
        failures.append("at least one artifact example is required")

    for path in artifact_examples:
        try:
            artifact = load_json(path)
        except ValueError as exc:
            failures.append(str(exc))
            continue
        for error in schema_errors(artifact, artifact_schema):
            failures.append(f"{path.relative_to(ROOT)}: {error}")
        failures.extend(validate_artifact_semantics(artifact, path))

    for path in collect_examples(EXAMPLE_EVENTS):
        try:
            event = load_json(path)
        except ValueError as exc:
            failures.append(str(exc))
            continue
        for error in schema_errors(event, event_schema):
            failures.append(f"{path.relative_to(ROOT)}: {error}")

    if failures:
        print("HydraSafe validation FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        "HydraSafe validation PASSED: "
        f"{len(artifact_examples)} artifact example(s), "
        f"{len(collect_examples(EXAMPLE_EVENTS))} event example(s)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
