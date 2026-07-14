---
title: Governance, Risk, and Compliance Operating Model
description: GRC viewpoint for explaining how an ISMS supports business objectives.
category: PDF Source Integration
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - source-integration
  - isms
  - iso27001
---

# Governance, Risk, and Compliance Operating Model

A useful way to explain the ISMS to management is through three viewpoints: governance, risk, and compliance.

## Governance view

Governance connects the ISMS to business objectives.

Questions:

- What business objectives must information security support?
- Who makes decisions?
- What objectives and policies apply?
- What resources are needed?
- What reports does management receive?
- What decisions must be escalated?

## Risk view

Risk management determines which controls are necessary, proportionate, and effective.

Questions:

- Which information assets and business processes are critical?
- What threats and vulnerabilities affect them?
- What is the risk appetite?
- Which controls reduce risk?
- Which residual risks are accepted?
- How are risks monitored?

## Compliance view

Compliance ensures that internal, external, legal, regulatory, contractual, and standard requirements are identified and fulfilled.

Questions:

- Which obligations apply?
- Which controls and policies address them?
- What evidence proves compliance?
- How are changes in obligations detected?
- How are nonconformities handled?

## Operating model

```mermaid
flowchart TD
    A[Business Objectives] --> B[Governance]
    C[Threats and Risk Exposure] --> D[Risk Management]
    E[Legal, Regulatory and Contractual Obligations] --> F[Compliance]
    B --> G[Information Security Requirements]
    D --> G
    F --> G
    G --> H[Policies, Controls and Processes]
    H --> I[Monitoring, Evidence and Audit]
    I --> J[Management Review]
    J --> B
    J --> D
    J --> F
```

## Suggested GRC dashboard

| View | Metric | Example |
|---|---|---|
| Governance | objective achievement | percentage of security objectives on track |
| Governance | management decisions overdue | decisions older than threshold |
| Risk | high risks overdue for treatment | number of overdue high risks |
| Risk | control failures | failed control tests |
| Compliance | obligations reviewed | percentage reviewed on schedule |
| Compliance | audit findings overdue | open findings past due |

## Related documents

- [ISMS Health Dashboard](../19-isms-professional-toolkit/isms-health-dashboard.md)
- [Management Review Pack](../19-isms-professional-toolkit/management-review-pack.md)
- [Metrics Library](../19-isms-professional-toolkit/metrics-library.md)
