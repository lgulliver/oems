# Event envelope

Status: working proposal.

An interchange event contains a version, dataset scope, unique event ID, record kind, source reference, occurrence time, collection time and payload. Event identity and entity identity are distinct: several revisions may describe one entity.

Draft schema: [event-envelope.schema.json](../../schemas/v0.1/event-envelope.schema.json).

The payload MUST validate against the schema for record_type. This conditional requirement is semantic in the initial envelope schema; the envelope alone does not validate payload contents.

Implementations MUST preserve source revision identity when available. Delivery order is not revision order. Unknown or conflicting source revisions require reconciliation; an implementation MUST NOT select an arbitrary array position as the truth.

Timestamps use RFC 3339 with an explicit offset. Normalisation stores an equivalent instant; a reporting timezone affects boundaries, not event identity. An observed timestamp is not automatically a production-effective timestamp.

The initial conformance datasets contain already reconciled entity records. They do not claim to exercise ingestion or revision handling; envelope conformance cases remain release work.
