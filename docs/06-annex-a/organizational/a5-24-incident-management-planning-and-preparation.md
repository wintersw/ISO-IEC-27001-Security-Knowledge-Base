---
title: A.5.24 Incident management planning and preparation
description: Practical implementation, evidence, and audit guidance for A.5.24.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.5.24 Incident management planning and preparation

## Overview

Incident preparation establishes roles, plans, playbooks, communication paths, tools, evidence handling, and exercises before a real event. Preparation should reflect likely scenarios and dependencies rather than a generic contact list.

## Purpose

This control ensures that the organization prepares for security incidents by defining appropriate roles, plans, communication paths, tools, decision authority, and exercises before a real crisis. Exercising relevant scenarios reveals gaps under controlled conditions and provides evidence that response arrangements are usable.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.5.24 when selected or otherwise committed to.
- **Implementation guidance:** Define **incident management planning and preparation** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

### Measures that support decisions

- mean time to triage
- mean time to contain
- incidents with lessons learned
- repeat incidents

## Practical example

A tabletop exercise simulates theft of a privileged cloud credential. Participants test escalation, containment authority, customer communication, evidence preservation, supplier coordination, and out-of-hours access, then update the playbook.

## Evidence to retain

- incident ticket and timeline
- severity and escalation decision
- preserved logs and artifacts
- communication and notification record
- lessons learned and corrective actions

## Common mistakes

- An incident response plan exists but is generic — no playbooks for specific scenarios like ransomware, data breach, or insider threat.
- Contact lists in the plan are outdated — key people have left or changed roles.
- Exercises are not conducted — the plan has never been tested under realistic conditions.
- External parties (suppliers, legal counsel, PR, authorities) are not included in preparation or exercises.

## Auditor questions

- What incident response plans and playbooks exist, and when were they last updated?
- How are incident response roles assigned, and how is 24/7 coverage ensured?
- When was the last incident response exercise, and what improvements were identified?
- Show evidence that exercise findings resulted in updates to plans or controls.

## Checklist

- [ ] incident response plan documented and approved
- [ ] scenario-specific playbooks developed
- [ ] incident response roles assigned and trained
- [ ] contact lists maintained and verified
- [ ] exercises conducted and lessons applied
- [ ] external party coordination included in planning

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
