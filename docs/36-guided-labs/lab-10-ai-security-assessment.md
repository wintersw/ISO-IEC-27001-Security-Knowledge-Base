---
title: Lab 10 — Assess an AI System
description: Security and privacy review for an LLM-enabled internal assistant.
category: Guided Labs
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - lab
  - workshop
  - practical
---

# Lab 10 — Assess an artificial intelligence (AI) System

## Scenario

An internal assistant will search company policies, architecture documents, support procedures, and selected customer tickets. It can draft answers but cannot send messages automatically.

## Tasks

1. inventory components and data
2. identify threats
3. assess supplier risk
4. define security requirements
5. define test cases
6. define monitoring
7. identify evidence

## Suggested threats

- prompt injection
- sensitive-data disclosure
- cross-user data leakage
- poisoned knowledge documents
- insecure output handling
- excessive service permissions
- provider retention
- vector-database exposure

## Suggested tests

- malicious instruction in a knowledge document
- request for another department's restricted content
- attempt to reveal system prompt
- prompt containing personal data
- oversized request causing resource exhaustion
- unsafe generated command

## Suggested evidence

- AI inventory
- data inventory
- threat model
- supplier assessment
- test report
- approval
- logging configuration
- incident playbook

## Review questions

- Is human approval meaningful?
- Are data and model lineage documented?
- Can the assistant retrieve content outside authorization?
- Is retirement/deletion planned?

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** This chapter explains **Lab 10 — Assess an AI System** without reproducing standard text. Determine formal obligations from the applicable clauses, scope, risk treatment, Statement of Applicability, and binding legal or contractual requirements.
- **Implementation guidance:** Adapt the described roles, frequency, workflow, and evidence to the organization.
- **Best practice:** Enhancements are optional unless adopted through policy, contract, or risk treatment.

## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- completed lab output
- assumptions and decision rationale
- review feedback
- revised result and lessons learned

Intent documents are insufficient on their own; retain scoped operating records, approvals, exceptions, and verified follow-up.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
