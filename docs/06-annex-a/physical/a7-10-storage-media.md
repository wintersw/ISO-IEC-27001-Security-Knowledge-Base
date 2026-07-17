---
title: A.7.10 Storage media
description: Practical implementation, evidence, and audit guidance for A.7.10.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.7.10 Storage media

## Overview

Storage media can retain sensitive information long after normal use. Its acquisition, inventory, handling, transport, encryption, reuse, and disposal should follow classification and legal or business retention needs.

## Purpose

This control manages storage media throughout its lifecycle — from acquisition and inventory through handling, transport, encryption, reuse, and disposal — to prevent unauthorized access, loss, or leakage of the information it contains.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.7.10 when selected or otherwise committed to.
- **Implementation guidance:** Define **storage media** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

Encrypted backup drives are inventoried, transferred in tamper-evident packaging, stored with restricted access, and reconciled on return. A failed drive is destroyed through an approved service with a disposal certificate.

## Evidence to retain

- site risk assessment
- access records
- visitor records
- inspection or maintenance records
- incident and corrective-action records

## Common mistakes

- Treating all media identically regardless of what is stored on it — no classification-based handling procedures
- Sending failed drives for repair or disposal without first sanitizing or destroying the data they contain
- Not maintaining a media inventory — losing track of which media exist, where they are, and what they hold
- Using consumer-grade encryption or no encryption at all for backup media in transit or off-site storage

## Auditor questions

- How do you track storage media from acquisition through disposal?
- What sanitization or destruction method is used before media leaves your control?
- How is media protected during transport between sites or to off-site storage?
- Can you show the media inventory and when it was last reconciled?

## Checklist

- [ ] Storage media inventory maintained with classification, location, and custodian
- [ ] Handling procedures defined by media classification and content sensitivity
- [ ] Encryption applied to media in transit and at rest where risk-appropriate
- [ ] Sanitization or destruction verified before disposal, reuse, or third-party repair
- [ ] Media inventory reconciled periodically and discrepancies investigated

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
