# HydraSafe

[![DiamondOps-Core Canonicals](https://github.com/stegverse-labs/stegdb/actions/workflows/sync-diamondops-core-canonicals.yml/badge.svg)](https://github.com/stegverse-labs/stegdb/actions/workflows/sync-diamondops-core-canonicals.yml)

> HydraSafe is the DiamondOps safety and permitting documentation layer for hydrogen and reactive-gas environments.
>
> HydraSafe is documentation-only and operates under the DiamondOps liability model. It does not manufacture, install, operate, maintain, or control physical systems.

## Why HydraSafe

The name refers to the Hydra as a model of **multi-headed, cascading, and interacting risk**. Hydrogen and reactive-gas environments combine hazards involving pressure, ignition, ventilation, detection, materials compatibility, operating state, human procedure, and emergency response.

`HydraSafe` therefore describes coordinated control of coupled hazards. It is intentionally distinct from `HydroSafe`, which would ordinarily suggest water-related safety.

## DiamondOps role

HydraSafe is a product-facing component of DiamondOps. It consumes shared schemas, standards, governance rules, and liability boundaries from [`StegVerse-Labs/DiamondOps-Core`](https://github.com/StegVerse-Labs/DiamondOps-Core).

HydraSafe owns domain-specific:

- permit packet frameworks;
- commissioning and inspection checklists;
- incident response playbooks;
- hazard-review and readiness documentation;
- event and export conventions aligned to DiamondOps-Core;
- YieldOS ingestion specifications;
- evidence packages for customer, insurer, regulator, and partner review.

Any conflict between a HydraSafe document and a DiamondOps-Core canonical must be resolved in favor of DiamondOps-Core.

## Scope for v0.1

The first release is documentation-first and focuses on:

1. versioned HydraSafe artifact and event schemas;
2. framework-level permit, commissioning, inspection, and incident templates;
3. explicit review gates for jurisdictional, OEM, engineering, owner, installer, and operator requirements;
4. deterministic export conventions for DiamondOps and YieldOS consumers;
5. examples and validation that demonstrate the documentation-only boundary.

## Responsibility boundary

HydraSafe materials are frameworks and evidence artifacts. They are not permits, engineering approvals, operating authorization, legal advice, or substitutes for review by the authority having jurisdiction, qualified professionals, OEMs, asset owners, installers, or operators.

## Evidence pack

For customer, insurer, and regulator-facing proof of DiamondOps' documentation-only posture and canonical governance, see [`docs/EVIDENCE_PACK.md`](docs/EVIDENCE_PACK.md).

Canonical liability boundary:

- [`DiamondOps-Core/docs/LIABILITY_BOUNDARY.md`](https://github.com/StegVerse-Labs/DiamondOps-Core/blob/main/docs/LIABILITY_BOUNDARY.md)

## Development handoff

The current development source of truth is [`docs/HYDRASAFE_MIRROR_HANDOFF.md`](docs/HYDRASAFE_MIRROR_HANDOFF.md). It records scope, ownership, integration boundaries, remaining components, and the active release sequence.
