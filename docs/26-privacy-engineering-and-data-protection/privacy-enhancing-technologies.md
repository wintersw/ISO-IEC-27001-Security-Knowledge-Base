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

## privacy-enhancing technology (PET) catalog

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

- documented PET selection rationale against sensitivity, utility, and threat model
- design and validation records for the chosen technique
- assessment of residual re-identification or inference risk
- operating records showing the PET works as designed (e.g., masking tests, token audits)
- periodic review confirming the technique still fits the use case

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

Two business units want joint fraud analytics without sharing raw customer data with each other. After comparing options against the selection criteria, the team rejects plain data sharing, pilots secure multi-party computation for the highest-value queries, and uses tokenized datasets for the rest — documenting why each technique was chosen and validating that raw identifiers never leave either unit.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
