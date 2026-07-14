---
title: Joiner-Mover-Leaver Control Failure
description: An audit finding that reveals a systemic mover-access weakness.
category: End-to-End Case Studies
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - case-study
  - implementation
  - iso27001
---

# Joiner-Mover-Leaver Control Failure

## Scenario

Internal audit samples twenty employees who changed roles during the previous quarter. Six retained access from their former roles.

## Immediate correction

Managers review the six accounts and remove unnecessary access.

That correction fixes the sample, but it does not address the cause.

## Root-cause analysis

The organization finds that:

- HR records role changes, but IAM receives only termination events
- managers request new access but are not prompted to review old access
- application roles are not mapped to job roles
- quarterly review reports do not identify movers
- service accounts owned by movers are not reassigned

## Corrective action

The organization:

- integrates role-change events from HR
- adds old-access review to the mover workflow
- creates role mappings for high-risk applications
- adds mover status to quarterly review reports
- adds service-account reassignment
- defines completion metrics and escalation

## Effectiveness review

After two quarters, internal audit samples movers again. It verifies that role-change events generated review tasks, removals were completed, and exceptions were approved.

## Metrics

- movers reviewed within target
- access removed after role change
- mover tasks overdue
- service accounts without current owner
- repeated access-review findings

## Lessons

The failure was not careless managers alone. The process was designed to grant new access without forcing review of old access. Effective corrective action changed the workflow.
