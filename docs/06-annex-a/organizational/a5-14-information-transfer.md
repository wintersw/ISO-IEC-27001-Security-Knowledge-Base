---
title: A.5.14 Information transfer
description: Practical implementation, evidence, and audit guidance for A.5.14.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.5.14 Information transfer

## Overview

Information transfer controls protect information while it moves within or outside the organization. Rules should address approved channels, recipients, authentication, encryption, agreements, logging, mistakes, and failed transfers.

## Purpose

This control ensures that information transferred within or outside the organization is protected according to its sensitivity, destination, and transfer risk. Safeguards can include approved channels, recipient verification, encryption, agreements, and useful transfer records; the combination should be selected for the context rather than applied as a universal checklist.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.5.14 when selected or otherwise committed to.
- **Implementation guidance:** Define **information transfer** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

A support team sends a customer export through an approved encrypted transfer service after verifying the recipient and authorization. The transfer record captures sender, recipient, file, time, expiry, and confirmation of receipt.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- Staff use personal email, messaging apps, or unapproved file-sharing services to transfer business information.
- Transfer rules exist only for external transfers — internal movement of sensitive data between systems is uncontrolled.
- Encryption is applied to the transfer channel but not to the information itself — data is exposed if the channel is compromised.
- Failed or misdirected transfers are not logged or investigated — information sent to the wrong recipient goes unnoticed.

## Auditor questions

- What are the approved channels for information transfer, and how are staff made aware of them?
- How is sensitive information protected during transfer — encryption, authentication, integrity verification?
- How are transfer mistakes (wrong recipient, wrong file) detected and handled?
- Show evidence that transfer rules are enforced and that violations are detected.

## Checklist

- [ ] approved transfer channels defined and communicated
- [ ] encryption required for sensitive information in transit
- [ ] recipient verification process defined
- [ ] transfer logging and monitoring in place
- [ ] transfer mistake handling procedure documented
- [ ] rules cover internal and external transfers

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
