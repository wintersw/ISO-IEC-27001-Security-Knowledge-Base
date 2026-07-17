---
title: Example Risk Register Entry
description: A worked cloud-access risk entry showing scenario, ownership, assessment, treatment, and evidence.
---

# Example Risk Register Entry

This example describes a plausible event and its business consequence rather than using a one-word risk such as “cloud” or “access control.” The values are illustrative; an organization must apply its approved scoring criteria and risk appetite.

| Field | Example |
|---|---|
| Risk ID | R-012 |
| Scenario | Unauthorized access to production cloud storage due to overly broad administrator roles and lack of quarterly review |
| Asset | Customer document storage |
| Owner | VP Engineering |
| Existing controls | single sign-on (SSO), multifactor authentication (MFA), cloud audit logs |
| Impact | 5 — Severe |
| Likelihood | 3 — Possible |
| Treatment | Mitigate |
| Actions | Least-privilege roles, quarterly review, alerting |
| Evidence | identity and access management (IAM) export, review records, remediation tickets |

## How to interpret the entry

The existing controls reduce likelihood but do not address whether administrative access remains appropriate over time. The treatment therefore adds least-privilege role design, a recurring review, and monitoring. The owner remains accountable for the risk decision even when technical teams perform the actions.

Before closure, define action owners and due dates, reassess residual likelihood and impact, and record whether the residual risk is accepted by an authorized role. Evidence should show both implementation and continuing operation—for example, a complete IAM export, documented reviewer decisions, completed removal tickets, and alerts investigated during the review period.


## Practical example

A process owner applies the guidance on **Example Risk Register Entry** to an in-scope service, records the decision and responsible roles, retains operating evidence, and reviews the result after a material change or control failure.

## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- approved decision or controlled procedure
- ownership and operating records
- test or review result
- exceptions and corrective actions


## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
