# HydroSafe Candidate Research Note: Ferrofluid Microplastic Filtration

Status: SOURCE-DOCUMENTED / RESEARCH ONLY  
Recorded: 2026-09-02T20:40:00-05:00  
Current host repository: `StegVerse-Labs/HydraSafe` (incubation record only)  
Intended product lane: `HydroSafe` water-safety / water-treatment research candidate  
HydraSafe product-scope effect: NONE

## Scope boundary

This record is intentionally **not** a HydraSafe hydrogen/reactive-gas product specification.

`HydraSafe` is the DiamondOps safety and permitting documentation layer for hydrogen and reactive-gas environments. The repository already distinguishes that name from `HydroSafe`, which would ordinarily imply a water-related safety domain.

This file preserves the water-filtration research finding without changing HydraSafe's product boundary. If a distinct `StegVerse-Labs/HydroSafe` repository is created, this document is a migration candidate and that repository must establish its own `*_MIRROR_HANDOFF.md` before product-development work begins.

## Source system

Primary technical source:

- Mia Heller, *Self-Recycling System for Microplastic Removal: Development of a Novel Ferrofluid-Based Filtration Technology for Affordable Water Treatment*, Regeneron ISEF 2025 project abstract (Society for Science).
- Smithsonian Magazine, 2026-03-20, article describing Heller's prototype and reported test results.

The public description should be treated as a prototype report, not an independently certified drinking-water treatment claim.

## Reported architecture

The prototype uses an oil-based ferrofluid and magnetic separation rather than relying only on a disposable solid membrane.

Reported flow:

1. contaminated water is held or introduced into the system;
2. oil-based ferrofluid is introduced into the water containing microplastic particles;
3. the mixture passes through a magnetic-separation stage;
4. the magnetic field draws the ferrofluid-associated microplastic fraction away from the treated water;
5. a layered filter/separation stage assists recovery;
6. treated water exits the process;
7. recovered ferrofluid is returned for reuse in a closed-loop or self-recycling path.

Smithsonian describes the prototype as a multi-module, approximately one-liter-at-a-time system. The ISEF abstract describes pumping ferrofluid into contaminated water, magnetic separation, layered filtration, purified-water output, and ferrofluid recycling.

## Reported results

The project reports:

- **95.52% microplastic removal** by weight in prototype testing;
- **87.15% ferrofluid recovery/recycling**;
- effective filtration of tested PET particles;
- a target of lower-cost, lower-maintenance treatment relative to some conventional approaches.

These are reported project results. They are not recorded here as independent replication, regulatory certification, health-protection certification, or commercial performance guarantees.

## Why the system is technically interesting

The system combines four features that warrant further study:

### 1. Separation without a conventional primary membrane

Magnetic extraction may reduce dependence on a membrane as the principal microplastic capture mechanism. That creates a different fouling, maintenance, and consumables profile than conventional cartridge-only filtration.

### 2. Reusable working medium

Recovering ferrofluid for reuse introduces a circular process variable: filtration performance depends not only on contaminant removal but also on recovery efficiency, degradation, carryover, and cumulative reuse cycles.

### 3. Explicit contaminant custody

The architecture creates a discrete removed fraction containing microplastics and ferrofluid. A production system would need to track where that captured material goes, how it is contained, and how disposal prevents re-release.

### 4. Instrumentable process

The reported project used turbidity sensing to estimate suspended material and process performance. A future HydroSafe system could treat every filtration cycle as a measurable event rather than an opaque household-filter operation.

## HydroSafe research model

A HydroSafe implementation should be evaluated as a **measurement-and-evidence system around a water-treatment process**, not as an assumption that the published prototype is already production-ready.

Candidate process envelope:

```text
SOURCE WATER
   |
   v
CHARACTERIZE / SAMPLE
   |
   v
FERROFLUID DOSING
   |
   v
CONTACT / ASSOCIATION
   |
   v
MAGNETIC SEPARATION
   |----------------------.
   v                      |
TREATED-WATER PATH        |
   |                      |
   v                      |
POST-PROCESS SAMPLE       |
                          |
CAPTURED FRACTION <-------'
   |
   +--> MICROPLASTIC CUSTODY / DISPOSAL
   |
   '--> FERROFLUID RECOVERY --> QUALITY CHECK --> REUSE OR RETIRE
```

