# Deployment rework rate

Status: proposed OEMS DORA measurement profile.

## Research framing

DORA describes this measure as share of unplanned deployments driven by production incidents. See [the primary research guide](https://dora.dev/guides/dora-metrics/). The detailed rules below are OEMS proposals, not an assertion that DORA prescribes these calculations.

## Proposed calculation

Use qualifying deployments in the window as the denominator. Count distinct deployments classified incident_driven as the numerator. Unknown rework classifications remain in the denominator. lower_bound=numerator/denominator; upper_bound=(numerator+unknown_count)/denominator.

## Evidence and edge cases

Zero denominator gives null bounds. Failure and rework are independent: a planned rollout can cause a failure; a successful incident hotfix can be rework. Temporal proximity alone cannot establish incident-driven intent.

Apply [shared measurement rules](../measurement-rules.md). Preserve the measurement period, evidence cutoff, population, profile version and missing-data counts. Inspect [conformance cases](../../../conformance/v0.1/README.md); this initial set is incomplete and does not support a certification claim.
