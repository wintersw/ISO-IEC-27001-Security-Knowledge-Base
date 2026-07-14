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

# Privacy and PII Protection

Privacy protects the rights and freedoms of individuals whose personal data is processed.

## Security and privacy relationship

Security protects data against unauthorized disclosure, alteration, and loss. Privacy also addresses lawful processing, transparency, purpose limitation, data subject rights, retention, and sharing.

## Best practices

- Maintain a personal data inventory.
- Identify controller and processor roles.
- Perform DPIAs where needed.
- Include privacy in supplier reviews.
- Align incident response with breach notification requirements.
- Define retention and deletion rules.

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
- review high-risk analytics and AI
- prepare breach workflows
- test privacy controls

### Common weaknesses

Organizations rely on consent language while collecting unnecessary data, treat pseudonymized data as anonymous, and fail to propagate deletion to derived data.

## Related chapters

- [Privacy Engineering and Data Protection](../26-privacy-engineering-and-data-protection/index.md)
- [Privacy Threat Modeling](../26-privacy-engineering-and-data-protection/privacy-threat-modeling.md)
