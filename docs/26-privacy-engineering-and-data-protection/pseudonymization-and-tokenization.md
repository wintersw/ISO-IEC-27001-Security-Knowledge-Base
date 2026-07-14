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

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** This chapter explains **Pseudonymization and Tokenization** without reproducing standard text. Determine formal obligations from the applicable clauses, scope, risk treatment, Statement of Applicability, and binding legal or contractual requirements.
- **Implementation guidance:** Adapt the described roles, frequency, workflow, and evidence to the organization.
- **Best practice:** Enhancements are optional unless adopted through policy, contract, or risk treatment.

## Practical example

A product team applies this guidance before using personal data for a new feature. It documents necessity, evaluates privacy and re-identification risk, selects safeguards, and tests the result before release.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
