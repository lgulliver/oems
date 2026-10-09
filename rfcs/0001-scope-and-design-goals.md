# RFC 0001 Scope and design goals

Status: proposed
Author: Liam Gulliver
Affected draft line: v0.1

## Problem

Tools can report identical metric names using different deployment units, timestamps and evidence assumptions. Small organisations need understandable results across mixed providers.

## Proposal

Define a service-level delivery vocabulary, provenance envelope, five DORA calculation policies and synthetic test vectors. Publish language-neutral JSON Schemas and prose together. Keep application collectors and UI outside this repository.

One qualifying deployment changes the effective production version or configuration of one logical service. Tenant, regional and job fan-out are subordinate outcomes of that rollout. A production-effective failure remains in the population. Successful builds that do not change production are excluded.

Unknown collection or classification data must remain visible. Failure and rework are independent properties. Proximity of an incident to a deployment is insufficient to establish causality.

## Alternatives

Provider-specific metric engines fragment semantics. An application-only model prevents independent interoperability. Standardising all engineering measurement immediately risks an oversized and unreviewable first contract.

## Compatibility and verification

No released consumers exist. This draft may change. Proposed cases cover complete data, no deployments and incomplete classifications. More cases are required before release.

## Open questions

- Confirm production rollout grouping and ambiguous deployment handling.
- Agree failure-onset evidence and approximation rules.
- Decide how immutable evidence and privacy deletion interact.
- Select licensing, contribution terms and conformance-claim policy.
- Validate deployment and change provenance across classic and YAML pipelines.

## Decision record

Not yet accepted. The files in this repository illustrate the proposal and do not imply a final standards decision.
