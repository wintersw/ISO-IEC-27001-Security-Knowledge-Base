---
title: Lab 9 — Map ITSM Records to ISO 27001 Evidence
description: Use existing ITSM workflows as evidence without building duplicate processes.
category: Guided Labs
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - lab
  - workshop
  - practical
---

# Lab 9 — Map information technology service management (ITSM) Records to ISO 27001 Evidence

## Scenario

The organization uses an ITSM tool for incidents, changes, service requests, problems, releases, and configuration items.

## Tasks

Map each record type to relevant ISO 27001 clauses or controls. Define required fields, evidence owner, retention, and quality checks.

## Suggested mapping

| ITSM record | information security management system (ISMS) use |
|---|---|
| change | Clause 8, A.8.32, secure release evidence |
| incident | A.5.24–A.5.27 |
| problem | root cause, Clause 10 corrective action |
| access request | A.5.15–A.5.18 |
| CI | A.5.9, vulnerability and continuity scope |
| release | A.8.25–A.8.29 |
| continuity test ticket | A.5.30, A.8.13 |

## Quality example

A change ticket is not useful evidence if it lacks affected asset, approval, test result, implementation outcome, and rollback information.

## Review questions

- Which workflows need security fields?
- Which records can be automatically reported?
- What historical data must be retained?
- How will auditors retrieve linked evidence?

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** This chapter explains **Lab 9 — Map ITSM Records to ISO 27001 Evidence** without reproducing standard text. Determine formal obligations from the applicable clauses, scope, risk treatment, Statement of Applicability, and binding legal or contractual requirements.
- **Implementation guidance:** Adapt the described roles, frequency, workflow, and evidence to the organization.
- **Best practice:** Enhancements are optional unless adopted through policy, contract, or risk treatment.

## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- completed lab output
- assumptions and decision rationale
- review feedback
- revised result and lessons learned

Intent documents are insufficient on their own; retain scoped operating records, approvals, exceptions, and verified follow-up.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
