# Release Process (HydraSafe)

## Core Compatibility
HydraSafe aligns to DiamondOps-Core releases.

Pin Core version here:
- Core compatibility: v0.1.x (update as you adopt newer Core)

## Versioning
SemVer:
- PATCH: docs/runbooks/template fixes
- MINOR: new templates, additive artifacts, new event exports
- MAJOR: breaking structure changes in deliverables

## Release steps
1. Update docs/templates
2. Update `README.md` if product scope changes
3. Create GitHub Release tag: `vX.Y.Z`
4. Include “Core compatibility” in release notes

## StegBrain Compatibility
StegBrain validates against DiamondOps-Core v0.3.x schemas.
Schema upgrades require StegBrain review.
