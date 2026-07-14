---
title: Anonymization and Re-identification Risk
description: Limits of anonymization and how to assess re-identification risk.
category: Privacy Engineering and Data Protection
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - anonymization
  - re-identification
---

# Anonymization and Re-identification Risk

Anonymization attempts to remove the ability to identify individuals. In practice, re-identification risk depends on context, auxiliary datasets, uniqueness, and attacker capability.

## Risk drivers

- rare attributes
- geographic precision
- timestamps
- linkage across datasets
- small groups
- public auxiliary data
- persistent identifiers
- high-dimensional data
- model outputs

## Review questions

- Is the dataset truly anonymous or only pseudonymized?
- Which quasi-identifiers remain?
- Can records be linked to public datasets?
- Can an attacker infer sensitive attributes?
- Is data released once or repeatedly?
- Are small cohorts suppressed?
- Is aggregation sufficient?
- Is re-identification tested?

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

- **ISO requirement:** This chapter explains **Anonymization and Re-identification Risk** without reproducing standard text. Determine formal obligations from the applicable clauses, scope, risk treatment, Statement of Applicability, and binding legal or contractual requirements.
- **Implementation guidance:** Adapt the described roles, frequency, workflow, and evidence to the organization.
- **Best practice:** Enhancements are optional unless adopted through policy, contract, or risk treatment.

## Practical example

A product team applies this guidance before using personal data for a new feature. It documents necessity, evaluates privacy and re-identification risk, selects safeguards, and tests the result before release.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
