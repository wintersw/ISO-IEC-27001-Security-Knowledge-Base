---
title: Backup Corruption
description: Worked risk scenario: Backup Corruption.
category: Worked Risk Scenarios
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - risk-scenario
  - worked-example
---

# Backup Corruption

## Risk statement

> Backups are incomplete or corrupted and cannot support recovery after an incident.

## Assets and context

Backup sets, recovery platform, critical databases.

The assessor should identify a business owner, technical owner, affected services, data classification, dependencies, and existing recovery requirements.

## Threat and cause

The scenario may be initiated by technical failure, ransomware, operational error. The risk is increased by untested restores, weak isolation, incomplete scope.

## Business impact

Potential impacts include extended outage, data loss, regulatory and contractual impact. Impact should be assessed in the organization's own financial, operational, legal, safety, privacy, and reputational language.

## Existing-control review

Relevant controls may include backup monitoring, isolated copies, restore testing, ownership, retention. The assessor should test whether these controls cover the complete population, operate at the required frequency, produce evidence, and address the actual scenario.

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

Useful indicators include restore success, backup coverage, failed jobs, RTO/RPO achievement. Metrics should be interpreted with scope and coverage information.

## Review triggers

Review after a related incident, major architecture change, supplier change, control failure, audit finding, new threat intelligence, or change in business impact.
