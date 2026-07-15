---
title: ISO/IEC 27017 Cloud Security
description: Explains how ISO/IEC 27017 supports cloud security control design.
category: ISO 27000 Family
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - iso27000-family
---

# ISO/IEC 27017 Cloud Security

ISO/IEC 27017 provides cloud-specific guidance based on ISO/IEC 27002. It helps cloud service customers and providers understand additional cloud control considerations.

## Key themes

- shared responsibility
- cloud customer and provider roles
- cloud service configuration
- virtualized environments
- cloud monitoring
- supplier and service agreements
- administrative access
- data deletion and return

## Practical use

Use this guidance when:

- adopting infrastructure as a service (IaaS), platform as a service (PaaS), or software as a service (SaaS)
- negotiating cloud contracts
- defining cloud security baselines
- building cloud landing zones
- documenting shared responsibilities
- reviewing cloud suppliers

## Evidence

- cloud responsibility matrix
- cloud security baseline
- cloud asset inventory
- logging configuration
- supplier agreements
- cloud risk assessment

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** ISO/IEC 27017 provides additional controls and implementation guidance for cloud services, building on ISO/IEC 27002. If the organisation uses cloud services within the ISMS scope and selects ISO/IEC 27017 controls through risk treatment, those controls become part of the documented information and are subject to the same audit and improvement discipline as Annex A controls.
- **Implementation guidance:** Map cloud service types (IaaS, PaaS, SaaS) to the shared-responsibility model, identify which controls the customer operates and which the provider operates, and document the boundary.
- **Best practice:** Apply the cloud-specific control extensions even when the cloud service is managed by the provider — the organisation retains accountability for the security outcome.

## Practical example

The cloud architecture team reviews the existing cloud controls against ISO/IEC 27017. The review confirms that shared-responsibility boundaries are documented per service type, that customer data isolation is enforced at the virtual network and IAM layers, and that a cloud-specific risk assessment covers the provider's sub-processors.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
