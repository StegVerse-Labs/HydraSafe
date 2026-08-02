# Security Policy (HydraSafe)

HydraSafe treats applicable United States federal cybersecurity requirements as the minimum floor and applies stronger fail-closed controls where technically and operationally feasible.

Authoritative repo-local baseline:

- `security/HYDRASAFE_SECURITY_BASELINE.md`
- `security/control-profile.json`
- `ops/task-registry.json`

HydraSafe is documentation-only. It does not control physical equipment, approve engineering, issue permits, authorize operations, or claim federal certification or authorization.

## Data restrictions

Do not commit secrets, credentials, customer records, facility-identifying sensitive data, CUI, export-controlled material, security-sensitive OT details, or personal data to this public repository. Templates and examples must use synthetic data only.

Customer-specific work must use an authorized controlled delivery environment with classification, access, retention, encryption, logging, provenance, and review controls defined before intake.

## Reporting

Report suspected vulnerabilities or accidental sensitive-data exposure through GitHub Security Advisories. Do not open a public issue containing exploit details, credentials, customer information, facility details, or evidence that could increase physical or cyber risk.

## Release behavior

Security evidence is required for release and delivery. Missing classification, authority, provenance, validation, logging, or required review causes a fail-closed `BLOCKED` or `REVIEW_REQUIRED` result rather than implicit success.
