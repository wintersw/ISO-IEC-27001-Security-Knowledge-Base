---
title: A.5.13 Labelling of information
description: Practical implementation, evidence, and audit guidance for A.5.13.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.5.13 Labelling of information

## Overview

Labels make classification and handling expectations visible to people and systems. The label format and placement should work across documents, messages, records, exports, and physical media without exposing unnecessary sensitive detail.

## Purpose

This control ensures that information is labelled according to its classification so that handlers can immediately recognize the required protection level. Labels that are missing, inconsistent, or ignored make classification a theoretical exercise with no practical effect.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.5.13 when selected or otherwise committed to.
- **Implementation guidance:** Define **labelling of information** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

Confidential reports receive a document marking and repository metadata. An email rule warns before external transmission, while a public document is deliberately marked for unrestricted distribution to prevent unnecessary handling barriers.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- Labelling requirements exist in policy but are not enforced — documents circulate without any visible classification marking.
- Digital labelling is considered optional — email, chat messages, and cloud documents are excluded from labelling scope.
- Labels are applied inconsistently — the same type of information carries different labels depending on who created it.
- Physical and digital labelling rules are not aligned — a document printed from a "Confidential" system carries no marking.

## Auditor questions

- How is information labelled — manually, automatically, or both?
- What labelling rules apply to email, chat, and collaborative platforms?
- How are labelling errors or omissions detected and corrected?
- Show examples of correctly labelled information across different media (document, email, printed output).

## Checklist

- [ ] labelling requirements defined per classification level
- [ ] labelling applied to physical and digital information
- [ ] email and collaboration platforms included in labelling scope
- [ ] automated labelling configured where feasible
- [ ] labelling accuracy spot-checked periodically
- [ ] labelling guidance and training provided to personnel

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
