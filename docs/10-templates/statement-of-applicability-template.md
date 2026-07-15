---
title: Statement of Applicability Template
description: Tried-and-tested ISMS template: Statement of Applicability Template.
category: Templates
difficulty: Beginner
applies_to:
  - ISO/IEC 27001:2022
tags:
  - template
  - isms-documentation
  - iso27001
---

# Statement of Applicability Template

> The status summary and chart pattern are based in part on the SoA workbook in the [ISO 27001:2022 Toolkit](https://github.com/PehanIn/ISO-27001-2022-Toolkit), copyright (c) 2024 Pehan Gunasekara, MIT License. Status definitions and reporting rules have been simplified and corrected for this project.

| Field | Content |
|---|---|
| Organization | [Organization name] |
| information security management system (ISMS) scope | [Scope reference] |
| Version | [Version] |
| Owner | [ISMS manager] |
| Approved by | [Top management / risk committee] |
| Approval date | [Date] |

## 1. Purpose

The Statement of Applicability identifies which Annex A controls are applicable, why they are included or excluded, their implementation status, and references to supporting evidence.

## 2. Control applicability table

| Control ID | Control name | Applicable? | Justification for inclusion/exclusion | Implementation status | Control owner | Related risks | Evidence / document reference |
|---|---|---|---|---|---|---|---|
| A.5.1 | Policies for information security | Yes | Required for ISMS governance | Implemented / Partial / Planned / Not implemented |  |  |  |
| A.5.2 | Information security roles and responsibilities | Yes | Required for accountability |  |  |  |  |
| A.5.3 | Segregation of duties |  |  |  |  |  |  |
| A.5.4 | Management responsibilities |  |  |  |  |  |  |
| A.5.5 | Contact with authorities |  |  |  |  |  |  |
| A.5.6 | Contact with special interest groups |  |  |  |  |  |  |
| A.5.7 | Threat intelligence |  |  |  |  |  |  |
| A.5.8 | Information security in project management |  |  |  |  |  |  |
| A.5.9 | Inventory of information and other associated assets |  |  |  |  |  |  |
| A.5.10 | Acceptable use of information and other associated assets |  |  |  |  |  |  |
| A.5.15 | Access control |  |  |  |  |  |  |
| A.5.16 | Identity management |  |  |  |  |  |  |
| A.5.19 | Information security in supplier relationships |  |  |  |  |  |  |
| A.5.23 | Information security for use of cloud services |  |  |  |  |  |  |
| A.5.24 | Information security incident management planning and preparation |  |  |  |  |  |  |
| A.5.30 | information and communication technology (ICT) readiness for business continuity |  |  |  |  |  |  |
| A.6.3 | Information security awareness, education and training |  |  |  |  |  |  |
| A.7.1 | Physical security perimeters |  |  |  |  |  |  |
| A.8.1 | User endpoint devices |  |  |  |  |  |  |
| A.8.2 | Privileged access rights |  |  |  |  |  |  |
| A.8.8 | Management of technical vulnerabilities |  |  |  |  |  |  |
| A.8.9 | Configuration management |  |  |  |  |  |  |
| A.8.15 | Logging |  |  |  |  |  |  |
| A.8.16 | Monitoring activities |  |  |  |  |  |  |
| A.8.24 | Use of cryptography |  |  |  |  |  |  |
| A.8.25 | Secure development life cycle |  |  |  |  |  |  |
| A.8.28 | Secure coding |  |  |  |  |  |  |
| A.8.32 | Change management |  |  |  |  |  |  |
| A.8.34 | Protection of information systems during audit testing |  |  |  |  |  |  |

## 3. Exclusion rules

Controls may be excluded only when:

- there is a documented justification
- exclusion does not invalidate risk treatment
- exclusion is approved
- exclusion is reviewed when context changes

## Implementation-status definitions

| Status | Definition | Minimum evidence expectation |
|---|---|---|
| Not started | Applicable control has no approved implementation activity | approved gap and assigned action |
| Planned | Implementation is approved, owned, and scheduled but not yet operating | plan, owner, resources, due date |
| Partially implemented | Some required scope or control components operate, but material gaps remain | operating evidence plus documented gaps |
| Implemented | Control design is deployed across the intended scope | current implementation and operating evidence |
| Effective | Testing or performance evidence supports that the control achieves its intended outcome | test results, metrics, exceptions, conclusion |
| Not applicable | Applicability decision is justified and approved | exclusion rationale linked to risk and requirements |

Do not equate “implemented” with “effective.” Keep `Not applicable` separate from implementation progress because it is an applicability decision, not a maturity level.

## Status summary

| Status | Count | Percentage of applicable controls |
|---|---:|---:|
| Not started |  |  |
| Planned |  |  |
| Partially implemented |  |  |
| Implemented |  |  |
| Effective |  |  |

The percentages should use applicable controls as the denominator. Report not-applicable controls separately and reconcile the total with all 93 Annex A controls.

### Example status chart

The following values are illustrative only. Replace them with counts calculated from the approved SoA.

```mermaid
pie showData
    title Example distribution of applicable-control status
    "Not started" : 5
    "Planned" : 12
    "Partially implemented" : 18
    "Implemented" : 38
    "Effective" : 14
```

## 4. Review triggers

Review the SoA when:

- risk assessment changes
- scope changes
- new controls are implemented
- audit findings identify inaccuracies
- incidents reveal control gaps
- legal or contractual requirements change

## Approval

| Role | Name | Date | Approval |
|---|---|---|---|
| ISMS manager |  |  |  |
| Risk owner / management |  |  |  |

## Usage guidance

Use this template to document **Statement of Applicability**. The owner defines its trigger and scope, uses authoritative sources, routes required approval, and tracks open items. Adapt the fields; this is guidance, not required ISO wording.

## Evidence to retain

Retain the approved record, source evidence, approval history, exceptions, and follow-up actions under the organization's retention and protection rules.

## Practical example

For one in-scope service, the owner completes the **Statement of Applicability** record, links authoritative evidence, obtains review, and tracks rejected or incomplete items to closure.

## ISO requirement, implementation guidance, and best practice

This exact template is not an ISO requirement; it is guidance for recording **Statement of Applicability** consistently. Controlled values, named owners, timestamps, approvals, and authoritative evidence improve assurance.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
