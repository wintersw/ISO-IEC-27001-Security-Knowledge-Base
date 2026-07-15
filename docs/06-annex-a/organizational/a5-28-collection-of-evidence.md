---
title: A.5.28 Collection of evidence
description: Practical implementation, evidence, and audit guidance for A.5.28.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.5.28 Collection of evidence

## Overview

Evidence collection must preserve relevance, integrity, traceability, and lawful handling so records can support investigation, disciplinary action, legal proceedings, or improvement. Collection should follow a prepared and repeatable method.

## Purpose

The purpose of A.5.28 is to reduce the likelihood or impact of failures related to **collection of evidence**. A well-designed control makes the expected outcome, accountability, operating trigger, exception path, and assurance method clear enough to be repeated and tested.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.5.28 when selected or otherwise committed to.
- **Implementation guidance:** Define **collection of evidence** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

An investigator exports relevant logs, records source and time, calculates an integrity hash, stores the original read-only, documents every transfer, and works from a controlled copy during analysis.

## Evidence to retain

- incident ticket and timeline
- severity and escalation decision
- preserved logs and artifacts
- communication and notification record
- lessons learned and corrective actions

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
