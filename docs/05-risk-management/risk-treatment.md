---
title: Risk Treatment and Residual Risk
description: Practical guidance for Risk Treatment and Residual Risk.
category: Risk Management
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - risk-management
---

# Risk Treatment and Residual Risk

Risk treatment is the decision about what to do with an assessed risk. The four treatment options — modify, retain, avoid, share — are not mutually exclusive; a risk may be treated through a combination of approaches.

## Core content

- **Modify (reduce):** Implement controls that reduce likelihood, impact, or both. This is the most common treatment. Example: deploy MFA to reduce the likelihood of account takeover.
- **Retain (accept):** Acknowledge the risk and choose not to take further action, either because the risk is within appetite or the cost of treatment exceeds the benefit. Requires documented approval by an authorized risk owner.
- **Avoid:** Cease or not start the activity that gives rise to the risk. Example: decide not to store certain categories of data to avoid the associated breach risk.
- **Share (transfer):** Share part of the risk with another party, typically through insurance or contractual terms. Note: risk sharing does not transfer accountability.
- **Residual risk:** The risk remaining after treatment is applied. Must be compared against the organization's risk acceptance criteria and approved by the risk owner.

## Practical implementation

1. For each risk above acceptance criteria, evaluate which treatment option (or combination) is appropriate based on cost, feasibility, effectiveness, and alignment with business objectives.
2. Identify specific controls, actions, or contractual changes needed for the chosen treatment. Link controls to the Statement of Applicability where Annex A controls are involved.
3. Assign a risk owner with authority to approve treatment decisions and accept residual risk.
4. Estimate the residual risk after treatment and compare it with acceptance criteria.
5. If residual risk remains above acceptance criteria, iterate: additional treatment, escalation, or formal risk acceptance with conditions and review triggers.
6. Record all treatment decisions, residual risk levels, approvals, and conditions in the risk register.
7. Monitor implementation of treatment actions and review residual risk after planned intervals or triggering events.

## Example

An e-commerce platform assesses the risk of payment card data interception during transmission. Inherent risk is rated 16 (high impact, moderate likelihood). Treatment combines multiple options: **modify** by enforcing the organization's current secure-transport baseline and network segmentation; **share** by maintaining cyber insurance whose verified coverage includes relevant breach costs; and **avoid** direct card handling through a hosted payment page and tokenization provided by a PCI DSS-validated service provider. Residual risk is reassessed at 6, which falls within acceptance criteria after the authorized business risk owner approves the treatment plan and sets a review trigger for any payment-processor or data-flow change. Outsourcing changes the exposure but does not transfer the organization's accountability for supplier and data-flow risks.

## Evidence

- risk treatment plan with treatment options, assigned controls, owners, and target dates
- residual risk assessments with comparison to acceptance criteria
- risk acceptance records with owner approval, rationale, conditions, and review triggers
- risk register entries showing inherent and residual risk levels and treatment decisions
- SoA updates reflecting control selection through risk treatment

## Common mistakes

- Selecting a treatment option without estimating the residual risk it produces.
- Accepting residual risk without documented owner approval and review conditions.
- Assuming risk transfer (insurance, outsourcing) eliminates accountability or the need for controls.
- Treating risk acceptance as the default for risks that are difficult or expensive to treat.
- Failing to re-evaluate treatment when the threat landscape, technology, or business context changes.


## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
