---
title: Privacy and PII Protection
description: Privacy management concepts connected to ISO 27001 and ISO 27701.
category: Security Domains
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - security-domain
---

# Privacy and personally identifiable information (PII) Protection

Privacy protects the rights and freedoms of individuals whose personal data is processed.

## Security and privacy relationship

Security protects data against unauthorized disclosure, alteration, and loss. Privacy also addresses lawful processing, transparency, purpose limitation, data subject rights, retention, and sharing.


## Evidence

- processing records
- privacy notices
- DPIAs
- data subject request records
- supplier privacy terms
- breach assessment records

## Detailed implementation guidance

Privacy protects people from inappropriate collection, use, inference, disclosure, retention, and decision-making. Security provides important controls, but privacy also asks whether processing is necessary, expected, fair, and transparent.

### Example

An analytics team proposes combining customer support data with product telemetry. Privacy engineering identifies new inference risk, limits fields, aggregates outputs, restricts access, defines retention, and records the approved purpose.

### Best practices

- identify personal data and data subjects
- document purpose
- minimize data
- map flows
- assess re-identification
- use pseudonymization or masking where useful
- control retention and deletion
- review high-risk analytics and artificial intelligence (AI)
- prepare breach workflows
- test privacy controls

### Common weaknesses

Organizations rely on consent language while collecting unnecessary data, treat pseudonymized data as anonymous, and fail to propagate deletion to derived data.

## Related chapters

- [Privacy Engineering and Data Protection](../26-privacy-engineering-and-data-protection/index.md)
- [Privacy Threat Modeling](../26-privacy-engineering-and-data-protection/privacy-threat-modeling.md)

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Privacy and PII protection is addressed primarily through Annex A control A.5.34 (privacy and protection of PII). Where the organisation implements a Privacy Information Management System, ISO/IEC 27701 provides the extension to the ISMS. The organisation must identify applicable privacy legislation and implement controls to meet those obligations.
- **Implementation guidance:** Conduct data protection impact assessments for processing activities, maintain a record of processing activities, define data-subject-rights procedures, implement privacy notices and consent mechanisms, and manage data retention and deletion.
- **Best practice:** Privacy and security governance should be integrated — running separate privacy and security programmes with duplicate risk assessments, control frameworks, and management reporting creates inefficiency and gaps.

## Practical example

The marketing team plans to introduce a customer-behaviour analytics feature. The privacy team conducts a DPIA, identifies the lawful basis and purpose-limitation obligations, documents the data flows and retention rules, and ensures the consent mechanism is granular and withdrawable before launch.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
