---
title: Supplier Security
description: Supplier security lifecycle and ISO 27001 implementation guidance.
category: Security Domains
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - security-domain
---

# Supplier Security

Supplier security manages risk from vendors, cloud services, outsourced providers, contractors, and business partners.

## Supplier lifecycle

1. identify supplier need
2. classify supplier risk
3. perform due diligence
4. define contract security requirements
5. approve onboarding
6. monitor performance
7. review changes
8. offboard securely


## Evidence

- supplier register
- due diligence questionnaire
- contract clauses
- risk rating
- review records
- offboarding confirmation

## Detailed implementation guidance

Supplier security manages risks from vendors, cloud providers, managed services, contractors, software dependencies, and fourth parties.

### Example

A managed service provider has privileged production access. Controls include named accounts, multifactor authentication (MFA), session logging, approval, access review, incident notification, subcontractor restrictions, continuity commitments, and exit support.

### Best practices

- tier suppliers by criticality and data
- assess before contract
- use risk-based evidence
- define security clauses
- monitor changes and incidents
- review privileged supplier access
- track subprocessors
- plan exit and data deletion
- reassess after material change
- link supplier findings to risk

### Common weaknesses

Questionnaires are accepted without validation, certificates are assumed to cover every service, contracts lack incident timelines, and exit requirements are considered too late.

## Related chapters

- [Supplier Lifecycle](../31-security-lifecycle-management/supplier-lifecycle.md)
- [Supplier Assurance Pack](../19-isms-professional-toolkit/supplier-assurance-pack.md)

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Supplier security is addressed through Annex A controls A.5.19 (information security in supplier relationships), A.5.20 (addressing information security within supplier agreements), A.5.21 (managing information security in the ICT supply chain), and A.5.22 (monitoring, review, and change management of supplier services). ISO/IEC 27036 provides additional guidance on supplier relationship security.
- **Implementation guidance:** Define supplier criticality tiers based on data access and service dependency, conduct risk-based due diligence before onboarding, include security requirements in contracts, monitor supplier performance and security posture, and manage offboarding securely.
- **Best practice:** Supplier security is not a one-time onboarding activity. The depth of ongoing monitoring should reflect the supplier's criticality, and offboarding must include revocation of access, return of data, and termination of interfaces.

## Practical example

The procurement team onboards a SaaS analytics provider that will process customer metadata. The security team conducts a risk-based due-diligence review, defines the required security controls in the contract, agrees on incident-notification SLAs, and schedules the first annual reassessment.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
