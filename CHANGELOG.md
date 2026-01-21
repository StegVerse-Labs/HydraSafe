# Changelog — HydraSafe

All notable changes to HydraSafe are documented in this file.

HydraSafe is the DiamondOps safety and permitting layer for hydrogen and reactive-gas environments.
Changes prioritize compliance clarity, auditability, and operational safety.

---

## [0.3.0] — Sellable Deliverables Framework
### Added
- **FRAMEWORK Permit Packet** template set:
  - Indexed, AHJ-ready documentation structure
  - Hazard summary, gas inventory, detection/shutdown narrative
  - Ventilation/exhaust narrative
  - Training & roles
  - Commissioning evidence index
  - Inspection & maintenance plan
  - Incident response plan
  - Appendices (references only)
- **Operational checklists**:
  - Commissioning checklist
  - Monthly / quarterly / annual inspection checklist
- Optional support for aggregated `sensor_reading` export aligned to DiamondOps-Core.

### Changed
- Integration documentation updated to reflect finalized Core schemas.
- Language tightened to reinforce framework-level (non-procedural) posture.

### Impact
- No breaking changes.
- HydraSafe is now suitable for customer-facing delivery and sales discussions.

---

## [0.2.0] — Governance & Platform Wiring
### Added
- `RELEASE.md` defining versioning and Core compatibility expectations.
- `CONTRIBUTING.md` clarifying safety-first contribution rules.
- `SECURITY.md` establishing public-safe posture.
- GitHub issue templates for:
  - customer intake
  - compliance questions
- Pull request template for safety and Core alignment review.

### Impact
- No functional or structural changes.
- Governance and workflow only.

---

## [0.1.0] — Initial HydraSafe Foundation
### Added
- HydraSafe product definition and scope.
- Pod concept documentation (framework-level).
- AHJ playbook and common inspector questions.
- Installation, commissioning, and incident response runbooks.
- YieldOS integration concept aligned to DiamondOps-Core interfaces.

### Impact
- Initial public release.
- Documentation-only, non-operational framework.

---

## Versioning Notes
- PATCH: documentation clarifications and typo fixes
- MINOR: additive templates, checklists, or exports
- MAJOR: breaking structural changes to deliverables or integrations

HydraSafe aligns to DiamondOps-Core releases and documents Core compatibility in `RELEASE.md`.
