# HydraSafe Evidence Pack (v0)

HydraSafe is the safety, permitting, and compliance documentation layer of the DiamondOps ecosystem.

HydraSafe is **documentation-only**:
it does not manufacture, install, operate, maintain, or control physical equipment.

## Canonical Governance (Proof)

This repo is governed by **DiamondOps-Core canonical documents** and is kept consistent by StegDB automation.

Canonicals (authoritative):
- `docs/POSITION.md`
- `docs/LIABILITY_BOUNDARY.md`

If these files differ from DiamondOps-Core, StegDB will open a PR to restore compliance.

## What a customer can expect here

HydraSafe provides:
- safety and permitting documentation structures
- audit-ready artifacts and examples
- incident / interlock event documentation conventions
- advisory-only validation inputs (schema conformance), without operational control

## What HydraSafe does not do

HydraSafe does **not**:
- guarantee real-world safety outcomes
- replace regulators or inspectors
- assume duty of care for operation or maintenance
- control interlocks, PLCs, actuators, or safety systems

## Suggested review flow (buyer / insurer / regulator)

1) Read the canonicals:
   - `docs/POSITION.md`
   - `docs/LIABILITY_BOUNDARY.md`

2) Review repo-local docs:
   - `README.md`
   - examples in `examples/` (if present)

3) Confirm provenance:
   - StegDB canonical sync workflow badge is green
