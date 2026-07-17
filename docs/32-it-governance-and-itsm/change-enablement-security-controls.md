---
title: Change Enablement Security Controls
description: Security controls embedded in ITSM change enablement.
category: IT Governance and ITSM
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - it-governance
  - itsm
  - isms
---

# Change Enablement Security Controls

Change enablement is one of the strongest links between IT Service Management (ITSM) and ISO 27001.

## Security fields to add to change records

- affected service or asset
- data classification
- security impact
- privacy impact
- access-control impact
- logging/monitoring impact
- vulnerability impact
- supplier impact
- rollback plan
- security testing performed
- risk acceptance required?
- post-implementation review required?

## Example

A firewall rule change allowing partner application programming interface (API) access should include business justification, partner identity, data classification, allowed source/destination, expiration or review date, logging requirement, security approval, and rollback plan.

## Best practices

- Use standard changes for low-risk repeatable work.
- Require enhanced review for high-risk changes.
- Include emergency change review after the fact.
- Link change records to risk and incident records where appropriate.
- Sample changes during internal audit.


## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- service or configuration record
- risk, approval, and segregation-of-duties evidence
- test and implementation logs
- post-implementation review and follow-up actions


## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
