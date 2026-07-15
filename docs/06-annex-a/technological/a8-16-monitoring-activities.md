---
title: A.8.16 Monitoring activities
description: Practical implementation, evidence, and audit guidance for A.8.16.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.16 Monitoring activities

## Overview

Monitoring activities observe systems, networks, applications, users, and control states so abnormal behavior and failures can be detected and investigated. Useful monitoring has defined coverage, ownership, thresholds, response, retention, and review.

## Purpose

The purpose of A.8.16 is to reduce the likelihood or impact of failures related to **monitoring activities**. A well-designed control makes the expected outcome, accountability, operating trigger, exception path, and assurance method clear enough to be repeated and tested.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.16 when selected or otherwise committed to.
- **Implementation guidance:** Define **monitoring activities** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

This control creates visibility into security-relevant activity. Logs and alerts should be designed around investigation and risk scenarios, protected from tampering, retained appropriately, and reviewed through defined workflows.

### Measures that support decisions

- critical systems with required logging
- alerts triaged within target
- log-source failures
- use cases tested

## Practical example

A monitoring use case alerts on impossible travel followed by privileged access. The analyst checks identity, device, and application context, records disposition, and the owner reviews detection coverage and false results each month.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
