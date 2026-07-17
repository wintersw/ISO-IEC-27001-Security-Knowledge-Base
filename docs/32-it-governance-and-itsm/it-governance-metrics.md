---
title: IT Governance Metrics for the ISMS
description: Metrics that show whether IT governance and ITSM processes support security outcomes.
category: IT Governance and ITSM
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - it-governance
  - itsm
  - isms
---

# IT Governance Metrics for the ISMS
Metrics should show whether IT governance and information technology service management (ITSM) processes support security objectives.

## Suggested metrics

| Metric | Type | Meaning |
|---|---|---|
| high-risk changes without security review | key risk indicator (KRI) | change governance weakness |
| emergency changes with post-review completed | key performance indicator (KPI) | control over urgent changes |
| critical services with current owner | KPI | accountability |
| critical services without tested recovery | KRI | availability exposure |
| security incidents linked to problem records | KPI | learning maturity |
| known errors with open security risk | KRI | unresolved systemic weakness |
| configuration management database (CMDB) assets without owner | KRI | asset governance gap |
| suppliers supporting critical services overdue for review | KRI | third-party risk |
| management decisions overdue | key control indicator (KCI) | governance control weakness |

## Best practices

- Report metrics by service criticality.
- Use trends, not isolated snapshots.
- Include exceptions and overdue management decisions.
- Link metrics to risk appetite and management review.


## Practical example

The quarterly governance dashboard shows that emergency changes have doubled and post-review completion has dropped below 60%. The chief information security officer (CISO) raises this at the IT governance forum. Investigation reveals inadequate change-planning capacity during a major platform migration. Governance directs additional resources, requires pre-approved change templates, and sets a review target of 90% within 30 days.

## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- service or configuration record
- risk, approval, and segregation-of-duties evidence
- test and implementation logs
- post-implementation review and follow-up actions


## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
