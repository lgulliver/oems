# Governance

Status: proposed initial governance.

Liam Gulliver (@lgulliver) is the initial maintainer. Decisions and rationale are recorded in GitHub issues, pull requests and RFCs. No external steering committee or endorsement is implied.

## Decisions

Editorial corrections can be proposed directly in a pull request. Changes to record meaning, calculation rules, privacy expectations, compatibility or conformance requirements require an RFC before acceptance.

An RFC describes the problem, proposed rules, alternatives, compatibility impact, evidence and examples. The maintainer records acceptance, rejection or deferral with reasons. Unresolved objections remain visible. An author must not describe a proposal as accepted without a recorded decision.

Contributors can challenge a decision in a linked issue with a concrete counterexample or alternative. Governance changes use the same public RFC process.

## Releases

A release identifies the specification text, schemas, fixture version, known limitations and licence. A stable release requires the release gates in [VERSIONING.md](VERSIONING.md). Application releases cannot silently change OEMS rules.

This working draft has no certification authority. Passing provided cases is evidence about those cases, not proof of complete conformance. Rules for public conformance claims must be agreed before a stable release.

## Independence

Clio is an intended reference implementation. Its preferences do not automatically become standard requirements. New requirements must be useful to independent implementations and must not depend on a particular language, vendor or Clio feature.
