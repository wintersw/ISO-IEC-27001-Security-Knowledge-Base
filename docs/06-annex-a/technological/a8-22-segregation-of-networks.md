---
title: A.8.22 Segregation of networks
description: Practical implementation, evidence, and audit guidance for A.8.22.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.22 Segregation of networks

## Overview

Network segregation limits unnecessary communication and reduces the spread and impact of compromise. Zones and flows should follow business purpose, sensitivity, identity, device trust, and administration needs, with controlled exceptions.

## Purpose

The purpose of A.8.22 is to reduce the likelihood or impact of failures related to **segregation of networks**. A well-designed control makes the expected outcome, accountability, operating trigger, exception path, and assurance method clear enough to be repeated and tested.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.22 when selected or otherwise committed to.
- **Implementation guidance:** Define **segregation of networks** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

Development, production, user, guest, and management networks use separate policies. Only documented service flows are permitted, administrative access uses a controlled path, and rule reviews remove obsolete connections.

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
