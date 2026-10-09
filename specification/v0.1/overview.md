# OEMS v0.1 overview

Status: working proposal. The words MUST, SHOULD and MAY express intended requirement strength within this draft; they do not announce a stable released standard.

## Scope

This draft describes service-level production delivery records and a proposed DORA measurement profile. It defines data meanings, missing-data behaviour and reproducible calculations. It does not define an ingestion HTTP API.

Read [terminology](terminology.md), [the canonical model](canonical-data-model.md), [the event envelope](event-envelope.md) and [measurement rules](measurement-rules.md) before the individual metric definitions.

## Metric definitions

- [Deployment frequency](metrics/deployment-frequency.md)
- [Change lead time](metrics/change-lead-time.md)
- [Change fail rate](metrics/change-fail-rate.md)
- [Failed deployment recovery time](metrics/failed-deployment-recovery-time.md)
- [Deployment rework rate](metrics/deployment-rework-rate.md)

Research framing: [DORA's current five metrics](https://dora.dev/guides/dora-metrics/). Statistics, record shapes and timestamps specified here are proposed OEMS choices.

## Compliance boundary

JSON Schema validates record shape. Semantic validation establishes meaningful relationships and valid timestamp ordering. Metric cases check expected calculations. Passing one layer does not establish the others.

No conformance designation or badge is authorised by this draft. Implementations should describe the exact draft commit and cases checked rather than claiming certification.
