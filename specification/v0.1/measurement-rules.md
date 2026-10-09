# Shared measurement rules

Status: working proposal.

Results identify service, half-open period [start,end), reporting timezone, evidence cutoff, profile version and quality state. UTC boundary instants MUST be supplied so independent implementations need not infer timezone conversion differently.

Deduplicate logical deployments by their stable service deployment ID. Disclose unresolved qualification records; complete final results require both source coverage and resolved qualification. Build success alone is insufficient evidence.

This initial profile uses service-level results. Pooled ratios require sums of underlying populations, and pooled duration statistics require underlying observations. Implementations MUST NOT average service percentages or medians.

Mean, median and percentile are distinct statistics. This draft requires median for durations and defines an even-sized median as the mean of the two middle values. p75 is deferred until its interpolation policy is specified.

Duration units are seconds. Ratios are fractions in [0,1], not percentage numbers. Display software may multiply by 100. Deployment frequency uses deployments per day; day count is the number of reporting calendar dates intersecting the window, supplied in the dataset. The initial fixtures use UTC whole-day windows. Partial-day semantics remain an open release question.

No eligible duration observations yields null. An empty deployment population yields null failure/rework ratios. With complete collection, deployment frequency can be zero. Incomplete collection yields a provisional observed count and no settled frequency rate.

Unknown classifications stay in the qualifying population. Show the known numerator, denominator, unknown count and lower/upper bounds. Such results are provisional. Do not divide only by the classified subset.

The supplied metric fixture format records a result's status (complete, provisional or no_observations). It is an illustrative output contract, not yet a published metric-result schema.
