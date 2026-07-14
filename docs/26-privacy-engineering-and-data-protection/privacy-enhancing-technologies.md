---
title: Privacy-Enhancing Technologies
description: Catalog of privacy-enhancing technologies and when to consider them.
category: Privacy Engineering and Data Protection
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - PETs
  - privacy
---

# Privacy-Enhancing Technologies

Privacy-enhancing technologies reduce disclosure, linkage, inference, or misuse risk while preserving utility.

## PET catalog

| Technique | Example use |
|---|---|
| masking | hide sensitive fields from support users |
| tokenization | replace payment or customer identifiers |
| pseudonymization | analytics with controlled re-identification |
| anonymization | public or external aggregate release |
| differential privacy | aggregate statistics |
| secure multi-party computation | joint analytics without exposing raw data |
| federated learning | train across locations without centralizing raw data |
| homomorphic encryption | compute over encrypted values in specialized cases |
| trusted execution environments | protected computation boundary |
| synthetic data | testing and analytics with reduced exposure |

## Selection criteria

- sensitivity
- utility needs
- threat model
- re-identification risk
- implementation complexity
- performance impact
- assurance capability


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
