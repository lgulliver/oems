# Change lead time

Status: proposed OEMS DORA measurement profile.

## Research framing

DORA describes this measure as commit to production elapsed time. See [the primary research guide](https://dora.dev/guides/dora-metrics/). The detailed rules below are OEMS proposals, not an assertion that DORA prescribes these calculations.

## Proposed calculation

For each change first deployed to this service during the window, subtract its committer timestamp from that first deployment's effective_at. Compute the median of valid durations. Use reconciled history to exclude changes already deployed before the window. A dataset MUST declare whether deployment history is sufficient to identify the first deployment.

## Evidence and edge cases

Missing change links or insufficient history make coverage incomplete; missing timestamps are not zero. A deployed squash commit is the default unit; an earlier PR-first-commit measure is a separate flow metric. Report linked observations and unresolved provenance.

Apply [shared measurement rules](../measurement-rules.md). Preserve the measurement period, evidence cutoff, population, profile version and missing-data counts. Inspect [conformance cases](../../../conformance/v0.1/README.md); this initial set is incomplete and does not support a certification claim.
