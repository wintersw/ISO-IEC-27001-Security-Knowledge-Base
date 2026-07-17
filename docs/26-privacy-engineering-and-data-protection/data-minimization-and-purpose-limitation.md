---
title: Data Minimization and Purpose Limitation
description: How to reduce risk by limiting collection, use, retention, and sharing.
category: Privacy Engineering and Data Protection
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - data-minimization
  - privacy
---

# Data Minimization and Purpose Limitation

Data minimization reduces exposure by collecting, storing, and using only what is necessary for a defined purpose.

## Implementation patterns

- remove unnecessary fields
- shorten retention
- aggregate where possible
- avoid production data in test
- mask data for support
- limit exports
- restrict privileged analytics access
- define allowed purposes
- review new secondary uses

## Purpose control

For each dataset, document:

- approved purpose
- prohibited purposes
- owner
- users
- systems
- retention
- sharing rules
- monitoring requirements

## Typical evidence

- documented approved and prohibited purposes per dataset
- records of removed or rejected data fields from collection forms and APIs
- retention schedule with shortened periods and deletion confirmation
- approvals for any new secondary use of an existing dataset
- masking or aggregation configuration for support and analytics access

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

A signup form asks for date of birth, full address, and phone number, but the service only needs an email and country. The team removes the unneeded fields, sets a 24-month inactive-account deletion rule, and documents "service delivery and billing" as the only approved purposes — so a later request to reuse the data for advertising triggers a formal secondary-use review instead of silent repurposing.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
