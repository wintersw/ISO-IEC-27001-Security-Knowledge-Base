---
title: ISMS Evidence Model
description: Defines how evidence should be designed, retained, and reviewed.
category: ISMS
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - isms
  - best-practice
---

# ISMS Evidence Model

An evidence model defines which records demonstrate that the information security management system (ISMS) and its controls were designed, operated, reviewed, and improved.

## Purpose

The model helps teams plan evidence as part of normal work instead of assembling screenshots shortly before an audit. It also distinguishes proof that a rule exists from proof that it operated and achieved its intended result.

## Evidence categories

- **Design evidence:** approved policies, standards, procedures, configurations, and assigned responsibilities.
- **Operating evidence:** tickets, logs, reports, approvals, and other records produced when the activity occurs.
- **Review evidence:** sampling, challenge, decisions, and follow-up performed by an authorized reviewer.
- **Effectiveness evidence:** tests, outcomes, trends, and failures showing whether the intended result was achieved.
- **Improvement evidence:** root-cause analysis, corrective actions, changed controls, and verified results.

## Evidence quality criteria

Good evidence is:

- relevant
- complete
- dated
- traceable
- authentic
- protected from unauthorized alteration
- retained for an appropriate period

Retain both design and operating evidence. A policy or control description shows intent but does not prove that the control operated. Prefer authoritative, scoped records that establish the complete population and preserve relevant approvals, exceptions, decisions, remediation, and review history.

## Best practices

- Define evidence before implementing a control.
- Prefer system-generated evidence.
- Store evidence in controlled repositories.
- Link evidence to the Statement of Applicability (SoA) and risk records.
- Avoid screenshots when better exports exist.

## Practical implementation

For each important activity, identify the evidence owner, authoritative source, complete population, collection frequency, format, review method, retention period, access restrictions, and disposal trigger. Record how failures and missing records are escalated. Evidence collection should be repeatable without giving auditors or administrators unnecessary standing access.

## Practical example

For a quarterly access review, the approved procedure is design evidence. The complete account export, reviewer decisions, and completed removal tickets are operating evidence. Independent sampling is review evidence. A reduction in inappropriate access and verified timely removals provide effectiveness evidence. A workflow change after a missed application is improvement evidence.

## Evidence to retain

Evidence that the model itself operates includes:

- evidence catalog and ownership assignments;
- source, retention, protection, and collection rules;
- collection and review workflow records;
- missing-evidence exceptions and remediation; and
- audit sampling and improvement results.


## Common mistakes

- retaining policies but no operating records;
- collecting a sample without proving the complete population;
- relying on screenshots that omit source, filters, time, or approval;
- giving evidence repositories excessive or permanent access;
- retaining sensitive records indefinitely without a defined need; and
- closing findings without evidence that corrective action was effective.

## Related controls, clauses, templates, and checklists

- [Documented information](documented-information.md)
- [Evidence and Assurance Lifecycle](../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Evidence Catalog](../15-reference/evidence-catalog.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Control Test Record Template](../10-templates/control-test-record-template.md)
- [ITSM Evidence Quality Checklist](../11-checklists/itsm-evidence-quality-checklist.md)
- [A.5.33 Protection of records](../06-annex-a/organizational/a5-33-protection-of-records.md)
