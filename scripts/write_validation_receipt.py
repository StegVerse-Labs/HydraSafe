#!/usr/bin/env python3
"""Write a deterministic HydraSafe repository-validation receipt.

The receipt is intended for GitHub Actions artifact retention. It records the
validated commit, workflow context, validator command, result, and next state.
The workflow invokes this script only after repository validation succeeds.
"""

from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "receipts" / "validation-receipt.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    required = [
        ROOT / "security" / "HYDRASAFE_SECURITY_BASELINE.md",
        ROOT / "security" / "control-profile.json",
        ROOT / "ops" / "task-registry.json",
        ROOT / "scripts" / "validate_repository.py",
        ROOT / ".github" / "workflows" / "validate-hydrasafe.yml",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
    if missing:
        raise SystemExit("cannot write receipt; missing: " + ", ".join(missing))

    receipt = {
        "receipt_type": "hydrasafe.repository-validation",
        "receipt_version": "0.1.0",
        "repository": os.getenv("GITHUB_REPOSITORY", "StegVerse-Labs/HydraSafe"),
        "commit_sha": os.getenv("GITHUB_SHA", "local-uncommitted"),
        "ref": os.getenv("GITHUB_REF", "local"),
        "workflow": os.getenv("GITHUB_WORKFLOW", "local-validation"),
        "run_id": os.getenv("GITHUB_RUN_ID", "local"),
        "run_attempt": os.getenv("GITHUB_RUN_ATTEMPT", "1"),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "validator_command": "python scripts/validate_repository.py",
        "result": "COMPLETE",
        "next_state": "CLAIM_RELEASE_ELIGIBLE",
        "fail_closed": True,
        "evidence": [
            {"path": str(path.relative_to(ROOT)), "sha256": digest(path)}
            for path in required
        ],
        "authority": {
            "certification": False,
            "federal_authorization": False,
            "operational_authorization": False,
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
