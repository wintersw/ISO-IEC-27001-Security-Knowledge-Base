---
title: Control Assurance Methodology
description: Methodology for testing control design and operating effectiveness.
category: ISMS Professional Toolkit
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - isms
  - professional-toolkit
---

# Control Assurance Methodology

Control assurance determines whether controls are designed appropriately and operating effectively.

Use this methodology with the [Control Assurance Review Checklist](../11-checklists/control-assurance-review.md). The methodology explains how to plan and perform testing; the checklist consolidates the common questions deliberately omitted from individual Annex A pages.

## Assurance dimensions

### Design effectiveness

A control is well designed when it is capable of reducing the intended risk.

Questions:

- Does the control address the relevant risk?
- Is the control owner defined?
- Is the process clear?
- Is the frequency appropriate?
- Is required evidence defined?
- Are exceptions handled?

### Operating effectiveness

A control is operating effectively when it performs consistently over time.

Questions:

- Was the control performed as scheduled?
- Were all required items included?
- Were exceptions identified?
- Were exceptions approved?
- Were remediation actions completed?
- Was evidence retained?

## Testing methods

- document inspection
- sample testing
- reperformance
- system configuration review
- log review
- interview
- walkthrough
- data analytics
- exception trend analysis

## Sampling guidance

| Control frequency | Suggested sample approach |
|---|---|
| Continuous | Sample events across the period |
| Daily/weekly | Sample multiple periods |
| Monthly | Sample several months |
| Quarterly | Sample at least one or more completed cycles |
| Annual | Test the completed annual activity |

## Control test record

| Field | Description |
|---|---|
| Control ID | Control being tested |
| Test objective | What the test verifies |
| Population | Full set being tested |
| Sample | Items selected |
| Method | Inspection, interview, reperformance, etc. |
| Result | Pass / fail / partial |
| Finding | Gap identified |
| Evidence | Source records |
| Tester | Person performing test |
| Date | Test date |

## Common mistakes

- Testing only whether a policy exists.
- Testing one screenshot without verifying population completeness.
- Accepting management statements without supporting evidence.
- Not distinguishing design gaps from operating failures.
- Not following up on repeat failures.
- Treating a high completion rate as evidence of effectiveness without checking population coverage, timeliness, exceptions, failures, and the intended security outcome.

## Output

Control assurance should produce:

- test results
- findings
- improvement actions
- evidence quality observations
- updates to risks and SoA where needed

## Related continual improvement lifecycle guidance

Control assurance failures should trigger improvement or corrective action. See:

- [Improvement Sources](../23-continual-improvement/improvement-sources.md)
- [Effectiveness Review](../23-continual-improvement/effectiveness-review.md)
- [Improvement Backlog Review Checklist](../11-checklists/improvement-backlog-review-checklist.md)


## Practical example

An assurance tester evaluates the quarterly access review control. Design testing confirms the control has an owner, a defined frequency, and required evidence. For operating effectiveness, the tester samples two completed quarters, reperforms the review for one system, and finds that terminated users appeared in the population but the review only covered active directory accounts — a design gap, not an operating failure. The result is recorded in the control test record with a finding, and the SoA and risk register are updated.

## Evidence to retain

Retain records showing both test design and execution, such as:

- completed control test records with population, sample, and method
- source evidence inspected during testing (reports, logs, configurations)
- findings with the design-vs-operating classification
- remediation actions and retest or effectiveness-verification results


## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
