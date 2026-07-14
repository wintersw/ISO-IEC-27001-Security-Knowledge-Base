---
title: ISMS KPIs and KRIs
description: Practical ISMS guidance for ISMS KPIs and KRIs.
---

# ISMS KPIs and KRIs

Metrics help leadership decide whether the information security management system (ISMS) is delivering its intended results and whether risk is moving outside acceptable limits.

## Purpose

A **key performance indicator (KPI)** shows whether an activity or objective is performing as intended. A **key risk indicator (KRI)** signals increasing exposure or deteriorating conditions. Neither is useful unless it leads to a defined decision or action.

## Key concepts

- **Measure:** the raw value, such as overdue actions.
- **Indicator:** a measure interpreted against a target, threshold, or trend.
- **KPI:** performance against an expected result, such as access reviews completed by the due date.
- **KRI:** changing exposure, such as critical vulnerabilities past the approved remediation time.
- **Owner:** the role accountable for data quality, interpretation, and escalation.

## Practical implementation

1. Start with a security objective, control outcome, or management decision—not with available data.
2. Define the indicator, population, formula, source, frequency, owner, target, and escalation threshold.
3. Validate completeness and accuracy before reporting the result.
4. Show trend and context; an isolated percentage can conceal backlog, excluded systems, or accepted exceptions.
5. Record the decision or action triggered when a threshold is crossed.
6. Retire indicators that no longer change decisions or accurately represent risk.

## Practical example

An access-review KPI reports 98% completion, but the related KRI shows twelve overdue removals involving privileged accounts. Management does not treat the high completion percentage as success: it assigns remediation, investigates why privileged removals are late, and tracks the KRI until exposure returns below the approved threshold.

## Evidence to retain

- metric definition and approved calculation method;
- source-system extract and population reconciliation;
- dashboard or report with reporting period and owner;
- threshold breaches, decisions, and assigned actions; and
- changes to the metric and validation or review records.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** ISO/IEC 27001 requires measurable objectives where practicable and evaluation of ISMS performance and effectiveness, but it does not prescribe a KPI/KRI dashboard or universal metric set.
- **Implementation guidance:** Select indicators that support the organization's objectives, risks, controls, and management-review decisions.
- **Best practice:** Combine performance, risk, control, and data-quality indicators so a favorable headline does not hide material exposure.

## Common mistakes

- counting completed activities without testing their outcome;
- reporting percentages without the numerator, denominator, exclusions, or trend;
- selecting easy-to-collect measures that do not support a decision;
- allowing the team being measured to alter definitions without review; and
- keeping permanently green thresholds that never trigger challenge.

## Related controls, clauses, templates, and checklists

- [Security objectives](security-objectives.md)
- [Metrics and management review](metrics-and-management-review.md)
- [Evidence model](evidence-model.md)
- [KPI/KRI Dashboard Template](../10-templates/kpi-kri-dashboard-template.md)
- [Management Review Checklist](../11-checklists/management-review.md)
- [A.8.16 Monitoring activities](../06-annex-a/technological/a8-16-monitoring-activities.md)
- [Abbreviations](../15-reference/abbreviations.md)
