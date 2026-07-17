---
title: Resource Economics and Central Solutions
description: How to make ISMS control decisions economically and avoid isolated overlapping solutions.
category: PDF Source Integration
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - source-integration
  - isms
  - iso27001
---

# Resource Economics and Central Solutions

The uploaded material reinforced that risk-oriented controls should also be economically appropriate.

## Key principle

Controls should be effective, proportionate, and sustainable. Complex or expensive controls should not be implemented in isolation from risk, context, and operating cost.

## Cost categories

| Cost type | Examples |
|---|---|
| Direct cost | tools, hardware, software, licenses, services |
| Operating cost | maintenance, monitoring, administration |
| People cost | training, control operation, reviews |
| Indirect cost | user friction, downtime, process delay |
| Opportunity cost | work displaced by security activity |

## Central solution decision logic

Centralized solutions may be preferable when they:

- reduce duplicate tooling
- improve consistency
- reduce manual effort
- improve monitoring
- improve reliability
- simplify evidence collection
- reduce total operating cost

Local solutions may be justified when:

- scope is specialized
- risk profile differs
- regulatory requirement is specific
- central service cannot meet the requirement
- local resilience is needed

## Decision questions

- Which risk does the control reduce?
- Is the control proportionate?
- What is the total cost of ownership?
- Can existing processes or tools be reused?
- Does the control create new operational risk?
- How will effectiveness be measured?
- What evidence will be generated?

## Related documents

- [Economic Use of Security Resources](../20-bsi-isms-enhancement/resource-economics.md)
- [information security management system (ISMS) Health Dashboard](../19-isms-professional-toolkit/isms-health-dashboard.md)
- [Improvement Prioritization](../23-continual-improvement/improvement-prioritization.md)


## Practical example

Three business units each request their own vulnerability scanner. Applying the central-solution decision logic, the security team compares one central scanning service against three local deployments across all cost categories: direct license cost is similar, but operating cost, duplicated administration effort, and inconsistent evidence collection clearly favor the central service. One unit with an isolated OT network keeps a local scanner because the central service cannot reach it — a documented exception based on the local-solution criteria, not a preference.

## Evidence to retain

Retain records showing control decisions were economically justified, such as:

- total-cost-of-ownership comparisons across the cost categories
- central-versus-local decisions with the criteria applied
- documented exceptions where local solutions were justified
- follow-up effectiveness and cost reviews of the chosen solution


## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
