---
title: Incident Response Lifecycle
description: Lifecycle from discovery through recovery and lessons learned.
category: Incident and Data Breach Management
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - incident-response
---

# Incident Response Lifecycle

## Stages

1. prepare
2. detect
3. triage
4. classify
5. contain
6. eradicate
7. recover
8. communicate
9. preserve evidence
10. document
11. learn and improve

## Readiness requirements

- incident roles
- contact list
- severity model
- escalation paths
- legal and privacy contacts
- forensic support
- logging coverage
- communication templates
- tabletop exercises
- supplier notification paths

## Typical evidence

- incident response plan with roles, severity model, and escalation paths
- incident tickets showing lifecycle stages from detection to closure
- containment, eradication, and recovery action records
- communication logs and preserved evidence per incident
- tabletop exercise results and lessons-learned records

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)
- [Incident Response](../07-security-domains/incident-response.md)
- [ISO/IEC 27035 Incident Management](../03-iso27001/iso27035-incident-management.md)


## Practical example

A ransomware alert on a file server triggers the lifecycle: the on-call analyst triages and classifies it as high severity, isolates the server (contain), removes the malware and patches the entry point (eradicate), restores from clean backups (recover), and briefs management (communicate). Logs are preserved before the server is rebuilt, and the lessons-learned review adds an EDR rule that would have caught the initial dropper.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
