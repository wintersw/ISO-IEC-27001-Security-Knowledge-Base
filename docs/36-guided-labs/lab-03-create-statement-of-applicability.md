---
title: Lab 3 — Create a Statement of Applicability
description: Build SoA entries from risk scenarios and business requirements.
category: Guided Labs
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - lab
  - workshop
  - practical
---

# Lab 3 — Create a Statement of Applicability

## Scenario

Use the customer data warehouse from Lab 2.

## Tasks

Create SoA rows for:

- A.5.9 asset inventory
- A.5.12 classification
- A.5.15 access control
- A.5.16 identity management
- A.5.18 access rights
- A.8.11 data masking
- A.8.12 data leakage prevention
- A.8.15 logging
- A.8.16 monitoring

For each row, record:

- applicability
- justification
- implementation status
- owner
- related risks
- evidence

## Suggested answer pattern

**A.8.16 Monitoring activities — Applicable**

The control is applicable because the risk assessment identifies unauthorized bulk export as a high risk. Existing authentication logs are insufficient because they do not detect abnormal data-access volume. Implementation includes security information and event management (SIEM) alerts for bulk export, unusual access time, and repeated failed authorization.

Evidence includes alert rules, sample alerts, triage tickets, and quarterly effectiveness review.

## Review questions

- Are justifications specific to the organization?
- Is implementation status honest?
- Is evidence current?
- Are exclusions justified by risk and context rather than convenience?


## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- completed lab output
- assumptions and decision rationale
- review feedback
- revised result and lessons learned


## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
