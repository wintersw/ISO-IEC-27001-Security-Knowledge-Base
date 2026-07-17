---
title: Federated Learning and Privacy
description: Federated learning as a privacy-preserving analytics pattern.
category: Emerging Data Security Trends
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - federated-learning
  - privacy
---

# Federated Learning and Privacy

Federated learning allows model training across distributed data locations without centralizing all raw data.

## Potential benefits

- reduced central data concentration
- local data control
- improved privacy posture
- support for cross-organization analytics
- reduced data transfer

## Risks

- model update leakage
- poisoning by participants
- participant trust issues
- aggregation server compromise
- weak identity controls
- uneven local controls
- governance complexity

## Controls

- participant vetting
- secure aggregation
- differential privacy where appropriate
- strong identity
- update validation
- anomaly detection
- legal and contractual controls

## Typical evidence

- participant vetting and contractual agreement records
- secure aggregation and update validation design documentation
- identity controls for participants and the aggregation server
- anomaly detection results on model updates
- assessment of residual leakage risk from shared model updates

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)


## Practical example

Five hospitals want a shared diagnostic model without exchanging patient records. Federated learning keeps raw data local, but the risk review notes that model updates can still leak information and a malicious participant could poison training. The consortium adds secure aggregation, per-participant update validation, contractual controls, and anomaly detection on submitted updates — documenting that "no raw data leaves the hospital" alone was not a sufficient privacy claim.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
