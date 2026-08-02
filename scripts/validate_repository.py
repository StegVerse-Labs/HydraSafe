#!/usr/bin/env python3
"""Validate HydraSafe contracts, examples, security policy, and task state."""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError as exc:
    raise SystemExit("jsonschema is required. Install with: python -m pip install jsonschema") from exc

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_SCHEMA = ROOT / "schemas" / "hydrasafe-artifact.schema.json"
EVENT_SCHEMA = ROOT / "schemas" / "hydrasafe-event.schema.json"
MANIFEST = ROOT / "hydrasafe.manifest.json"
SECURITY_BASELINE = ROOT / "security" / "HYDRASAFE_SECURITY_BASELINE.md"
CONTROL_PROFILE = ROOT / "security" / "control-profile.json"
TASK_REGISTRY = ROOT / "ops" / "task-registry.json"
EXAMPLE_ARTIFACTS = ROOT / "examples" / "artifacts"
EXAMPLE_EVENTS = ROOT / "examples" / "events"
HANDOFF = ROOT / "docs" / "HYDRASAFE_MIRROR_HANDOFF.md"
CANONICAL_EVIDENCE = ROOT / "docs" / "EVIDENCE_PACK.md"

DENIED_AUTHORITY_FIELDS = ("physical_control", "permit_issuance", "engineering_approval")
REQUIRED_BASELINES = {
    "NIST-SP-800-53-Rev5",
    "NIST-SP-800-82-Rev3",
    "NIST-SP-800-171-Rev3-when-applicable",
    "FIPS-140-3-when-required",
    "CISA-Secure-by-Design",
    "CISA-Cross-Sector-CPGs",
}
ALLOWED_TASK_STATES = {
    "COMPLETE", "BLOCKED", "RETRY", "REVIEW_REQUIRED", "FAILED",
    "CLAIMED", "SUPERSEDED", "MERGED", "UNCLAIMED",
}


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError(f"missing required file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path.relative_to(ROOT)}: line {exc.lineno}, column {exc.colno}: {exc.msg}") from exc


def schema_errors(instance: Any, schema: dict[str, Any]) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [f"{'.'.join(str(p) for p in e.path) or '<root>'}: {e.message}" for e in sorted(validator.iter_errors(instance), key=lambda i: list(i.path))]


