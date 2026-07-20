---
title: Identity and Access Management
description: Practical domain guidance for ISO 27001 security teams.
category: Security Domains
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - security-domain
---

# Identity and Access Management

IAM ensures the right identities have the right access to the right resources for the right reasons and for the right duration.

## Key concepts

- centralized identity
- multifactor authentication (MFA)
- least privilege
- joiner-mover-leaver
- privileged access management
- service accounts


## ISO relevance

This domain supports multiple ISO/IEC 27001 clauses and Annex A controls. Use the domain guidance to implement controls in a practical, operationally sustainable way.

## Evidence

- policy or standard
- process documentation
- configuration evidence
- logs or reports
- review records
- exceptions
- remediation tickets

## Detailed implementation guidance

Identity and access management ensures that people, services, devices, and automated workloads receive appropriate access throughout their lifecycle.

### Example

A contractor joins for a three-month project. The account is created through central identity, assigned a sponsor and expiry, protected by MFA, limited to required applications, and reviewed at project end. Extension requires a new approval.

### Best practices

- integrate HR and identity events
- use unique identities
- enforce strong authentication
- design roles around business need
- manage privileged access separately
- assign service-account owners
- use temporary and just-in-time access
- perform access reviews
- remove access promptly
- monitor risky sign-ins and privileged actions

### Common weaknesses

Mover access accumulates, service accounts lack owners, emergency access never expires, and quarterly reviews confirm accounts without validating privilege.

## Related chapters

- [Identity and Access Lifecycle](../31-security-lifecycle-management/identity-access-lifecycle.md)
- [Identity-Centric Security](../27-zero-trust-and-data-centric-security/identity-centric-security.md)

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Identity and access management spans multiple Annex A controls: A.5.15 (access control), A.5.16 (identity management), A.5.17 (authentication information), A.5.18 (access rights), A.8.2 (privileged access rights), A.8.3 (information access restriction), and A.8.5 (secure authentication). The organisation must manage the full identity lifecycle — provisioning, review, modification, and removal.
- **Implementation guidance:** Implement role-based access with least privilege, enforce MFA for all privileged and remote access, conduct periodic access reviews, automate joiner-mover-leaver workflows, and maintain an inventory of privileged accounts.
- **Best practice:** Access reviews that list accounts without requiring data owners to affirm or revoke each entitlement are a common audit finding. Reviews must produce an auditable decision per account, not a summary sign-off.

## Practical example

A quarterly access review identifies 14 accounts with privileged roles that no longer match the person's current function. The reviewer escalates the mismatches, the access manager revokes the obsolete entitlements within the defined SLA, and the review outcome is recorded as control evidence.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
