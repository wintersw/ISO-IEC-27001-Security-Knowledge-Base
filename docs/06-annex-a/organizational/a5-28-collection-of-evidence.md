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

This control ensures that evidence related to security events, incidents, and investigations is collected, handled, and preserved in a way that supports integrity, traceability, and the evidential requirements of the intended proceeding. Requirements for admissibility and handling depend on the jurisdiction and purpose, so legal or specialist advice may be needed.

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

## Common mistakes

- Logs and artifacts are collected but not protected from modification — anyone with access can alter evidence after collection.
- Chain of custody is not documented — there is no record of who handled evidence, when, and why.
- Evidence is collected by personnel who are not trained for the relevant evidence type, investigation purpose, or applicable handling requirements.
- Only inculpatory evidence is preserved — exculpatory evidence that might clear someone is ignored or discarded.

## Auditor questions

- What procedures govern evidence collection, handling, and preservation?
- How is chain of custody documented and maintained?
- Who is authorized and trained to collect evidence?
- Show evidence of a recent investigation where evidence was collected and preserved according to procedure.

## Checklist

- [ ] evidence collection and handling procedure documented
- [ ] personnel trained on evidence collection
- [ ] chain of custody forms/templates available
- [ ] evidence storage secured against tampering
- [ ] integrity verification (hashing) performed at collection
- [ ] legal and regulatory requirements for evidence identified

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
