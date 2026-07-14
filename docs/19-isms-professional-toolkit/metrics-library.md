---
title: ISMS Metrics Library
description: Reusable KPI and KRI catalog for ISMS professionals.
category: ISMS Professional Toolkit
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - isms
  - professional-toolkit
---

# ISMS Metrics Library

Metrics should help decision-makers understand performance, risk exposure, and improvement.

## Metric definition template

| Field | Description |
|---|---|
| Metric name | Clear name |
| Type | KPI or KRI |
| Purpose | Why it matters |
| Owner | Accountable person/team |
| Source | Data source |
| Formula | How calculated |
| Frequency | How often measured |
| Threshold | Green/amber/red criteria |
| Escalation | What happens when threshold is exceeded |

## IAM metrics

| Metric | Type | Purpose |
|---|---|---|
| Privileged accounts without MFA | KRI | Indicates access compromise exposure |
| Access reviews completed on time | KPI | Measures review process execution |
| Orphaned accounts | KRI | Indicates joiner-mover-leaver weakness |

## Vulnerability metrics

| Metric | Type | Purpose |
|---|---|---|
| Critical vulnerabilities overdue | KRI | Indicates exploitable exposure |
| Remediation within SLA | KPI | Measures patch process performance |
| Scan coverage | KPI | Measures visibility |

## Incident metrics

| Metric | Type | Purpose |
|---|---|---|
| Mean time to detect | KPI | Detection capability |
| Mean time to contain | KPI | Response capability |
| Repeat incident themes | KRI | Control weakness trend |

## Supplier metrics

| Metric | Type | Purpose |
|---|---|---|
| High-risk suppliers overdue for review | KRI | Supplier assurance weakness |
| Suppliers assessed before onboarding | KPI | Process compliance |
| Supplier incidents | KRI | Third-party exposure |

## Audit metrics

| Metric | Type | Purpose |
|---|---|---|
| Findings overdue | KRI | Corrective action weakness |
| Repeat findings | KRI | Root-cause failure |
| Audit plan completion | KPI | Assurance coverage |

## Related GRC monitoring model

For a governance, risk, and compliance viewpoint including KPI, KRI, and KCI usage, see:

- [Governance, Risk, and Compliance Operating Model](../24-pdf-source-integration/governance-risk-compliance-operating-model.md)

## Related modern data security metrics

For data security, breach, Zero Trust, AI, and post-quantum metrics, see:

- [Data Security Metrics Dashboard Template](../10-templates/data-security-metrics-dashboard-template.md)
- [Incident and Breach Metrics](../28-incident-and-data-breach-management/incident-and-breach-metrics.md)
- [Zero Trust Monitoring and Metrics](../27-zero-trust-and-data-centric-security/zero-trust-monitoring-and-metrics.md)
