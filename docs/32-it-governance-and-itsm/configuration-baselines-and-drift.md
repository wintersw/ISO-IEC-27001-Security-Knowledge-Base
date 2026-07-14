---
title: Configuration Baselines and Drift
description: How ITSM configuration management supports secure configuration and drift control.
category: IT Governance and ITSM
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - it-governance
  - itsm
  - cobit
  - itil
---

# Configuration Baselines and Drift

A configuration baseline defines the approved state of a system or service. Drift occurs when actual configuration moves away from that state.

## Example

A cloud storage baseline requires encryption, logging, restricted public access, approved regions, and owner tags. Continuous checks detect a storage bucket created without logging.

The issue is not merely a technical alert. The workflow should:

1. identify the owner
2. assess exposure
3. correct configuration
4. preserve evidence
5. determine why preventive controls failed
6. improve templates or policy enforcement

## Best practices

- Define baselines by technology and risk tier.
- Automate detection where possible.
- Link drift findings to change records.
- distinguish approved exceptions from unauthorized drift.
- track recurring baseline violations.
- include cloud, network, endpoint, database, and identity configuration.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** This chapter explains **Configuration Baselines and Drift** without reproducing standard text. Determine formal obligations from the applicable clauses, scope, risk treatment, Statement of Applicability, and binding legal or contractual requirements.
- **Implementation guidance:** Adapt the described roles, frequency, workflow, and evidence to the organization.
- **Best practice:** Enhancements are optional unless adopted through policy, contract, or risk treatment.

## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- service or configuration record
- risk, approval, and segregation-of-duties evidence
- test and implementation logs
- post-implementation review and follow-up actions

Intent documents are insufficient on their own; retain scoped operating records, approvals, exceptions, and verified follow-up.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
