---
title: AI Customer Support System
description: A secure and privacy-aware implementation of an AI assistant for customer support.
category: End-to-End Case Studies
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - case-study
  - implementation
  - iso27001
---

# artificial intelligence (AI) Customer Support System

## Scenario

A company wants to deploy an AI assistant that summarizes support tickets, drafts replies, and searches internal knowledge.

## Use-case definition

The system may process customer names, ticket text, technical logs, and internal support procedures. It is not allowed to make account changes, issue refunds, or send replies without human approval.

## Asset and data inventory

The AI system inventory records:

- model provider
- prompt orchestration service
- support platform integration
- vector database
- knowledge documents
- prompt and output logs
- evaluation datasets
- service identities

The data inventory identifies personal data, customer confidential information, internal procedures, and secrets that must not enter prompts.

## Threat modeling

Key threats include:

- prompt injection in customer messages
- disclosure of another customer's content
- sensitive data in prompts or logs
- unsafe generated instructions
- compromised plugins or tools
- excessive model permissions
- insecure vector-store access
- provider retention of prompts

## Controls

- tenant-aware retrieval
- content and prompt filtering
- restricted tool permissions
- human approval
- data minimization
- contract review
- logging with sensitive-data controls
- red-team testing
- output validation
- rate limiting
- incident playbook
- kill switch

## Privacy engineering

The team removes unnecessary identifiers, limits prompt retention, documents purpose, assesses model-provider processing, and tests whether generated summaries expose sensitive content.

## Secure development and release

Security acceptance criteria are included in the release. Tests cover prompt injection, tenant separation, authorization, logging, and unsafe outputs. The release is approved through change enablement.

## Monitoring

Metrics include blocked prompt attacks, sensitive-output detections, cross-tenant test results, human rejection rate, unusual tool calls, and incidents.

## Lessons

AI security is not a separate universe. It uses familiar information security management system (ISMS) disciplines—ownership, data classification, supplier review, threat modeling, access control, logging, incident response, change management, and continual improvement—applied to new assets and failure modes.


## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- local assumptions and scope
- decision and risk rationale
- implementation records
- review showing which lessons were adopted

Intent documents are insufficient on their own; retain scoped operating records, approvals, exceptions, and verified follow-up.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
