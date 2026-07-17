---
title: Evidence Preservation
description: Preserving logs, records, and artifacts during incidents and breaches.
category: Incident and Data Breach Management
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - evidence
  - forensics
---

# Evidence Preservation

Evidence preservation protects investigation integrity and supports legal, regulatory, disciplinary, insurance, and audit needs.

## Evidence examples

- authentication logs
- access logs
- application programming interface (API) logs
- endpoint detection and response (EDR) alerts
- security information and event management (SIEM) events
- cloud audit logs
- database audit trails
- network flow records
- email records
- screenshots
- forensic images
- ticket history
- communications
- management decisions

## Chain-of-custody fields

- evidence ID
- description
- source
- collector
- collection date/time
- hash or integrity check
- storage location
- access restrictions
- transfer history
- retention period

## Typical evidence

- preserved log and forensic artifacts with integrity hashes
- completed chain-of-custody records for each evidence item
- restricted-access evidence storage with transfer history
- evidence preservation procedure and collection checklists
- retention decisions covering legal hold requirements

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

After detecting unauthorized database access, the responder immediately exports authentication logs, database audit trails, and API gateway logs before their 30-day rotation deletes them, hashes each file, and records collector, time, and storage location in the chain-of-custody log. Months later, the intact chain of custody lets legal counsel use the logs in proceedings against the attacker — evidence collected without custody records would have been challengeable.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
