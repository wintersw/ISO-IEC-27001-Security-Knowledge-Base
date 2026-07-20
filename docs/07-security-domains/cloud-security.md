---
title: Cloud Security
description: Practical domain guidance for ISO 27001 security teams.
category: Security Domains
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - security-domain
---

# Cloud Security

Cloud security requires clear understanding of shared responsibility. The provider secures some layers, while the customer remains responsible for configuration, identity, data, access, monitoring, and usage decisions.

## Key concepts

- shared responsibility
- landing zones
- guardrails
- central logging
- cloud posture management
- software as a service (SaaS) governance


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

Cloud security combines shared responsibility, identity, configuration, data protection, monitoring, supplier governance, resilience, and cost-aware architecture. Moving a service to cloud infrastructure does not transfer accountability for information security.

### Example

A team deploys a data-processing service to a public cloud. Security requirements include separate accounts, strong federation, restricted administrator roles, infrastructure-as-code, encryption, key management, centralized logging, backup, public-exposure prevention, and supplier incident procedures.

### Best practices

- document the shared-responsibility model
- use organization-level guardrails
- centralize identity and logging
- enforce secure configuration through code and policy
- inventory cloud resources and data
- separate environments
- monitor privileged actions
- manage secrets centrally
- review cloud-provider dependencies
- test backup and region failure
- plan exit and data deletion

### Common weaknesses

Cloud environments fail when teams assume the provider handles everything, create unmanaged accounts, leave public resources exposed, fail to collect audit logs, or permit standing privilege.

## Related chapters

- [Cloud Data Security Patterns](../29-emerging-data-security-trends/cloud-data-security-patterns.md)
- [Zero Trust and Data-Centric Security](../27-zero-trust-and-data-centric-security/index.md)

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Cloud security is primarily addressed through Annex A control A.5.23 (information security for use of cloud services). Supplementary guidance comes from ISO/IEC 27017 (cloud-specific controls) and, where PII is involved, ISO/IEC 27018. The organisation must manage cloud services through a documented process that covers procurement, configuration, monitoring, and termination.
- **Implementation guidance:** Define the cloud procurement and security review process, document the shared-responsibility model per service type, manage cloud-service inventory, and ensure security requirements are included in cloud agreements.
- **Best practice:** Apply least privilege and default-deny for cloud IAM, enable logging and encryption by default through policy or landing-zone guardrails, and continuously monitor configuration against a hardened baseline.

## Practical example

The infrastructure team deploys a new workload in the cloud. The team reviews the shared-responsibility model for each service, applies least-privilege IAM roles, enables encryption and logging by default through a landing-zone policy, and validates the configuration against a hardened baseline before production traffic.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
