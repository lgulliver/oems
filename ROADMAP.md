# Roadmap

## Initial draft

- Adopted the scope and service deployment unit in RFC 0001.
- Implemented evidence, population and output contracts from [RFC 0002](rfcs/0002-v0.1-preview-contract.md), with schemas, fixtures and CI.
- Review the five DORA calculation policies against realistic workflows.
- Refine record identity, revisions, source evidence and unknown values.
- Define conformance claims and expand semantic test cases.
- Licensing and contribution terms are established under [Apache 2.0](LICENSING.md).

## Before a first release

Shared incidents, open/approximate recovery, fan-out, incomplete collection, unknown qualification and UTC boundary cases are checked. Next validate the contract through a collector/independent implementation and exercise real-world squash/rebase provenance. Non-UTC calendars, partial days and revision-ingestion conformance are separate future profiles. Define p75 precisely before requiring it.

Test the contract with Clio and seek feedback from an independent implementation. Publish an exact version and immutable artifacts only when release gates pass.

## Later profiles

Work-item and PR flow, reliability/SLO evidence, protected developer-experience aggregates and executive report provenance are planned extensions. They are not included in initial DORA conformance. Survey privacy must be designed before response interchange is considered.

A standardised ingestion API is deferred. Initial records are an interchange vocabulary, not an HTTP transport protocol. Provider authentication, collectors, dashboards and PDF rendering belong to applications.
