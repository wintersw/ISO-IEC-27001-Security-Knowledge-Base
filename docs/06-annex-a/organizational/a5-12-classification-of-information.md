---
title: A.5.12 Classification of information
description: Practical implementation, evidence, and audit guidance for A.5.12.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.5.12 Classification of information

## Overview

Information classification groups information by the protection it needs. Criteria should reflect confidentiality, integrity, availability, legal duties, business value, aggregation, and the harm caused by disclosure, change, or loss.

## Purpose

This control ensures that information is classified according to its sensitivity, value, and criticality so that appropriate protection levels can be applied. Classification is the foundation for access control, encryption, handling rules, and retention — without it, all information tends to be treated the same.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.5.12 when selected or otherwise committed to.
- **Implementation guidance:** Define **classification of information** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

A data owner classifies customer support tickets as confidential because they may contain personal and contract information, defines approved storage and sharing rules, and schedules review when the ticketing process changes.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- Classification scheme exists on paper but is never applied to actual data — everything defaults to "unclassified."
- Too many classification levels are defined — users cannot distinguish between them and default to the middle.
- Classification focuses only on confidentiality — integrity and availability requirements are ignored.
- Information owners are not assigned — no one is accountable for classifying the data they create or manage.

## Auditor questions

- What classification scheme is in use, and how are the levels defined?
- How are information owners assigned, and what training do they receive on classification?
- How is classification enforced — through labeling, access controls, or automated tools?
- Show evidence that classification decisions are reviewed when information changes hands or purpose.

## Checklist

- [ ] classification scheme defined and documented
- [ ] levels cover confidentiality, integrity, and availability
- [ ] information owners assigned and trained
- [ ] classification applied to information assets
- [ ] handling rules defined per classification level
- [ ] classification reviewed periodically and on change

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
