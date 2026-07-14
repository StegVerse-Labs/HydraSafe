# HydraSafe Mirror Handoff

## Status

- **Repository:** `StegVerse-Labs/HydraSafe`
- **Parent ecosystem:** DiamondOps
- **Canonical dependency:** `StegVerse-Labs/DiamondOps-Core`
- **Product role:** Safety, permitting, commissioning, inspection, and incident-documentation layer for hydrogen and reactive-gas environments
- **Posture:** Documentation-first; no physical control, installation, operation, or maintenance authority
- **Completed goal:** Define and validate the HydraSafe artifact envelope
- **Current activation goal:** Install framework templates and map validated exports for YieldOS ingestion

## Naming decision

**HydraSafe** is named for the Hydra as a model of multi-headed, cascading, and interacting hazards. The name distinguishes this repository from a water-oriented `HydroSafe` product and reflects the reality that hydrogen and reactive-gas safety involves coupled risks across pressure, ignition, ventilation, detection, materials compatibility, operating state, human procedure, and emergency response.

The name does not grant or imply operational authority. HydraSafe remains a documentation, schema, checklist, permitting-framework, and evidence-export product within DiamondOps.

## Product scope

HydraSafe may provide:

- permit packet templates at framework level;
- commissioning and inspection checklists;
- incident response playbooks;
- hazard-review and readiness documentation;
- event and export conventions aligned to DiamondOps-Core;
- integration specifications for YieldOS ingestion;
- documentation-only evidence packets for customers, insurers, regulators, and partners.

HydraSafe must not:

- manufacture, install, operate, maintain, or control equipment;
- represent templates as jurisdiction-specific legal approval;
- override OEM, authority-having-jurisdiction, licensed-engineer, owner, installer, or operator obligations;
- redefine DiamondOps-Core canonical liability or governance documents locally.

## Canonical relationship

DiamondOps-Core is authoritative for shared schemas, standards, governance, and liability boundaries. HydraSafe may add domain-specific documentation and mappings, but any conflict is resolved in favor of DiamondOps-Core.

Canonical files synchronized into this repository are read-only downstream copies. Changes to those documents must originate in DiamondOps-Core and propagate through the approved synchronization path.

## Installed product contract

The following components are installed and committed:

- `README.md` — product-facing DiamondOps boundary and naming rationale;
- `hydrasafe.manifest.json` — machine-readable product identity, scope, authority, dependencies, and active goal;
- `schemas/hydrasafe-artifact.schema.json` — HydraSafe documentation-artifact envelope;
- `schemas/hydrasafe-event.schema.json` — lifecycle and integration event envelope;
- `examples/artifacts/commissioning-checklist.example.json` — schema-valid boundary-safe artifact example;
- `examples/events/artifact-created.example.json` — schema-valid event example;
- `scripts/validate_repository.py` — schema plus semantic-policy validation;
- `.github/workflows/validate-hydrasafe.yml` — automated repository validation;
- `docs/EVIDENCE_PACK.md` — synchronized DiamondOps canonical evidence pack.

## Artifact-envelope invariants

Every HydraSafe artifact must identify:

- artifact identity, class, and semantic version;
- hazard domains and lifecycle stage;
- project/facility scope without embedding unnecessary sensitive data;
- issuer and documentation-only authority class;
- required and completed external review posture;
- DiamondOps-Core canonical references;
- evidence references;
- status and disposition;
- creation/update timestamps;
- integrity metadata;
- explicit denial of physical-control, permit-issuance, and engineering-approval authority.

A `complete` artifact is invalid unless its review posture is `externally-reviewed` or `superseded`. At least one DiamondOps-Core canonical reference is required by repository validation.

## Event invariants

HydraSafe events record:

- event and artifact identity;
- lifecycle event type;
- actor and authority class;
- source and destination;
- previous-event hash and event hash;
- event payload;
- canonical references;
- downstream receipt state when applicable.

