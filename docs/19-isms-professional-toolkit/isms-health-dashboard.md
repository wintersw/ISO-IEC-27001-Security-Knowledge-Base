---
title: ISMS Health Dashboard
description: Dashboard design for monitoring ISMS performance, risk, control health, and improvement.
category: ISMS Professional Toolkit
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - isms
  - professional-toolkit
---

# ISMS Health Dashboard
An ISMS health dashboard summarizes whether the management system is operating, effective, and improving.

## Dashboard principles

A useful dashboard should:

- be understandable by management
- link metrics to risk and objectives
- show trends, not only point-in-time values
- highlight overdue decisions and actions
- distinguish performance indicators from risk indicators
- trigger escalation when thresholds are exceeded

## Recommended dashboard sections

### Risk

| Metric | Purpose |
|---|---|
| Open high risks | Shows unresolved exposure |
| Overdue treatment actions | Shows risk treatment discipline |
| Aging accepted risks | Shows whether risk acceptance is reviewed |
| Risks without owners | Shows governance weakness |

### Controls

| Metric | Purpose |
|---|---|
| Controls without evidence | Indicates assurance gaps |
| Controls with overdue reviews | Shows operating weakness |
| Failed control tests | Shows design or operation problems |
| Aging control exceptions | Shows control erosion |

### Operations

| Metric | Purpose |
|---|---|
| Critical vulnerabilities overdue | Shows technical exposure |
| Access reviews completed | Shows identity and access management (IAM) governance |
| Incident containment time | Shows response capability |
| Backup restore success | Shows resilience |

### Improvement

| Metric | Purpose |
|---|---|
| Audit findings overdue | Shows corrective-action discipline |
| Repeat findings | Shows root-cause weakness |
| Improvement backlog age | Shows whether improvements are acted on |

## Example status logic

| Status | Criteria |
|---|---|
| Green | Within threshold and no significant trend concern |
| Amber | Threshold approaching or negative trend |
| Red | Threshold exceeded or management decision required |

## Evidence

- dashboard export
- data source definitions
- threshold definitions
- management review minutes
- action tracker

## Related continual improvement lifecycle guidance

Use the dashboard to track improvement health. See:

- [Continual Improvement Metrics](../23-continual-improvement/continual-improvement-metrics.md)
- [Improvement Backlog](../23-continual-improvement/improvement-backlog.md)
- [Improvement Prioritization](../23-continual-improvement/improvement-prioritization.md)


## Practical example

At the quarterly governance meeting, the dashboard shows "aging accepted risks" trending amber for two consecutive quarters and three controls without evidence flagged red. Because the thresholds and escalation rules were defined in advance, the committee does not debate the data — it assigns the risk owners a re-review deadline and directs assurance testing at the unevidenced controls, recording both decisions in the action tracker for follow-up on the next dashboard.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