Each transition should be independently observable before any removal-efficiency claim is accepted.

## Candidate evidence variables

A HydroSafe evaluation record should eventually capture at least:

- source-water volume;
- source-water microplastic concentration;
- particle-size distribution;
- polymer type(s), including PET and non-PET testing;
- ferrofluid formulation and batch;
- ferrofluid dose;
- contact/residence time;
- field strength and separator geometry;
- flow rate;
- temperature;
- pH and relevant water chemistry;
- pre-process turbidity and particle measurement;
- post-process turbidity and particle measurement;
- measured microplastic mass or count removed;
- ferrofluid recovery percentage;
- ferrofluid carryover into treated water;
- number of reuse cycles;
- change in removal efficiency across reuse cycles;
- captured-material mass and disposition;
- energy consumption;
- consumables consumption;
- cleaning/maintenance interval;
- sensor calibration evidence;
- operator/procedure version;
- test and sample provenance.

## Critical validation questions

Before HydroSafe could characterize this as a viable treatment technology, the following must be answered experimentally or through authoritative external evidence:

1. Does removal efficiency hold across particle sizes substantially below the tested range?
2. Does performance generalize across PE, PP, PS, PVC, nylon, PET, tire-wear particles, fibers, and mixed environmental samples?
3. What is the treated-water concentration of ferrofluid constituents after separation?
4. Does repeated ferrofluid reuse change particle affinity, viscosity, stability, toxicity, or separation efficiency?
5. What happens in hard water, high-organic-load water, saline water, wastewater, and chemically complex source water?
6. What magnetic-field strength and residence time are necessary at higher flow rates?
7. Does scaling create aggregation, fouling, heat, pumping, or separation limitations?
8. Can the captured microplastic fraction be handled without secondary release?
9. What maintenance burden appears after tens, hundreds, or thousands of cycles?
10. How should performance be verified using direct particle characterization rather than turbidity alone?
11. What standards, drinking-water regulations, material-contact requirements, and disposal rules would apply to a production device?
12. What lifecycle cost and energy profile results after ferrofluid loss, replacement, cleaning, sensors, magnets, pumps, and disposal are included?

## StegVerse / DiamondOps relevance

The strongest ecosystem fit is not a claim to own or reproduce Heller's invention. It is the ability to make experimental and operational evidence reconstructable.

Potential governed evidence surfaces include:

- input-water characterization record;
- ferrofluid batch and custody record;
- filtration-cycle manifest;
- sensor calibration record;
- separation outcome;
- recovered-medium record;
- contaminant-custody record;
- disposal record;
- test protocol version;
- reviewer disposition;
- replication receipt.

A future HydroSafe lane should separate:

- **observed measurements** from **derived performance claims**;
- **prototype evidence** from **commercial-readiness claims**;
- **filtration success** from **drinking-water safety**;
- **research findings** from **regulatory approval**;
- **process observability** from **physical-control authority**.

## Intellectual-property and attribution boundary

This record documents a publicly described third-party prototype for research awareness and architecture comparison.

It does **not**:

- claim invention or ownership by StegVerse, DiamondOps, HydraSafe, or a future HydroSafe entity;
- authorize reproduction of protected claims;
- establish freedom to operate;
- determine patent status;
- reproduce a complete build recipe;
- assert that ferrofluid treatment is safe for human consumption without further evidence.

Any product-development lane must perform an independent patent / prior-art / licensing review before adopting protected implementation details.

## Recommended next research artifacts

If the HydroSafe lane is activated, create:

- `docs/HYDROSAFE_MIRROR_HANDOFF.md`;
- `research/microplastics/ferrofluid-literature-map.md`;
- `research/microplastics/replication-test-plan.md`;
- `schemas/water-test-cycle.schema.json`;
- `schemas/contaminant-custody.schema.json`;
- `schemas/working-medium-recovery.schema.json`;
- `examples/microplastics/`;
- a regulatory/material-contact applicability matrix;
- a patent/prior-art review record;
- a bench-validation evidence pack.

## Current disposition

**Documented as a distinct HydroSafe candidate.**

No HydraSafe hydrogen/reactive-gas requirement, release gate, authority boundary, or commercial offer is changed by this research note.
