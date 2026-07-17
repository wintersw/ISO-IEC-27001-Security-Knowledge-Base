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

- dataset approval records for each model training run
- training data lineage linking models to source datasets
- privacy test results (memorization, membership inference, output leakage)
- prompt and inference logging rules with retention limits
- human review records for high-impact model uses

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

A team fine-tunes a support chatbot on historical tickets. Privacy testing shows the model can reproduce customer names and order numbers verbatim. The team pseudonymizes tickets before training, adds output filtering for identifier patterns, records dataset approval and lineage, and limits prompt-log retention — so the model keeps its utility without memorizing personal data.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
