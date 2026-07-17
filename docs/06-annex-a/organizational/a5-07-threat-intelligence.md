---
title: A.5.7 Threat intelligence
description: Practical implementation, evidence, and audit guidance for A.5.7.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.5.7 Threat intelligence

## Overview

Threat intelligence turns information about attackers, methods, vulnerabilities, and targets into decisions relevant to the organization. Collection alone is not enough; sources need evaluation, analysis, distribution, and action.

## Purpose

This control ensures that the organization collects, analyzes, and uses threat intelligence relevant to its context — industry, geography, technology, and threat actors. Threat intelligence that is collected but never operationalized is just noise; it must drive decisions about monitoring, defenses, and risk treatment.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.5.7 when selected or otherwise committed to.
- **Implementation guidance:** Define **threat intelligence** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

A trusted alert reports exploitation of a component used in the public portal. The team confirms exposure from the asset inventory, increases monitoring, accelerates remediation, and records why unrelated systems were excluded.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- Threat feeds are subscribed to but not filtered for relevance — every alert is treated equally, causing alert fatigue.
- Intelligence is consumed but not correlated with the organization's asset inventory — no one checks whether the threat applies.
- Actionable intelligence is not routed to the right teams — the SOC receives it but patching and config teams do not.
- Threat intelligence is treated as a purely technical function — business context (mergers, geopolitics, new products) is ignored.

## Auditor questions

- What threat intelligence sources are used, and how are they selected and evaluated?
- How is threat intelligence analyzed and turned into actionable decisions?
- How is intelligence correlated with the organization's asset inventory and risk profile?
- Show a recent example where threat intelligence led to a change in controls or monitoring.

## Checklist

- [ ] threat intelligence sources identified and evaluated
- [ ] intelligence analysis and triage process defined
- [ ] intelligence correlated with asset inventory
- [ ] actionable intelligence routed to responsible teams
- [ ] intelligence-driven control improvements tracked
- [ ] intelligence programme reviewed for effectiveness

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
