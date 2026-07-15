---
title: Service Catalogue Security
description: How service catalogue records support ownership, classification, resilience, and ISMS scope.
category: IT Governance and ITSM
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - it-governance
  - itsm
  - cobit
  - itil
---

# Service Catalogue Security

A service catalogue describes live services in language meaningful to customers and service owners. Security-relevant fields turn it into a governance and assurance tool.

## Recommended security fields

- service owner
- business purpose
- customer/user groups
- criticality
- data classification
- availability target
- recovery objectives
- identity and access model
- monitoring and incident escalation
- major suppliers
- regulatory or contractual obligations
- support period
- planned retirement

## Example

The “Customer Support Portal” catalogue entry records that it processes confidential customer ticket data, depends on the identity provider and software as a service (SaaS) vendor, has an recovery time objective (RTO) of four hours, and requires 24-hour customer incident notification.

This helps incident responders assess impact, vulnerability teams prioritize findings, and auditors understand scope.

## Best practices

- Keep service records understandable to business owners.
- Link services to configuration items rather than duplicating technical inventory.
- Review catalogue entries after major change.
- Use criticality to drive recovery and monitoring.
- Treat missing service ownership as a governance issue.


## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- service or configuration record
- risk, approval, and segregation-of-duties evidence
- test and implementation logs
- post-implementation review and follow-up actions

Intent documents are insufficient on their own; retain scoped operating records, approvals, exceptions, and verified follow-up.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
