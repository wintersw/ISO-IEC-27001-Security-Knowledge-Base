---
title: Metrics and Management Review
description: Practical ISMS guidance for Metrics and Management Review.
---

# Metrics and Management Review

Metrics should support decisions. Counting activities without evaluating outcomes can create false confidence.

## Why this matters

The ISMS is the operating system of the security program. It turns isolated controls into a managed, measurable, and continually improving system.

## Key elements

- Objectives
- Inputs
- Metrics
- Decisions
- Actions
- Follow-up

## Design measurement from the decision backward

A measurement programme should begin with an information need: the decision or uncertainty that management must resolve. It then defines the measured population, raw observations, calculation, interpretation threshold, owner, frequency, data-quality checks, and action when the result is outside tolerance.

| Layer | Plain-language meaning | Example |
|---|---|---|
| Information need | What a decision-maker needs to know | Are critical vulnerabilities being reduced before exposure becomes unacceptable? |
| Base measure | A direct observation or count | discovery date, remediation date, affected critical assets |
| Derived measure | A calculation using base measures | median remediation time for critical assets |
| Indicator | A result interpreted against a target or threshold | red when overdue exposure exceeds the approved tolerance |
| Evaluation | A conclusion and decision | add capacity, change priority, accept risk, or redesign the process |

Define the denominator and exclusions. “95% compliant” is not decision-quality information unless the complete population, missing records, age of data, approved exceptions, and business criticality are visible.

### Measure-design example

A dashboard reports patch compliance. Management asks whether high-impact services remain exposed, not simply how many devices passed. The metric owner reconciles the vulnerability scanner with the asset inventory, reports missing agents separately, weights overdue items by criticality and external exposure, and records the remediation or risk decision made at review.

## Practical implementation

1. Define the purpose and scope of the activity.
2. Assign an accountable owner.
3. Document the minimum process needed for repeatability.
4. Embed the activity into business or security workflows.
5. Define evidence before the process goes live.
6. Review performance at a planned interval.
7. Improve based on incidents, audits, changes, and metrics.

## Best practices

- Keep documentation proportional to complexity and risk.
- Separate policy from procedure.
- Use workflow tools to retain evidence.
- Assign risk acceptance to business risk owners.
- Use management review for decisions, not status reporting only.
- Track exceptions and overdue actions.

## Evidence examples

- approved document or process description
- owner assignment
- review records
- meeting minutes
- action tracker
- metric report
- exception register
- audit trail
- measurement specification and data lineage
- population reconciliation and data-quality result
- threshold breach, decision, and follow-up record


## Management-cycle example

The information security management system manager applies this guidance during the annual planning cycle, assigns accountable owners, connects the activity to risks and objectives, and schedules an effectiveness review.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
