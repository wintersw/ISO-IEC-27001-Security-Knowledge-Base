---
title: Data Security Lifecycle
description: Lifecycle model for data collection, transfer, use, storage, sharing, retention, archival, and deletion.
category: Data Security Governance
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - data-security
  - lifecycle
---

# Data Security Lifecycle

A data security lifecycle defines how data is protected from creation or collection until deletion or archival.

## Lifecycle stages

| Stage | Security questions |
|---|---|
| Collection | Is collection lawful, necessary, and minimal? |
| Ingestion | Is source authenticity verified? |
| Classification | Is sensitivity known and labeled? |
| Storage | Is storage authorized, encrypted, backed up, and monitored? |
| Use | Are access, purpose, and processing controlled? |
| Sharing | Are transfers approved, protected, logged, and contractually controlled? |
| Analytics | Is privacy, inference, aggregation, and re-identification risk considered? |
| Retention | Is retention justified and tracked? |
| Archival | Is long-term access restricted and recoverable? |
| Deletion | Is deletion complete, defensible, and evidenced? |

## Lifecycle control pattern

For each lifecycle stage, define:

- owner
- allowed locations
- allowed processing activities
- minimum control requirements
- evidence records
- monitoring signals
- exceptions
- deletion and retention requirements

## Common mistakes

- classifying only documents, not databases or API data
- ignoring derived data and analytics outputs
- losing control over exports
- missing data in logs, backups, caches, and data lakes
- treating deletion as a best-effort IT task
- failing to link lifecycle controls to breach response


## Typical evidence

- approved policy, standard, procedure, or architecture record
- risk assessment or design review
- owner and role assignment
- implementation plan
- operating records
- monitoring records
- exception or waiver decisions
- test results
- audit records
- management review decisions

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)
