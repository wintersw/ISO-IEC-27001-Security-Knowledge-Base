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

## Best practices

- Define data classes.
- Map data flows.
- Restrict sensitive data access.
- Avoid production data in test.
- Define retention and deletion rules.
- Monitor high-risk transfers.

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

- **ISO requirement:** This chapter explains **Data Protection** without reproducing standard text. Determine formal obligations from the applicable clauses, scope, risk treatment, Statement of Applicability, and binding legal or contractual requirements.
- **Implementation guidance:** Adapt the described roles, frequency, workflow, and evidence to the organization.
- **Best practice:** Enhancements are optional unless adopted through policy, contract, or risk treatment.

## Practical example

A growing software-as-a-service provider applies this guidance to a new customer-data feature. The service owner identifies the relevant risks, implements proportionate safeguards, and verifies them before release and during operation.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
