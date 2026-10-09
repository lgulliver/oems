# Failed deployment recovery time

Status: proposed OEMS DORA measurement profile.

## Research framing

DORA describes this measure as restoration time after a deployment-related failure. See [the primary research guide](https://dora.dev/guides/dora-metrics/). The detailed rules below are OEMS proposals, not an assertion that DORA prescribes these calculations.

## Proposed calculation

Select confirmed service recovery episodes whose failure_started_at lies within the window and whose causal deployment is explicitly linked. For completed episodes subtract failure_started_at from restored_at and compute the median. Open episodes are disclosed and excluded from completed medians.

## Evidence and edge cases

Start uses confirmed failure onset; a deployment-time approximation requires an explicit flag. Alert acknowledgement and ticket closure are not restoration. With no completed episodes the median is null; disclose open_count.

Apply [shared measurement rules](../measurement-rules.md). Preserve the measurement period, evidence cutoff, population, profile version and missing-data counts. Inspect [conformance cases](../../../conformance/v0.1/README.md); this initial set is incomplete and does not support a certification claim.
