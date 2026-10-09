# Deployment frequency

Status: proposed OEMS DORA measurement profile.

## Research framing

DORA describes this measure as production deployment rate. See [the primary research guide](https://dora.dev/guides/dora-metrics/). The detailed rules below are OEMS proposals, not an assertion that DORA prescribes these calculations.

## Proposed calculation

Count distinct qualifying service deployments with effective_at in [start,end). Divide by window.calendar_days only when collection is complete and qualification is resolved. Otherwise preserve the observed count with provisional status and null deployments_per_day. A deployment that became effective then failed remains eligible.

## Evidence and edge cases

Empty complete collection gives count=0 and deployments_per_day=0. Never infer complete history from an empty API response.

Apply [shared measurement rules](../measurement-rules.md). Preserve the measurement period, evidence cutoff, population, profile version and missing-data counts. Inspect [conformance cases](../../../conformance/v0.1/README.md); this initial set is incomplete and does not support a certification claim.
