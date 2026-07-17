---
title: ISMS Process Architecture
description: How policies, processes, procedures, work instructions, and records fit together.
category: PDF Source Integration
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - source-integration
  - isms
  - iso27001
---

# ISMS Process Architecture
The uploaded process-management material strongly reinforces the relationship between policies, processes, procedures, and records.

## Architecture layers

| Layer | Purpose | Example |
|---|---|---|
| Policy | Defines management intent and rules | Information Security Policy |
| Process | Defines flow, roles, inputs, outputs, and interfaces | Access Review Process |
| Procedure | Defines step-by-step execution | How to perform quarterly access review |
| Work instruction | Provides detailed task guidance | Export identity and access management (IAM) report from system |
| Record | Proves the work occurred | Signed access review report |

## Why process architecture matters

Without process documentation:

- knowledge remains informal
- new staff struggle to perform tasks
- responsibilities are unclear
- errors are hard to trace
- process continuity depends on individuals
- audits become difficult
- improvement is inconsistent

## Minimum process description

Each ISMS process should define:

- purpose
- trigger
- input
- output
- process owner
- participating roles
- activities
- decision points
- interfaces
- evidence
- KPIs/KRIs/KCIs
- exceptions
- review frequency

## Process interface examples

| Process | Interfaces |
|---|---|
| Risk management | change management, incident management, vulnerability management |
| Access management | HR, asset management, IAM, line management |
| Backup management | business continuity, change management, incident response |
| Supplier security | procurement, legal, privacy, business owners |
| Incident management | legal, privacy, communications, IT operations, suppliers |

## Related templates

- [ISMS Process Description Template](../10-templates/isms-process-description-template.md)
- [ISMS Process Catalog Template](../10-templates/isms-process-catalog-template.md)
- [Process Interface Agreement Template](../10-templates/process-interface-agreement-template.md)


## Practical example

An internal audit finds that quarterly access reviews depend entirely on one administrator who "knows how it's done." Applying the architecture layers, the team writes the missing pieces: the Access Control Policy already states the rule, so they add a process description (owner, trigger, inputs, outputs, interfaces to HR), a procedure with the review steps, and a work instruction for exporting the IAM report. When the administrator leaves three months later, a colleague performs the review from the documentation alone, and the signed review report provides the record layer.

## Evidence to retain

Retain artifacts from each architecture layer, such as:

- process descriptions with owner, trigger, inputs, outputs, and interfaces
- procedures and work instructions kept in the document register
- records proving each documented process actually ran
- review results showing process documentation stays current


## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
