---
title: Metrics and Management Review
description: Practical ISMS guidance for Metrics and Management Review.
category: ISMS
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - isms
---

# Metrics and Management Review

Metrics should support decisions. Counting activities without evaluating outcomes can create false confidence.

## Why this matters

Poor measures hide missing populations and reward activity without showing whether risk changed. Management review turns reliable performance information into decisions about the ISMS's continuing suitability, adequacy, and effectiveness.

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

1. Map each security objective and material risk to a decision-quality indicator and accountable recipient.
2. Specify the population, source, calculation, threshold, frequency, exclusions, and data-quality checks.
3. Prepare all required management-review inputs, showing trends and unresolved actions rather than isolated snapshots.
4. Record decisions on improvements, ISMS changes, resources, risk, and corrective actions with owners and dates.
5. Track outputs to completion and test whether the decisions produced the intended result.

## Best practices

- Reconcile every metric to its complete population and report missing data separately.
- Present trends, tolerances, uncertainty, exceptions, and business impact together.
- Reserve management-review time for decisions; distribute routine status beforehand.
- Escalate overdue review outputs through defined governance channels.

## Evidence examples

- measurement specification and data lineage
- population reconciliation and data-quality result
- threshold breach, decision, and follow-up record
- management-review input pack, attendees, decisions, actions, and effectiveness follow-up


## Management-cycle example

The quarterly pack shows 98% endpoint coverage, but reconciliation reveals that the missing 2% contains half of the critical servers. Management rejects the headline result, funds agent deployment, assigns the infrastructure owner, and requires a verified population report at the next review.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