YieldOS acceptance must be represented by a separate downstream receipt or event. HydraSafe creation or export does not imply YieldOS acceptance or execution authority.

## Integration contract

HydraSafe deliverables are structured so DiamondOps services can identify:

- artifact type and version;
- facility or project scope without embedding unnecessary sensitive data;
- hazard domain;
- lifecycle stage;
- issuer and review posture;
- referenced DiamondOps-Core schema or standard;
- evidence references;
- status and disposition;
- creation and update timestamps;
- export integrity metadata.

YieldOS ingestion remains a downstream consumer contract. HydraSafe defines export-ready safety and permitting artifacts; it does not assume YieldOS execution or acceptance authority.

## Development sequence

1. **Complete:** Replace the scaffold README with a product-facing repository contract.
2. **Complete:** Add a machine-readable HydraSafe manifest aligned to DiamondOps-Core.
3. **Complete:** Define and validate artifact and event envelopes.
4. **Active:** Add framework templates with explicit jurisdiction/OEM/qualified-professional review gates.
5. Define YieldOS ingestion mapping, receipt behavior, and validation examples.
6. Extend validation to template metadata, broken canonical references, and synchronized-file protection.
7. Add incident-response playbooks and evidence-export examples.
8. Prepare a release candidate only after documentation boundaries, schemas, examples, and validation are complete.

## Known remaining files and modules

Destination: `StegVerse-Labs/HydraSafe`

- `templates/permit-packet/README.md`
- `templates/permit-packet/permit-packet.template.json`
- `templates/commissioning/README.md`
- `templates/commissioning/commissioning-checklist.template.json`
- `templates/inspection/README.md`
- `templates/inspection/inspection-checklist.template.json`
- `playbooks/incident-response/README.md`
- `playbooks/incident-response/initial-response.template.json`
- `integrations/yieldos/INGESTION_SPEC.md`
- `integrations/yieldos/yieldos-export.schema.json`
- `examples/yieldos/`
- canonical-reference reachability validation;
- synchronized canonical-file modification protection.

Potential canonical additions, only if absent and approved:

Destination: `StegVerse-Labs/DiamondOps-Core`

- shared artifact-envelope schema if HydraSafe semantics are generalized across DiamondOps products;
- canonical lifecycle/status vocabulary;
- shared evidence-reference and integrity metadata conventions;
- shared downstream receipt envelope.

## Ownership and continuation scope

HydraSafe owns its domain-specific templates, playbooks, examples, mappings, and validation. DiamondOps-Core owns shared canonical definitions. YieldOS owns downstream ingestion behavior.

Continuation is permitted within HydraSafe for product documentation, domain schemas, examples, validation, and integration mappings, provided no local change expands physical authority or contradicts DiamondOps-Core canonicals.

## Validation and pending observation

The repository workflow `.github/workflows/validate-hydrasafe.yml` runs the validator on pushes, pull requests, and manual dispatch. Its required checks are:

- required continuity and canonical files exist;
- manifest retains the DiamondOps parent, canonical dependency, documentation-only posture, and denied authority fields;
- artifact and event examples satisfy Draft 2020-12 schemas;
- artifact examples retain denied authority fields;
- artifact scope declares that sensitive data is not embedded;
- artifacts reference at least one DiamondOps-Core canonical;
- complete artifacts carry an externally reviewed or superseded posture.

A workflow result is an observation of the committed validator, not an expansion of HydraSafe authority.

## Release and ecosystem propagation

When HydraSafe reaches a taggable release state:

1. tag the repository according to the DiamondOps release convention;
2. verify canonical references against DiamondOps-Core;
3. create a follow-up task to verify pertinent release information is reflected in:
   - `StegVerse-Labs/Site`;
   - `GCAT-BCAT-Engine/Publisher`;
   - `admissibility-wiki`;
   - `stegguardian-wiki`.

## Handoff source-of-truth rule

This file is the current session handoff and task source of truth for HydraSafe development. Update it whenever the active goal, ownership, installed components, blockers, release posture, or continuation scope changes.
