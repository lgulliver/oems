# RFC 0001 Scope and design goals

Status: adopted for the v0.1 working draft
Author: Liam Gulliver
Affected draft line: v0.1

## Problem

Tools can report identical metric names using different deployment units, timestamps and evidence assumptions. Small organisations need understandable results across mixed providers.

## Adopted scope

Define a service-level delivery vocabulary, provenance envelope, five DORA calculation policies and synthetic test vectors. Publish language-neutral JSON Schemas and prose together. Keep application collectors and UI outside this repository.

One qualifying deployment changes the effective production version or configuration of one logical service. Tenant, regional and job fan-out are subordinate outcomes of that rollout. A production-effective failure remains in the population. Successful builds that do not change production are excluded.

Unknown collection or classification data must remain visible. Failure and rework are independent properties. Proximity of an incident to a deployment is insufficient to establish causality.

## Alternatives

Provider-specific metric engines fragment semantics. An application-only model prevents independent interoperability. Standardising all engineering measurement immediately risks an oversized and unreviewable first contract.

## Compatibility and verification

No released consumers exist. This draft may change. Proposed cases cover complete data, no deployments and incomplete classifications. More cases are required before release.

## Open questions

- Production rollout grouping and unknown qualification are defined in RFC 0002.
- Failure-onset evidence and separate approximate recovery statistics are defined in RFC 0002.
- Decide how immutable evidence and privacy deletion interact.
- Define conformance-claim policy. Licensing and contribution terms are recorded in [LICENSING.md](../LICENSING.md).
- Validate source adapters and provenance across provider pipeline styles; this is adapter work beyond the reconciled-snapshot profile.

## Decision record

The sole maintainer directed progression from review proposals into an implemented working-draft contract on 2026-10-09. The service-level scope and independence goals are adopted; RFC 0002 records the operational choices. Production grouping, onset approximation and first-deployment provenance are implemented there. Snapshot retention/privacy deletion and broader adapter provenance remain future work; their open questions do not block this bounded snapshot profile. This is not acceptance of a stable release or standards-body endorsement.
