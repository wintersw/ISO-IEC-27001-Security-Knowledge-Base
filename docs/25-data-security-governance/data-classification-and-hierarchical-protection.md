---
title: Data Classification and Hierarchical Protection
description: Classification levels, labeling, handling rules, and tiered control strength.
category: Data Security Governance
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - classification
  - data-security
---

# Data Classification and Hierarchical Protection

Data classification helps the organization apply controls proportionate to sensitivity, business value, and risk.

## Suggested classification levels

| Level | Description | Example controls |
|---|---|---|
| Public | Approved for public release | integrity check, brand approval |
| Internal | Business data not intended for public release | employee access, internal sharing rules |
| Confidential | Sensitive business or personal information | restricted access, encryption, logging |
| Restricted | Highly sensitive data with serious harm potential | strong approval, DLP, monitoring, segmentation |
| Critical regulated | Data subject to strict legal, safety, or contractual obligations | formal risk assessment, enhanced assurance |

## Hierarchical protection

Higher classification should increase:

- identity assurance
- access approval strength
- monitoring depth
- encryption requirements
- data loss prevention rules
- retention restrictions
- supplier controls
- incident escalation priority
- audit sampling

## Classification decision factors

- confidentiality impact
- integrity impact
- availability impact
- privacy impact
- legal or contractual obligation
- fraud or misuse potential
- competitive sensitivity
- safety or public-interest impact

## Typical evidence

- approved classification policy with defined levels and handling rules
- labeling records or automated labeling configuration
- classification register for key datasets and systems
- records showing control strength increases with classification level
- reclassification decisions and periodic classification reviews

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

A finance team stores payroll extracts in the same shared drive as internal newsletters. After classification, payroll data is labeled Restricted: access now requires manager approval plus MFA, downloads are DLP-monitored, and retention is capped — while the Internal newsletter folder keeps its lightweight rules. The tiered model avoids over-protecting low-value data and under-protecting high-risk data.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
