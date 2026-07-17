---
title: Data Ownership and Stewardship
description: Roles and responsibilities for governing data security in the ISMS.
category: Data Security Governance
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - data-ownership
  - stewardship
---

# Data Ownership and Stewardship

Clear ownership is essential for data security. Without accountable owners, data classification, access, retention, deletion, and breach decisions become inconsistent.

## Role model

| Role | Responsibility |
|---|---|
| Data owner | Accountable for business value, classification, access, and risk decisions |
| Data steward | Maintains metadata, quality, lifecycle, and usage rules |
| System owner | Protects the system processing or storing the data |
| Risk owner | Accepts or treats risks related to the data |
| Control owner | Operates security controls that protect the data |
| Privacy owner | Advises on personal data, rights, minimization, and legal basis |
| Security architect | Designs technical protection patterns |
| Supplier owner | Ensures third-party data handling requirements are met |

## Ownership questions

- Who can approve access?
- Who can approve sharing?
- Who decides retention?
- Who approves deletion?
- Who receives breach notifications?
- Who approves exceptions?
- Who validates lineage?
- Who owns derived datasets?

## Typical evidence

- documented role model with named data owners and stewards per dataset
- access and sharing approvals signed by the accountable data owner
- retention and deletion decisions attributed to a named role
- ownership review records after reorganizations or staff changes
- escalation records showing breach notifications reached the right owner

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

An access request for a customer database stalls because nobody knows who may approve it — the original sponsor left two years ago. The organization assigns a data owner (approves access and sharing) and a steward (maintains metadata and usage rules) for each critical dataset, then adds ownership checks to the joiner, mover, and leaver process so stale assignments are detected and corrected.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
