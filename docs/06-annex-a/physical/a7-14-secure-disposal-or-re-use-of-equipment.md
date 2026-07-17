---
title: A.7.14 Secure disposal or re-use of equipment
description: Practical implementation, evidence, and audit guidance for A.7.14.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.7.14 Secure disposal or re-use of equipment

## Overview

Equipment intended for disposal or reuse may still contain information, credentials, configuration, licenses, or labels. The organization should verify sanitization or destruction before release and retain traceable evidence.

## Purpose

This control ensures that equipment containing storage media is sanitized or destroyed before disposal or reuse, so that no residual information, credentials, licenses, or configuration data can be recovered by unauthorized parties.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.7.14 when selected or otherwise committed to.
- **Implementation guidance:** Define **secure disposal or re-use of equipment** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

Retired laptops are reconciled to the asset register, cryptographic keys are revoked, storage is sanitized using an approved method, random results are verified, labels are removed, and the disposal provider's certificate is retained.

## Evidence to retain

- site risk assessment
- access records
- visitor records
- inspection or maintenance records
- incident and corrective-action records

## Common mistakes

- Deleting files or formatting drives and assuming that is sufficient — without using verified sanitization methods
- Disposing of equipment through general waste channels without a controlled and documented disposal chain
- Forgetting to remove or destroy labels, asset tags, and configuration details that reveal organizational information
- Not retaining disposal certificates or sanitization verification records, leaving no audit trail

## Auditor questions

- What sanitization method do you use, and how do you verify it was effective?
- How do you ensure equipment is not disposed of through uncontrolled channels?
- Can you show disposal certificates or sanitization records for equipment retired in the last period?
- How are labels, asset tags, and embedded configuration details removed before disposal?

## Checklist

- [ ] Sanitization method defined and matched to media type and information sensitivity
- [ ] Verification step included after sanitization to confirm data is irrecoverable
- [ ] Disposal chain documented — from decommissioning through final destruction or reuse
- [ ] Labels, asset tags, and configuration identifiers removed before release
- [ ] Disposal certificates or sanitization records retained as evidence

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
