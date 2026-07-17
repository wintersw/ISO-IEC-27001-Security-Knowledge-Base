---
title: Pseudonymization and Tokenization
description: How to reduce exposure while preserving controlled utility.
category: Privacy Engineering and Data Protection
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - pseudonymization
  - tokenization
---

# Pseudonymization and Tokenization

Pseudonymization replaces direct identifiers with alternative values while preserving the possibility of re-linking under controlled conditions. Tokenization replaces sensitive values with tokens and protects the mapping separately.

## Use cases

- analytics with reduced exposure
- customer support workflows
- payment or identifier protection
- research and data science
- non-production environments
- controlled data sharing

## Design decisions

- what fields are replaced?
- who can re-identify?
- where is the mapping stored?
- how is the mapping protected?
- are tokens reversible?
- are tokens format-preserving?
- are keys rotated?
- are logs safe?
- can multiple datasets be linked?

## Common mistakes

- treating pseudonymized data as anonymous
- storing mapping tables with the dataset
- allowing broad re-identification rights
- ignoring quasi-identifiers
- failing to monitor token lookup

## Typical evidence

- design record listing replaced fields and who may re-identify
- mapping-table or token-vault protection and separation evidence
- key rotation and token-lookup monitoring records
- quasi-identifier review showing pseudonymized data is not treated as anonymous
- non-production environments verified to use tokenized data

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

A data science team needs customer transaction history but not identities. Customer IDs are tokenized with the vault stored in a separate, monitored system, and only the fraud team may request re-identification with an approval workflow. A review also catches that postal code plus birth date remain in the dataset as quasi-identifiers, so birth dates are generalized to year — avoiding the classic mistake of treating pseudonymized data as anonymous.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
