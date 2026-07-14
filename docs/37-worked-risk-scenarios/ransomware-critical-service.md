---
title: Ransomware Affecting a Critical Service
description: Worked risk scenario: Ransomware Affecting a Critical Service.
category: Worked Risk Scenarios
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - risk-scenario
  - worked-example
---

# Ransomware Affecting a Critical Service

## Risk statement

> Ransomware encrypts production systems and accessible backups, interrupting customer service and creating recovery uncertainty.

## Assets and context

Critical customer service, production servers, backup platform.

The assessor should identify a business owner, technical owner, affected services, data classification, dependencies, and existing recovery requirements.

## Threat and cause

The scenario may be initiated by phishing or exposed service. The risk is increased by weak segmentation, excessive privilege, accessible backups.

## Business impact

Potential impacts include service outage, lost revenue, contractual penalties, recovery cost. Impact should be assessed in the organization's own financial, operational, legal, safety, privacy, and reputational language.

## Existing-control review

Relevant controls may include MFA, EDR, segmentation, immutable backups, restore tests, incident playbook. The assessor should test whether these controls cover the complete population, operate at the required frequency, produce evidence, and address the actual scenario.

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

Useful indicators include restore success, privileged access anomalies, critical EDR coverage, recovery test findings. Metrics should be interpreted with scope and coverage information.

## Review triggers

Review after a related incident, major architecture change, supplier change, control failure, audit finding, new threat intelligence, or change in business impact.
