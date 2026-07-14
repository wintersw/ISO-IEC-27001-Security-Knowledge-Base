---
title: Lab 5 — Investigate a Mock Data Breach
description: Breach-response exercise covering evidence, impact, notification, and improvement.
category: Guided Labs
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - lab
  - workshop
  - practical
---

# Lab 5 — Investigate a Mock Data Breach

## Scenario

An administrator account downloads 18,000 customer records at 01:40. The user says they were asleep. MFA logs show approval from an unfamiliar device.

## Tasks

1. Classify the incident.
2. Define containment actions.
3. List evidence to preserve.
4. Draft a timeline.
5. Assess data impact.
6. Identify escalation parties.
7. Record a notification decision.
8. Propose corrective actions.

## Suggested containment

- disable the account
- revoke sessions and tokens
- block the device
- restrict bulk export
- preserve logs
- search for related activity
- identify affected records

## Suggested evidence

- identity logs
- MFA events
- application audit logs
- endpoint telemetry
- data-export record
- network logs
- support tickets
- administrator role history

## Suggested root-cause questions

- Was MFA fatigue involved?
- Why did one administrator have bulk export?
- Were unusual downloads monitored?
- Was step-up authentication required?
- Was the device managed?
- Were access reviews effective?

## Review questions

- Which actions preserve evidence?
- Which actions could destroy evidence?
- What facts are needed before external notification?
- Which ISMS documents should be updated?