def validate_manifest(manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    product = manifest.get("product", {})
    authority = manifest.get("authority", {})
    if product.get("parent_ecosystem") != "DiamondOps": errors.append("manifest product.parent_ecosystem must be DiamondOps")
    if product.get("canonical_dependency") != "StegVerse-Labs/DiamondOps-Core": errors.append("manifest canonical_dependency must remain StegVerse-Labs/DiamondOps-Core")
    if product.get("posture") != "documentation-only": errors.append("manifest product.posture must remain documentation-only")
    for field in DENIED_AUTHORITY_FIELDS:
        if authority.get(field) is not False: errors.append(f"manifest authority.{field} must be false")
    if manifest.get("handoff") != "docs/HYDRASAFE_MIRROR_HANDOFF.md": errors.append("manifest handoff must identify docs/HYDRASAFE_MIRROR_HANDOFF.md")
    return errors


def validate_security(profile: dict[str, Any], baseline_text: str) -> list[str]:
    errors: list[str] = []
    if profile.get("status") != "required": errors.append("security profile status must be required")
    if profile.get("owner_repository") != "StegVerse-Labs/HydraSafe": errors.append("security profile owner must be StegVerse-Labs/HydraSafe")
    if not profile.get("release_gate", {}).get("fail_closed"): errors.append("security release gate must fail closed")
    missing = REQUIRED_BASELINES - set(profile.get("reference_baselines", []))
    if missing: errors.append(f"security profile missing reference baselines: {sorted(missing)}")
    claims = profile.get("certification_claims", {})
    if any(value is not False for value in claims.values()): errors.append("security profile must not assert certification or authorization")
    for phrase in ("minimum acceptable floor", "Fail-closed intake", "OT and safety separation", "Missing provenance blocks release"):
        if phrase not in baseline_text: errors.append(f"security baseline missing required policy phrase: {phrase}")
    return errors


def validate_task_registry(registry: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    ids: set[str] = set()
    for task in registry.get("tasks", []):
        task_id = task.get("task_id")
        if not task_id or task_id in ids: errors.append(f"invalid or duplicate task_id: {task_id}")
        ids.add(task_id)
        state = task.get("claim_state")
        if state not in ALLOWED_TASK_STATES: errors.append(f"{task_id}: unsupported claim_state {state}")
        if not task.get("owner") or not task.get("release_condition") or not task.get("expected_evidence"):
            errors.append(f"{task_id}: owner, release_condition, and expected_evidence are required")
        if state == "CLAIMED":
            expires = task.get("claim_expires_at")
            if task_id != "HYDRA-COMMERCIAL-001" and not expires:
                errors.append(f"{task_id}: claimed task requires claim_expires_at")
            if expires:
                try: datetime.fromisoformat(expires)
                except ValueError: errors.append(f"{task_id}: invalid claim_expires_at")
    return errors


def validate_artifact_semantics(artifact: dict[str, Any], path: Path) -> list[str]:
    errors: list[str] = []
    label = path.relative_to(ROOT)
    boundary = artifact.get("authority_boundary")
    if boundary is None: errors.append(f"{label}: authority_boundary is required")
    else:
        for field in DENIED_AUTHORITY_FIELDS:
            if boundary.get(field) is not False: errors.append(f"{label}: authority_boundary.{field} must be false")
    refs = artifact.get("canonical_references", [])
    if not any(isinstance(ref, dict) and ref.get("reference_type") == "diamondops-canonical" and "DiamondOps-Core" in ref.get("identifier", "") for ref in refs):
        errors.append(f"{label}: at least one DiamondOps-Core canonical reference is required")
    if artifact.get("scope", {}).get("sensitive_data_embedded") is not False: errors.append(f"{label}: scope.sensitive_data_embedded must be false")
    if artifact.get("status") == "complete" and artifact.get("review_posture", {}).get("state") not in {"externally-reviewed", "superseded"}:
        errors.append(f"{label}: complete artifacts require external review or supersession")
    return errors


def examples(directory: Path) -> list[Path]:
    return sorted(directory.glob("*.json")) if directory.exists() else []


def main() -> int:
    failures: list[str] = []
    for required in (HANDOFF, CANONICAL_EVIDENCE, SECURITY_BASELINE, CONTROL_PROFILE, TASK_REGISTRY):
        if not required.is_file(): failures.append(f"missing required file: {required.relative_to(ROOT)}")
    try:
        manifest = load_json(MANIFEST)
        artifact_schema = load_json(ARTIFACT_SCHEMA)
        event_schema = load_json(EVENT_SCHEMA)
        profile = load_json(CONTROL_PROFILE)
        registry = load_json(TASK_REGISTRY)
        baseline_text = SECURITY_BASELINE.read_text(encoding="utf-8")
    except (ValueError, FileNotFoundError) as exc:
        print(f"ERROR: {exc}")
        return 1
    failures.extend(validate_manifest(manifest))
    failures.extend(validate_security(profile, baseline_text))
    failures.extend(validate_task_registry(registry))
    artifact_examples = examples(EXAMPLE_ARTIFACTS)
    if not artifact_examples: failures.append("at least one artifact example is required")
    for path in artifact_examples:
        try: artifact = load_json(path)
        except ValueError as exc: failures.append(str(exc)); continue
        failures.extend(f"{path.relative_to(ROOT)}: {e}" for e in schema_errors(artifact, artifact_schema))
        failures.extend(validate_artifact_semantics(artifact, path))
    event_examples = examples(EXAMPLE_EVENTS)
    for path in event_examples:
        try: event = load_json(path)
        except ValueError as exc: failures.append(str(exc)); continue
        failures.extend(f"{path.relative_to(ROOT)}: {e}" for e in schema_errors(event, event_schema))
    if failures:
        print("HydraSafe validation FAILED")
        for failure in failures: print(f"- {failure}")
        return 1
    print(f"HydraSafe validation PASSED: {len(artifact_examples)} artifact example(s), {len(event_examples)} event example(s), federal-floor-plus security profile, and task registry.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
