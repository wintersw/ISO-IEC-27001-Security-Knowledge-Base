---
title: Identity and Access Management
description: Practical domain guidance for ISO 27001 security teams.
---

# Identity and Access Management

IAM ensures the right identities have the right access to the right resources for the right reasons and for the right duration.

## Key concepts

- centralized identity
- MFA
- least privilege
- joiner-mover-leaver
- privileged access management
- service accounts

## Best practices

- Define ownership and scope.
- Integrate with risk management.
- Document minimum requirements.
- Automate evidence collection where practical.
- Review exceptions and control performance.
- Link operational practices to Annex A and the SoA.

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
