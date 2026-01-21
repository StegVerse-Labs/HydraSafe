# HydraSafe

HydraSafe is the **safety, permitting, and compliance documentation layer** of the DiamondOps platform.

It defines how hazardous, regulated, or high-risk environments are **described, validated, and evidenced** — without controlling or operating physical equipment.

HydraSafe exists to make safety decisions **explicit, auditable, and defensible** before, during, and after retrofit or operational work.

---

## What HydraSafe Is

HydraSafe provides:

- Permit and compliance **metadata schemas**
- Safety and inspection **documentation frameworks**
- Incident and interlock **event structures**
- Validation inputs for **StegBrain advisory checks**
- Audit-ready references for regulators, insurers, and operators

HydraSafe answers:

> *What safety rules apply here, what evidence is required, and how do we prove compliance — without touching the equipment?*

---

## What HydraSafe Is NOT

HydraSafe does **not**:

- manufacture, sell, or supply hardware
- install, commission, or operate equipment
- control actuators, interlocks, or safety systems
- replace regulatory authorities or inspectors
- guarantee physical safety outcomes or performance

HydraSafe produces **documentation and validation artifacts only**.  
All physical responsibility remains with asset owners, OEMs, and contractors.

---

## Relationship to DiamondOps

HydraSafe is part of the DiamondOps ecosystem:

- **DiamondOps-Core**  
  Defines canonical schemas and contract semantics.
- **HydraSafe**  
  Specializes in safety, permitting, and compliance artifacts.
- **ReactorOps**  
  Covers retrofit, inspection, and operational change workflows.
- **YieldOS**  
  Aggregates validated records for analysis and reporting.
- **StegBrain**  
  Performs advisory-only schema validation and consistency checks.

HydraSafe outputs are validated against **DiamondOps-Core schemas** and surfaced via **StegBrain**, but HydraSafe itself never enforces or blocks operations.

---

## Repository Structure

Typical directories include:

examples/        # Example safety, permit, and incident records
demo/            # Demonstration-only payloads
meta/diamondops/ # DiamondOps-aligned metadata references
.github/         # CI workflows (StegBrain advisory validation)
stegbrain.allowlist

Only paths listed in `stegbrain.allowlist` are scanned by StegBrain.

---

## Validation & Governance

HydraSafe uses **contract-first validation**:

- Schemas live in **DiamondOps-Core**
- HydraSafe emits structured records
- StegBrain validates conformance (warn-only)
- No automated enforcement or control is performed

This ensures:
- consistent documentation
- early detection of schema drift
- audit-ready artifacts without operational risk

---

## Liability Boundary

HydraSafe operates under the DiamondOps liability model.

> DiamondOps is responsible for the correctness of technical determinations and documentation produced under its schemas at the time of issuance. DiamondOps is not responsible for physical installation, operation, maintenance, or real-world performance of equipment.

See the authoritative statement in:

DiamondOps-Core/LIABILITY_BOUNDARY.md

---

## Intended Use Cases

HydraSafe is designed for:

- Retrofit readiness documentation
- Permit packet preparation
- Safety incident documentation
- Interlock and inspection evidence
- Compliance and audit support
- Pre-install regulatory alignment

It is **documentation-first by design** and safe to use in regulated environments.

---

## Status

HydraSafe is under active development and intended for **professional, industrial, and regulated use cases**.

Schemas are versioned.  
Changes prioritize backward compatibility and audit integrity.

---

## Contributing

Contributions should:
- respect schema contracts
- avoid embedding secrets or sensitive telemetry
- remain documentation-only (no control logic)

Future contributor guidance will be added as the platform matures.

---

## License

See `LICENSE` for details.
