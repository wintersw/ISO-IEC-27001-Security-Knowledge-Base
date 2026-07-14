---
title: Lab 2 — Conduct a Full Risk Assessment
description: Worked risk assessment for a customer data warehouse.
category: Guided Labs
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - lab
  - workshop
  - practical
---

# Lab 2 — Conduct a Full Risk Assessment

## Scenario

A cloud data warehouse contains customer profiles, transaction summaries, support data, and product telemetry. Analysts authenticate through SSO. Twenty analysts have broad read access. Exports are allowed. Logging exists, but nobody reviews bulk-download activity.

## Tasks

1. Identify assets and owners.
2. Write three risk scenarios.
3. Identify existing controls.
4. Score impact and likelihood using a five-level method.
5. Select treatment options.
6. Identify Annex A controls.
7. Define residual-risk monitoring.

## Suggested risk scenario

> A compromised analyst account exports large volumes of customer data because access is broad and unusual download behavior is not monitored, causing customer harm, contractual breach, regulatory exposure, and loss of trust.

## Suggested treatment

- redesign access by business role
- introduce MFA or step-up authentication
- add bulk-export alerts
- review access quarterly
- require approval for high-volume export
- mask sensitive fields where full values are unnecessary
- retain data-access logs

## Suggested evidence

- role design
- access approval
- quarterly review record
- SIEM alert configuration
- export approval ticket
- masking test
- risk-owner approval

## Review questions

- Did you separate inherent and residual risk?
- Did you assign a business risk owner?
- Does each treatment action have evidence?
- Would the selected metrics reveal control failure?
