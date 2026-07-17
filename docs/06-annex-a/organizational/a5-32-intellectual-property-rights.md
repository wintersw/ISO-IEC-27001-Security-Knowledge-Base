---
title: A.5.32 Intellectual property rights
description: Practical implementation, evidence, and audit guidance for A.5.32.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.5.32 Intellectual property rights

## Overview

Intellectual-property controls protect both the organization's rights and the rights of others. They address licenses, ownership, permitted use, copying, source material, third-party content, and disposal.

## Purpose

This control ensures that the organization protects its own intellectual property and respects the IP rights of others — including software licenses, copyright, trademarks, and trade secrets. IP infringement, even unintentional, can result in litigation, financial penalties, and reputational damage.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.5.32 when selected or otherwise committed to.
- **Implementation guidance:** Define **intellectual property rights** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

A development team approves open-source dependencies through a process that records license obligations and source. Build checks flag an unapproved component before release, and the resolution is retained with the product record.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- Open-source license obligations are not tracked — copyleft licenses infect proprietary code because usage conditions were ignored.
- Employees use unlicensed or personally-owned software for business purposes without review.
- IP ownership is not addressed in employment contracts or supplier agreements — the organization does not own work it paid for.
- Third-party content (images, fonts, code snippets) is used without verifying license terms.

## Auditor questions

- How does the organization identify and comply with software license obligations?
- How is IP ownership addressed in employment and supplier contracts?
- How are open-source components tracked and their license obligations managed?
- Show evidence that IP compliance is checked before software or content is released.

## Checklist

- [ ] IP policy documented and communicated
- [ ] software license inventory maintained
- [ ] open-source license obligations tracked
- [ ] IP ownership clauses in employment and supplier contracts
- [ ] third-party content license verification process
- [ ] IP compliance reviewed before product release

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
