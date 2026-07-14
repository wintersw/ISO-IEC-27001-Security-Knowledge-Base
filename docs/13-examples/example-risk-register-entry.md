---
title: Example Risk Register Entry
description: A worked cloud-access risk entry showing scenario, ownership, assessment, treatment, and evidence.
---

# Example Risk Register Entry

This example describes a plausible event and its business consequence rather than using a one-word risk such as “cloud” or “access control.” The values are illustrative; an organization must apply its approved scoring criteria and risk appetite.

| Field | Example |
|---|---|
| Risk ID | R-012 |
| Scenario | Unauthorized access to production cloud storage due to overly broad admin roles and lack of quarterly review |
| Asset | Customer document storage |
| Owner | VP Engineering |
| Existing controls | SSO, MFA, cloud audit logs |
| Impact | 5 — Severe |
| Likelihood | 3 — Possible |
| Treatment | Mitigate |
| Actions | Least-privilege roles, quarterly review, alerting |
| Evidence | IAM export, review records, remediation tickets |

## How to interpret the entry

The existing controls reduce likelihood but do not address whether administrative access remains appropriate over time. The treatment therefore adds least-privilege role design, a recurring review, and monitoring. The owner remains accountable for the risk decision even when technical teams perform the actions.

Before closure, define action owners and due dates, reassess residual likelihood and impact, and record whether the residual risk is accepted by an authorized role. Evidence should show both implementation and continuing operation—for example, a complete IAM export, documented reviewer decisions, completed removal tickets, and alerts investigated during the review period.
