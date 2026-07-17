---
title: IT Governance vs IT Management
description: Clarifies the difference between governance and management for security professionals.
category: IT Governance and ITSM
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - it-governance
  - itsm
  - isms
---

# IT Governance vs IT Management

Governance and management are related but different.

## Governance

Governance evaluates, directs, and monitors. Examples include approving IT risk appetite, setting strategic priorities, deciding major investments, reviewing service and security performance, accepting high residual risk, and overseeing obligations.

## Management

Management plans, builds, runs, and improves. Examples include deploying patches, operating the service desk, configuring monitoring, managing incidents, running access reviews, and reporting metrics.

## Why the distinction matters

Security teams often get stuck doing management work while governance decisions remain unresolved. Security can identify a risk, but accountable governance must approve resources, set priorities, or accept residual risk.

## Practical rule

If a decision involves risk acceptance, resources, priority conflict, or policy enforcement across business units, it should be visible to governance.

## Related tools

- [Management Decision Log Template](../10-templates/management-decision-log-template.md)
- [governance, risk, and compliance (GRC) Operating Map Template](../10-templates/grc-operating-map-template.md)


## Practical example

The security operations team detects that a critical customer-facing application runs on an unsupported operating system and cannot be patched (management identifies the risk). The team escalates to the IT governance forum, which must decide whether to fund replacement, add compensating controls, accept residual risk for a defined period, or retire the service. Management implements the decision; governance owns the acceptance.

## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- service or configuration record
- risk, approval, and segregation-of-duties evidence
- test and implementation logs
- post-implementation review and follow-up actions


## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
