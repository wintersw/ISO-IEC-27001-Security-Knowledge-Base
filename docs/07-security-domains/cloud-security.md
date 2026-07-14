---
title: Cloud Security
description: Practical domain guidance for ISO 27001 security teams.
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

- **ISO requirement:** This chapter explains **Cloud Security** without reproducing standard text. Determine formal obligations from the applicable clauses, scope, risk treatment, Statement of Applicability, and binding legal or contractual requirements.
- **Implementation guidance:** Adapt the described roles, frequency, workflow, and evidence to the organization.
- **Best practice:** Enhancements are optional unless adopted through policy, contract, or risk treatment.

## Practical example

A growing software-as-a-service provider applies this guidance to a new customer-data feature. The service owner identifies the relevant risks, implements proportionate safeguards, and verifies them before release and during operation.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
