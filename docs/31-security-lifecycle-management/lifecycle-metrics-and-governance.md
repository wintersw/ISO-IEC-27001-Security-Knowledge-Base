---
title: Lifecycle Metrics and Governance
description: How to measure lifecycle health and report it to management.
category: Security Lifecycle Management
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - security-lifecycle
  - isms
---

# Lifecycle Metrics and Governance

Lifecycle management should be visible to governance forums. Management does not need every operational detail, but it does need trend information, decision points, resource constraints, and high-risk exceptions.

## Example lifecycle metrics

| Lifecycle | Metric | Why it matters |
|---|---|---|
| asset/data | critical assets without owner | weak accountability |
| risk | overdue high-risk treatment actions | unmanaged exposure |
| access | movers not reviewed within target | excessive access risk |
| vulnerability | critical vulnerabilities overdue | exploitable exposure |
| supplier | high-risk suppliers overdue for review | third-party risk |
| change | high-risk changes without security review | security drift |
| incident | lessons learned not closed | weak improvement |
| evidence | controls without current evidence | audit and assurance gap |

## Best practices

- Separate key performance indicator (KPI), key risk indicator (KRI), and key control indicator (KCI) measures.
- Use thresholds that trigger decisions.
- Report trends rather than isolated numbers.
- Link metrics to risk appetite.
- Include resource constraints and blocked actions.
- Use management review to approve priorities and risk acceptance.

## Related chapters

- [information security management system (ISMS) Health Dashboard](../19-isms-professional-toolkit/isms-health-dashboard.md)
- [Metrics Library](../19-isms-professional-toolkit/metrics-library.md)
- [Continual Improvement Metrics](../23-continual-improvement/continual-improvement-metrics.md)


## Practical example

A quarterly governance report shows two amber trends: 14 movers were not re-reviewed within target and eight high-risk suppliers are overdue for review. Because thresholds were defined in advance, the amber status triggers decisions rather than discussion: management assigns temporary review capacity, formally accepts a 30-day delay for two low-exposure suppliers, and records both decisions — demonstrating metrics that drive action instead of dashboards that are merely admired.

## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- metric definitions with thresholds, owners, and data sources
- trend reports presented to governance forums
- management decisions triggered by threshold breaches
- risk acceptance records for tolerated metric deviations


## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
