---
title: A.8.6 Capacity management
description: Practical implementation, evidence, and audit guidance for A.8.6.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.6 Capacity management

## Overview

Capacity management keeps services within acceptable performance and resilience limits as demand, data, and dependencies change. Forecasting, thresholds, monitoring, scaling, and corrective action should focus on business-critical constraints.

## Purpose

This control ensures that information processing facilities, storage, and supporting services have sufficient capacity to meet availability requirements, including under projected growth and peak loads. Capacity shortfalls degrade performance, cause outages, and can prevent security controls from functioning.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.6 when selected or otherwise committed to.
- **Implementation guidance:** Define **capacity management** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

A transaction service monitors compute, database connections, storage, queue depth, and supplier quotas. Forecasts trigger scaling before a seasonal peak, while a load test verifies the capacity and exposes one hidden dependency.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- Capacity is only reviewed after an outage — there is no proactive monitoring or trend analysis.
- Monitoring focuses on a single metric (e.g., CPU) while ignoring other constraints like disk I/O, network throughput, or database connections.
- Capacity forecasts do not account for seasonal peaks, new feature launches, or supplier-imposed quotas.
- Security tooling overhead (scanning, logging, encryption) is not factored into capacity planning.

## Auditor questions

- What capacity metrics are monitored, and what thresholds trigger alerts or scaling actions?
- How are capacity forecasts generated, and how far ahead do they project?
- When was the last capacity-related incident, and what corrective action was taken?
- Show evidence that capacity testing or load testing is performed for critical services.

## Checklist

- [ ] capacity metrics defined and monitored for critical services
- [ ] alert thresholds configured and tested
- [ ] capacity forecasts updated on a defined cadence
- [ ] load testing performed for critical services
- [ ] supplier capacity limits documented and tracked
- [ ] capacity incident and corrective action records retained

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
