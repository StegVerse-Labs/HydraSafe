# HydraSafe Federal-Floor-Plus Security Baseline

Status: REQUIRED
Owner: StegVerse-Labs/HydraSafe
Canonical dependency: StegVerse-Labs/DiamondOps-Core
Applies to: repository content, commercial delivery artifacts, facility document intake, exports, integrations, CI, and evidence handling

## Policy

Applicable United States federal cybersecurity requirements and guidance are the minimum acceptable floor. HydraSafe must exceed that floor where stronger controls are technically and operationally feasible.

This baseline does not claim federal certification, FedRAMP authorization, FISMA authorization, CMMC status, legal compliance, engineering approval, or authority to operate. Applicability must be determined for each engagement by the customer and qualified authorities.

## Reference floor

HydraSafe control selection must account for, at minimum:

- NIST SP 800-53 Rev. 5 security and privacy controls;
- NIST SP 800-82 Rev. 3 guidance for operational technology security;
- NIST SP 800-171 Rev. 3 when Controlled Unclassified Information is in scope;
- FIPS 140-3 validated cryptography when federal requirements or contract terms require it;
- CISA Secure by Design principles and Cross-Sector Cybersecurity Performance Goals;
- applicable agency, contractual, export-control, privacy, records-retention, and critical-infrastructure requirements.

A control is not satisfied by citation alone. Each applicable control must have implementation evidence, validation evidence, an owner, and a review date.

## Mandatory controls

1. **Data minimization and classification**
   - Collect only data necessary for the bounded documentary purpose.
   - Classify every intake and output as PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED, CUI-CANDIDATE, or PROHIBITED.
   - Do not place facility-sensitive, security-sensitive, CUI, export-controlled, personal, credential, or secret material in this public repository.

2. **Fail-closed intake**
   - Intake is rejected when classification, owner, authorization, retention, or permitted-use metadata is absent.
   - CUI-CANDIDATE and PROHIBITED material must not enter ordinary HydraSafe repository or collaboration paths.

3. **Least privilege and separation of duties**
   - Access is role-bound, time-bounded, reviewable, and revoked on role change.
   - Artifact author, independent reviewer, approver, and downstream recipient must be distinguishable.
   - HydraSafe cannot self-assign engineering, permit, legal, AHJ, or operational authority.

4. **Strong identity and authentication**
   - Multi-factor authentication is required for privileged and production-adjacent access.
   - Shared credentials are prohibited.
   - Machine identities must be scoped to the minimum repository, workflow, environment, and duration.

5. **Cryptographic protection**
   - Sensitive data must be encrypted in transit and at rest using approved, maintained cryptographic implementations.
   - Federal or contractual use must require the applicable FIPS-validated module boundary.
   - Integrity records must use SHA-256 or stronger approved algorithms and must identify the algorithm.

6. **Immutable provenance and evidence**
   - Every released artifact must record source, author, reviewer posture, canonical references, version, timestamp, disposition, and integrity digest.
   - Hash-chain or signed-receipt continuity is required for transfers involving restricted facility artifacts.
   - Missing provenance blocks release.

7. **Secure-by-default delivery**
   - Public sharing, anonymous links, unrestricted exports, and persistent broad access are disabled by default.
   - Customer-specific work must use a controlled delivery environment, not repository commits.
   - Examples and templates must contain synthetic data only.

8. **OT and safety separation**
   - HydraSafe documentation, schemas, and integrations must not directly control PLCs, SIS, interlocks, actuators, valves, alarms, or other physical systems.
   - Any data exchange with OT-adjacent systems must be read-only by default, mediated, authenticated, logged, and independently authorized.
   - Loss of HydraSafe services must not impair a physical safety function.

9. **Logging and detection**
   - Security-relevant access, mutation, export, validation, and release events must be logged.
   - Logs must be tamper-evident, time-synchronized, access-controlled, and retained under a declared schedule.
   - Missing required logging blocks release or export.

10. **Vulnerability and dependency management**
    - Dependencies must be pinned or constrained, inventoried, and scanned.
    - Known exploited or critical vulnerabilities must trigger fail-closed release review until remediated or formally risk-accepted by authorized ownership.
    - Secrets scanning, dependency review, static validation, and artifact validation are required in CI where supported.

11. **Incident response and recovery**
    - Security incidents must have severity, owner, containment, evidence-preservation, notification, recovery, and lessons-learned records.
    - Recovery must be tested; backups alone are not recovery evidence.
    - Safety incidents and cybersecurity incidents must be cross-referenced when causal interaction is possible.

12. **Supplier and integration controls**
    - YieldOS and every downstream consumer must validate schema, integrity, provenance, authorization, and classification before acceptance.
    - An export event is not an ingestion receipt, and an ingestion receipt is not operational authorization.
    - Missing or unverifiable downstream evidence yields REVIEW_REQUIRED or BLOCKED, never implicit success.

## Exceeding the floor

HydraSafe adopts these additional requirements even when not explicitly mandated for a specific nonfederal engagement:

- deny-by-default authority and data handling;
- signed or hash-chained high-sensitivity transfer receipts;
- independent review before a facility artifact can be marked complete;
- machine-enforced prohibition on operational-control claims;
- deterministic validation with inspectable receipts;
- short-lived machine credentials and protected deployment environments;
- continuous claim collision detection and stale-claim expiration;
- explicit human-authority gates for legal, engineering, AHJ, insurer, OEM, owner, installer, and operator decisions.

## Required evidence

No control may be marked complete without:

- control identifier and applicability statement;
- implementation location;
- accountable owner;
- validation command or procedure;
- dated evidence or receipt;
- exceptions and expiration date;
- next review date.

## Release gate

A HydraSafe release or customer delivery is blocked when any required security control is missing, unowned, unvalidated, expired, or contradicted by the artifact being released.
