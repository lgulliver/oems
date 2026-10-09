# Governance

Status: active maintainer-led governance for the working draft.

Liam Gulliver (@lgulliver) is the sole maintainer and decision-maker at this stage. Decisions and rationale are recorded in GitHub issues, pull requests and RFCs. No external steering committee or endorsement is implied.

## Decisions

Editorial corrections can be proposed directly in a pull request. Changes to record meaning, calculation rules, privacy expectations, compatibility or conformance requirements require an RFC before acceptance.

An RFC describes the problem, rules, alternatives, compatibility impact, evidence and examples. The sole maintainer may decide and implement a bounded draft change directly; no committee vote or additional maintainer approval is required. Record the decision and rationale in the RFC and commit the coordinated specification, schema and fixture change. Discussions may inform decisions but do not require a separate proposal-only waiting period. Unresolved objections remain visible. Do not claim acceptance without a recorded maintainer decision.

Contributors can challenge a decision in a linked issue with a concrete counterexample or alternative. Governance changes use the same public RFC process.

## Releases

A release identifies the specification text, schemas, fixture version, known limitations and licence. A stable release requires the release gates in [VERSIONING.md](VERSIONING.md). Application releases cannot silently change OEMS rules.

This working draft has no certification authority. Passing provided cases is evidence about those cases, not proof of complete conformance. Rules for public conformance claims must be agreed before a stable release.

## Independence

Clio is an intended reference implementation. Its preferences do not automatically become standard requirements. New requirements must be useful to independent implementations and must not depend on a particular language, vendor or Clio feature.
