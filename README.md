# Open Engineering Metrics Standard

OEMS is an open specification in development for describing engineering measurement evidence and calculating transparent, reproducible metrics across tools.

**Status: v0.1 working draft.** There is no stable release, certification programme or claim of standards-body recognition. Repository materials are licensed under [Apache 2.0](LICENSE); see [LICENSING.md](LICENSING.md) for scope and contribution terms.

## Why this exists

Engineering teams use different combinations of source control, work tracking, delivery and observability systems. The same metric name can conceal different populations, timestamps and assumptions. OEMS aims to make those decisions explicit so independently developed tools can interpret the same evidence consistently.

The first draft addresses service-level delivery evidence and all five current DORA measures:

- Deployment frequency
- Change lead time
- Change fail rate
- Failed deployment recovery time
- Deployment rework rate

DORA supplies the research framing. OEMS defines operational rules and interchange records; those rules must not be attributed to DORA as prescribed implementation details.

## Start here

- [Draft specification](specification/v0.1/overview.md)
- [Adopted scope and design goals](rfcs/0001-scope-and-design-goals.md)
- [Technical review and adopted v0.1 contract](rfcs/0002-v0.1-preview-contract.md)
- [Schemas](schemas/v0.1/README.md) and [examples](examples/v0.1/README.md)
- [Conformance cases](conformance/v0.1/README.md)
- [Contribution process](CONTRIBUTING.md), [governance](GOVERNANCE.md) and [versioning](VERSIONING.md)
- [Roadmap](ROADMAP.md)

## Relationship to Clio

Clio is the planned reference application. It will collect provider evidence, implement a published OEMS version and offer dashboards and executive reports. Clio's code and releases belong in a separate repository. No Clio repository or completed implementation is claimed here.

OEMS is language-neutral. Schemas and test data use JSON; an implementation can be written in TypeScript, Go, Rust or another language.

## Repository contents

| Directory | Contents |
| --- | --- |
| specification/v0.1 | Draft meanings, evidence rules and metric calculations |
| schemas/v0.1 | Draft JSON Schemas for entity, dataset and result shapes |
| examples/v0.1 | Synthetic records illustrating those shapes |
| conformance/v0.1 | Input datasets and expected metric outputs |
| rfcs | Design proposals and recorded tradeoffs |

## Research attribution

[DORA's software delivery performance metrics](https://dora.dev/guides/dora-metrics/) is the primary source for the five-measure research framing. The operational policy in this draft is OEMS's own contract. Later developer-experience work will use the [SPACE research](https://www.microsoft.com/en-us/research/publication/the-space-of-developer-productivity-theres-more-to-it-than-you-think/) as framing without asserting a universal productivity score or copying proprietary survey instruments.

## Check the working draft

```sh
python -m pip install -r requirements-dev.txt
python tools/validate_v0_1.py
```

The optional Python helper validates local schemas, semantic rules and full fixture outputs. The contract is language-neutral. CI runs the same checks; passing fixtures is not certification. See the [conformance guide](conformance/v0.1/README.md).
