---
title: A.8.17 Clock synchronization
description: Practical implementation, evidence, and audit guidance for A.8.17.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.17 Clock synchronization

## Overview

Consistent time lets records from different systems be ordered and correlated. Systems should use approved, trustworthy time sources, monitor synchronization health, protect settings, and account for time zones and known offsets.

## Purpose

The purpose of A.8.17 is to reduce the likelihood or impact of failures related to **clock synchronization**. A well-designed control makes the expected outcome, accountability, operating trigger, exception path, and assurance method clear enough to be repeated and tested.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.17 when selected or otherwise committed to.
- **Implementation guidance:** Define **clock synchronization** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

This control creates visibility into security-relevant activity. Logs and alerts should be designed around investigation and risk scenarios, protected from tampering, retained appropriately, and reviewed through defined workflows.

## Practical example

Servers and security tools synchronize to approved redundant time sources. Monitoring detects excessive drift, changes require privilege and logging, and incident records retain coordinated universal time with local display conversion.

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
