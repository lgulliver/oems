# Draft conformance cases

The fixtures are synthetic proposed calculation cases. They are not a complete certification suite or a released conformance profile.

Each case has an input JSON dataset and an expected JSON result. Input records use the draft entity schemas; collection metadata defines the window and coverage. Outputs use ratios in [0,1] and durations in seconds. See [shared rules](../../specification/v0.1/measurement-rules.md).

| Case | Expected behaviour |
| --- | --- |
| complete | 10 deployments, 10% failure, 20% rework, 2.5h median lead time, 30m recovery |
| empty | Zero frequency with complete collection; null ratios and durations |
| unknown-classifications | Known numerators stay over all deployments; bounds disclose unknowns |

Implementers should validate record shapes, resolve semantic constraints, calculate values and compare outputs. Repeating identical deployment records must not change results. Conflicting duplicates must be rejected.

Additional cases for late evidence, failed production-effective rollouts, tenant fan-out, open episodes and timezone boundaries are required before a release. No reference metric engine is included in this scaffold.
