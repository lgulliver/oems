# Roadmap

## Initial draft

- Agree the scope and service deployment unit in RFC 0001.
- Review the five DORA calculation policies against realistic workflows.
- Refine record identity, revisions, source evidence and unknown values.
- Define conformance claims and expand semantic test cases.
- Resolve licensing and contribution terms.

## Before a first release

Add shared incidents, open recovery episodes, rollout fan-out, squash/rebase provenance, partial collection, late corrections and timezone boundary cases. Define p75 precisely before requiring it. Confirm how production-effective failures and ambiguous rollout outcomes are represented.

Test the contract with Clio and seek feedback from an independent implementation. Publish an exact version and immutable artifacts only when release gates pass.

## Later profiles

Work-item and PR flow, reliability/SLO evidence, protected developer-experience aggregates and executive report provenance are planned extensions. They are not included in initial DORA conformance. Survey privacy must be designed before response interchange is considered.

A standardised ingestion API is deferred. Initial records are an interchange vocabulary, not an HTTP transport protocol. Provider authentication, collectors, dashboards and PDF rendering belong to applications.
