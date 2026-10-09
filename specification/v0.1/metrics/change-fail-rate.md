# Change fail rate

Status: proposed OEMS DORA measurement profile.

## Research framing

DORA describes this measure as share of production deployments requiring immediate intervention. See [the primary research guide](https://dora.dev/guides/dora-metrics/). The detailed rules below are OEMS proposals, not an assertion that DORA prescribes these calculations.

## Proposed calculation

Use qualifying deployments in the window as the denominator. Count distinct deployments classified failed as the numerator. Unknown failure classifications remain in the denominator. lower_bound=numerator/denominator; upper_bound=(numerator+unknown_count)/denominator.

## Evidence and edge cases

Zero denominator gives null bounds. Unknown classifications make the result provisional. No recorded failure describes the available evidence, not guaranteed absence of failure. CI failure alone does not classify a production failure.

Apply [shared measurement rules](../measurement-rules.md). Preserve the measurement period, evidence cutoff, population, profile version and missing-data counts. Inspect [conformance cases](../../../conformance/v0.1/README.md); this initial set is incomplete and does not support a certification claim.
