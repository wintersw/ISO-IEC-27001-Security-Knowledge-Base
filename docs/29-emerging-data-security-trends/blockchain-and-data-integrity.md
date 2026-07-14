---
title: Blockchain and Data Integrity
description: When blockchain-style mechanisms may or may not help data integrity.
category: Emerging Data Security Trends
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - blockchain
  - data-integrity
---

# Blockchain and Data Integrity

Blockchain and distributed ledger techniques can support tamper-evident records, but they do not solve all trust or data-quality problems.

## Potential uses

- integrity proof
- shared audit trail
- multi-party transaction record
- supply-chain traceability
- notarization of evidence hashes

## Limitations

- bad data can be written immutably
- privacy and deletion can be difficult
- key management remains critical
- governance of participants is still required
- performance and cost may be unsuitable
- smart contracts can contain vulnerabilities

## Decision questions

- Is multi-party trust the real problem?
- Who governs the ledger?
- What data goes on-chain?
- Can sensitive data be kept off-chain?
- How is deletion handled?
- How are keys protected?
- How are smart contracts tested?


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
