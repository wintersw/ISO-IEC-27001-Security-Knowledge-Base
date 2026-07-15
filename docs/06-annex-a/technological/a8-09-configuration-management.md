---
title: A.8.9 Configuration management
description: Practical implementation, evidence, and audit guidance for A.8.9.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.9 Configuration management

## Overview

Configuration management defines, approves, records, monitors, and changes secure settings for systems and services. Baselines should be appropriate to asset purpose and make unauthorized or accidental drift visible.

## Purpose

The purpose of A.8.9 is to reduce the likelihood or impact of failures related to **configuration management**. A well-designed control makes the expected outcome, accountability, operating trigger, exception path, and assurance method clear enough to be repeated and tested.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.9 when selected or otherwise committed to.
- **Implementation guidance:** Define **configuration management** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

A cloud service baseline requires approved identity, logging, encryption, and network settings. Automated checks identify a disabled log source, create a ticket, and verify restoration while an authorized temporary deviation follows the exception process.

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
