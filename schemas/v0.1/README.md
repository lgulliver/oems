# Draft schemas

These JSON Schemas use Draft 2020-12. They describe proposed record shapes and use relative local references where needed. No hosted schema endpoint is promised.

Validate service, deployment, change and incident examples against their corresponding files. An envelope payload also needs record-type validation. Shape validation does not resolve reference integrity, duplicate conflicts, timestamp ordering, classification evidence or metric calculation.

Dates require date-time format checking when the validator supports it; configure format checking explicitly. Unknown values are represented through enums or nulls, not zero durations.

Release work includes an output schema, revision-selection rules and additional semantic conformance cases.
