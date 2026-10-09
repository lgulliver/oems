# Canonical data model

Status: working proposal. Schemas define draft shapes; the following semantics also apply.

IDs are unique within an explicitly identified dataset. Implementations MUST preserve namespaced provider identifiers in provenance rather than joining entities by similar names or project-local numeric IDs alone.

## Records

A service identifies a logical deployable unit. A deployment names one service, its rollout group, environment classification, qualification state, production-effective time, changes and independent failure/rework classifications.

A change identifies a repository and commit and records the committer timestamp. An incident record represents one service recovery episode and links the confirmed causal deployment. Shared incidents may have several service episodes, each with a distinct ID and the same source incident reference.

## Semantic constraints

- A qualifying deployment MUST have a non-null effective_at and environment=production.
- Unknown qualification is unresolved evidence; it MUST be disclosed separately from counted deployments.
- Repeated records with the same ID and identical content are deduplicated.
- Conflicting records with the same ID MUST fail semantic validation. Revision selection is deferred to the envelope policy and must never depend on array order.
- References MUST resolve within the dataset or be explicitly reported as unresolved.
- Lead-time evidence is valid only when a change's timestamp is not after its first production-effective time.
- Restoration cannot precede failure onset.
- A confirmed causal link MUST carry a source reference or review evidence.
- A change already deployed to the same service is not a new lead-time observation.

Current record schemas intentionally omit full provider payloads and personal contributor identity. Retain only the evidence required for interpretation.
