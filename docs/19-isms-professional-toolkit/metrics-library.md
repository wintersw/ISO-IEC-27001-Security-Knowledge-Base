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
| Type | key performance indicator (KPI) or key risk indicator (KRI) |
| Purpose | Why it matters |
| Owner | Accountable person/team |
| Source | Data source |
| Formula | How calculated |
| Frequency | How often measured |
| Threshold | Green/amber/red criteria |
| Escalation | What happens when threshold is exceeded |

## identity and access management (IAM) metrics

| Metric | Type | Purpose |
|---|---|---|
| Privileged accounts without multifactor authentication (MFA) | KRI | Indicates access compromise exposure |
| Access reviews completed on time | KPI | Measures review process execution |
| Orphaned accounts | KRI | Indicates joiner-mover-leaver weakness |

## Vulnerability metrics

| Metric | Type | Purpose |
|---|---|---|
| Critical vulnerabilities overdue | KRI | Indicates exploitable exposure |
| Remediation within service-level agreement (SLA) | KPI | Measures patch process performance |
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

For a governance, risk, and compliance viewpoint including KPI, KRI, and key control indicator (KCI) usage, see:

- [Governance, Risk, and Compliance Operating Model](../24-pdf-source-integration/governance-risk-compliance-operating-model.md)
- [KPIs and KRIs](../04-isms/kpis-and-kris.md)

## Related modern data security metrics

For data security, breach, Zero Trust, artificial intelligence (AI), and post-quantum metrics, see:

- [Data Security Metrics Dashboard Template](../10-templates/data-security-metrics-dashboard-template.md)
- [Incident and Breach Metrics](../28-incident-and-data-breach-management/incident-and-breach-metrics.md)
- [Zero Trust Monitoring and Metrics](../27-zero-trust-and-data-centric-security/zero-trust-monitoring-and-metrics.md)


## Practical example

An ISMS manager selects "privileged accounts without MFA" from this library as a KRI, completes the definition template (source: IAM system export; frequency: monthly; amber at 5, red at 10; escalation to the security steering committee), and adds it to the health dashboard. Three months later the metric crosses the red threshold after an acquisition onboards new administrators, triggering the predefined escalation and a funded remediation plan — instead of the gap surfacing for the first time in an audit.

## Evidence to retain

Retain records showing that metrics are defined, measured, and acted on, such as:

- completed metric definitions with owner, source, formula, and thresholds
- periodic measurement outputs and dashboard extracts
- threshold breach escalations and resulting decisions
- metric review records (retired, recalibrated, or added metrics)


## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
