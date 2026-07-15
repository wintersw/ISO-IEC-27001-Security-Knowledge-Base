---
title: Zero Trust
description: Explains Zero Trust principles and their relationship to ISO 27001.
category: Fundamentals
difficulty: Beginner
applies_to:
  - ISO/IEC 27001:2022
tags:
  - fundamentals
---

# Zero Trust

Zero Trust is a security approach based on continuous verification, least privilege, and the assumption that network location alone should not establish trust.

## Core principles

- Verify explicitly.
- Use least privilege.
- Assume breach.
- Continuously evaluate risk.
- Segment access.
- Monitor behavior.

## Practical implementation

- Central identity and multifactor authentication (MFA)
- Device posture checks
- Conditional access
- Network segmentation
- Strong logging
- Privileged access management
- Micro-segmentation where appropriate
- Continuous monitoring

## ISO relevance

Zero Trust is not required by name in ISO/IEC 27001, but it supports many controls, especially access control, identity management, secure authentication, network segregation, logging, and monitoring.

## Common mistakes

- Treating Zero Trust as a product purchase
- Ignoring legacy systems
- Implementing conditional access without user impact planning
- Not monitoring service accounts and APIs

## Evidence

- access policies
- conditional-access configuration
- segmentation diagrams
- identity and access management (IAM) logs
- access-review records

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** This chapter explains **Zero Trust** without reproducing standard text. Determine formal obligations from the applicable clauses, scope, risk treatment, Statement of Applicability, and binding legal or contractual requirements.
- **Implementation guidance:** Adapt the described roles, frequency, workflow, and evidence to the organization.
- **Best practice:** Enhancements are optional unless adopted through policy, contract, or risk treatment.

## Practical example

After a VPN appliance compromise let an attacker move laterally to the HR database, a company drops the assumption that the corporate network is trusted. It deploys device posture checks, enforces MFA on every access, segments workloads with micro-segmentation, and monitors east-west traffic. It records the architecture change, the risk of lateral movement, and continuous verification metrics.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
