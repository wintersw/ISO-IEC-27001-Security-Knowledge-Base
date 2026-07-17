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

- documented decision analysis of whether multi-party trust justified a ledger
- ledger governance agreement between participants
- on-chain/off-chain data design showing sensitive data stays off-chain
- key management and smart contract test records
- deletion-handling design for privacy obligations

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

A logistics consortium proposes putting shipment records on a blockchain. The review finds that sensitive customer data was planned to go on-chain, conflicting with correction and deletion requirements. The redesign keeps source data off-chain in controlled stores and considers whether even document hashes could identify a person or enable linkage before recording them on-chain. This preserves a limited tamper-evidence use case while allowing off-chain records to follow applicable retention, correction, and deletion processes.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
