---
title: Lab 4 — Test an Access Review Control
description: Control-testing exercise for quarterly application access review.
category: Guided Labs
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - lab
  - workshop
  - practical
---

# Lab 4 — Test an Access Review Control

## Scenario

A quarterly review covers 420 users. The application owner signed a spreadsheet stating that access was reviewed. Twelve users were marked for removal.

## Tasks

1. Define the control objective.
2. Identify the population.
3. Select a sample.
4. Test design effectiveness.
5. Test operating effectiveness.
6. Identify missing evidence.
7. Draft a conclusion.

## Suggested testing steps

- confirm the export came from the authoritative application
- reconcile the population to active identities
- check whether service accounts were included
- verify reviewer authority
- sample retained-access decisions
- verify all twelve removals through completed tickets
- check timing
- review exceptions

## Example conclusion

The control was designed appropriately but not fully effective because three removal decisions remained open forty-five days after review. The review document alone did not prove remediation.

## Review questions

- Was population completeness tested?
- Was remediation tested?
- Did the control include privileged and service accounts?
- Is the issue a correction, corrective action, or both?
