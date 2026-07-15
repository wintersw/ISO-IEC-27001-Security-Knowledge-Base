---
title: Data Protection
description: Data protection controls for classification, retention, transfer, masking, deletion, and leakage prevention.
category: Security Domains
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - security-domain
---

# Data Protection

Data protection ensures information is handled according to sensitivity, business value, legal obligations, and risk.

## Key practices

- classification
- labeling
- retention
- secure transfer
- encryption
- masking
- deletion
- data loss prevention (DLP)
- backup
- privacy controls


## Evidence

- classification policy
- data inventory
- DLP alerts
- deletion records
- transfer approvals
- masking procedures

## Detailed implementation guidance

Data protection applies security controls according to data value, sensitivity, use, location, and lifecycle. It is broader than encryption and includes ownership, classification, minimization, access, masking, monitoring, retention, sharing, and deletion.

### Example

A support team needs customer context but not full payment identifiers. The application masks sensitive fields, restricts bulk export, logs record access, and requires approval for exceptional access. Retention rules remove old exports.

### Best practices

- maintain a data asset register
- classify data
- map flows and copies
- minimize collection
- restrict access by purpose
- use masking and tokenization
- monitor bulk access and export
- control non-production data
- define retention and defensible deletion
- include suppliers and backups

### Common weaknesses

Organizations protect production databases but ignore exports, logs, caches, analytics copies, support downloads, and test systems.

## Related chapters

- [Data Security Governance](../25-data-security-governance/index.md)
- [Privacy Engineering](../26-privacy-engineering-and-data-protection/index.md)

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Data protection spans multiple Annex A controls: A.5.12 (classification of information), A.5.33 (protection of records), A.5.34 (privacy and protection of PII), A.8.10 (information deletion), A.8.11 (data masking), A.8.12 (data leakage prevention), and A.8.13 (information backup). Each must be selected through risk treatment and implemented as documented information.
- **Implementation guidance:** Classify data by sensitivity and regulatory impact, define handling rules per classification level, implement technical controls (encryption, DLP, masking) aligned to classification, and manage the data lifecycle from creation to secure deletion.
- **Best practice:** Data classification is the prerequisite — without it, protection controls are applied inconsistently. Ensure classification labels are actionable (linked to specific handling requirements) rather than decorative.

## Practical example

The organisation plans to share a pseudonymised dataset with a research partner. The DPO reviews the legal basis, the data owner classifies the fields and confirms that re-identification risk is low, a data-sharing agreement is signed, and the transfer is logged with a retention schedule.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
