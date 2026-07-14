---
title: Privacy in Machine Learning
description: Privacy risks and controls for ML and data science pipelines.
category: Privacy Engineering and Data Protection
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - machine-learning
  - privacy
---

# Privacy in Machine Learning

Machine learning introduces privacy risks through training data, feature engineering, model outputs, inference, prompts, embeddings, and monitoring logs.

## Risk examples

- model memorizes sensitive records
- embeddings expose sensitive content
- prompts contain personal data
- outputs reveal sensitive attributes
- training data is reused beyond purpose
- model users infer membership
- datasets lack lineage
- labels introduce bias or fairness concerns

## Controls

- dataset approval
- minimization
- pseudonymization
- access controls
- model/data lineage
- privacy testing
- output filtering
- retention and deletion process
- prompt logging controls
- human review for high-impact uses

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

- **ISO requirement:** This chapter explains **Privacy in Machine Learning** without reproducing standard text. Determine formal obligations from the applicable clauses, scope, risk treatment, Statement of Applicability, and binding legal or contractual requirements.
- **Implementation guidance:** Adapt the described roles, frequency, workflow, and evidence to the organization.
- **Best practice:** Enhancements are optional unless adopted through policy, contract, or risk treatment.

## Practical example

A product team applies this guidance before using personal data for a new feature. It documents necessity, evaluates privacy and re-identification risk, selects safeguards, and tests the result before release.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
