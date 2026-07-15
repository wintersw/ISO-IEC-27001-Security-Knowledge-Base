---
title: A.8.24 Use of cryptography
description: Practical implementation, evidence, and audit guidance for A.8.24.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.24 Use of cryptography

## Overview

Cryptography protects confidentiality, integrity, authenticity, or proof of origin when selected and managed correctly. The organization needs rules for approved use, algorithms, protocols, keys, certificates, ownership, recovery, rotation, and retirement.

## Purpose

The purpose of A.8.24 is to reduce the likelihood or impact of failures related to **use of cryptography**. A well-designed control makes the expected outcome, accountability, operating trigger, exception path, and assurance method clear enough to be repeated and tested.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.24 when selected or otherwise committed to.
- **Implementation guidance:** Define **use of cryptography** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

Sensitive backups use approved encryption with keys stored separately under restricted roles. Key generation, rotation, recovery, use, and destruction are recorded, and a recovery exercise confirms data remains accessible to authorized staff.

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
