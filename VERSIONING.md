# Versioning and releases

The current material is an unreleased v0.1 working draft. Directory names identify a draft line, not a published release or compatibility guarantee.

A published specification uses semantic versions. Breaking changes to required record shapes or metric meaning require a major version after 1.0. Additive compatible changes require a minor version. Clarifications that preserve meaning require a patch. Before 1.0, semantic changes may occur between minor releases but still need migration notes.

Metric-definition, schema and fixture versions are recorded together in each release manifest. Consumers pin an exact published version. An application must state the version and measurement profile used, plus deviations.

## Stable release gates

- Scope, governance and redistribution/contribution terms are accepted.
- All normative requirements are testable or have a documented review method.
- Schemas, examples and calculation cases agree.
- Unresolved questions and migration rules are published.
- Independent implementation feedback has been reviewed.
- Conformance-claim wording is defined; no unsupported certification claims.
- Release artifacts are immutable and have checksums.

Independent implementation feedback is a project release policy, not a claim that an external standards organisation requires it.
