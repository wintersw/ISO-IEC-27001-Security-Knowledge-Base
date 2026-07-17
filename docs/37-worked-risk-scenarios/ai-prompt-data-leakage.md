---
title: AI Prompt and Data Leakage
description: "Worked risk scenario: AI Prompt and Data Leakage."
category: Worked Risk Scenarios
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - risk-scenario
  - worked-example
---

# AI Prompt and Data Leakage
## Risk statement

> Sensitive information enters an AI prompt or is disclosed through generated output.

## Assets and context

Prompts, model provider, vector store, customer data.

The assessor should identify a business owner, technical owner, affected services, data classification, dependencies, and existing recovery requirements.

## Threat and cause

The scenario may be initiated by user error, prompt injection, model behavior. The risk is increased by weak data controls, broad retrieval, provider retention.

## Business impact

Potential impacts include privacy breach, IP loss, customer exposure. Impact should be assessed in the organization's own financial, operational, legal, safety, privacy, and reputational language.

## Existing-control review

Relevant controls may include data minimization, filtering, tenant isolation, provider controls, output validation. The assessor should test whether these controls cover the complete population, operate at the required frequency, produce evidence, and address the actual scenario.

## Treatment approach

A complete treatment plan should:

1. reduce the most important causal weaknesses
2. assign owners and dates
3. define compensating controls where immediate remediation is impossible
4. update the Statement of Applicability if control implementation changes
5. define residual-risk approval
6. specify verification evidence

## Example evidence

- asset and owner record
- risk assessment and treatment plan
- architecture or data-flow record
- policy and procedure
- technical configuration
- operating logs or tickets
- control test
- exception or risk acceptance
- management decision

## Monitoring indicators

Useful indicators include sensitive prompt detections, blocked attacks, human rejection, cross-tenant tests. Metrics should be interpreted with scope and coverage information.

## Worked decision

| Field | Illustrative entry |
|---|---|
| Inherent | 4 × 4 = 16 (high): staff routinely handle customer and source-code data |
| Finding | The approved tenant disables provider training, but unsanctioned AI use exists and retrieval permissions exceed source permissions |
| Treatment | Block unsanctioned services, label prompt-eligible data, reduce retrieval scope, and test injection and output leakage |
| Target | 8 (moderate); AI product owner; controls due before external rollout |
| Acceptance | Privacy and security owners approve remaining provider and model uncertainty after tests pass |

## Review triggers

Review after a related incident, major architecture change, supplier change, control failure, audit finding, new threat intelligence, or change in business impact.


## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- validated scenario and affected assets
- likelihood and impact rationale
- treatment decision and owner
- residual-risk approval and review trigger


## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
