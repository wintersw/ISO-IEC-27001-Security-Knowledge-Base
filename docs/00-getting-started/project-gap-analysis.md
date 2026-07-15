---
title: Project Structure Gap Analysis
description: Comparison between the planned documentation architecture and the current repository structure.
category: Getting Started
difficulty: Beginner
applies_to:
  - ISO/IEC 27001:2022
tags:
  - architecture
  - gap-analysis
---

# Project Structure Gap Analysis

This page records the architectural comparison between the project vision developed in the chat and the generated repository.

## Target architecture from the planning discussion

The agreed documentation project should include:

- Getting started and learning paths
- Information security fundamentals
- Governance, risk, and compliance
- ISO/IEC 27000-family content
- ISO/IEC 27001 clauses and certification guidance
- information security management system (ISMS) operating model and best practices
- Risk management
- Annex A control catalog and detailed control pages
- Security-domain guidance
- Auditing and assurance
- Implementation guides for different organization types
- Templates and checklists
- Labs and examples
- Diagrams
- Framework mappings
- Glossary, FAQ, and references

## Gaps found in the previous project version

The previous repository already contained a good foundation, but it was missing or underdeveloped in these areas:

| Area | Gap | Action taken in this version |
|---|---|---|
| Fundamentals | Missing Zero Trust, defense in depth, least privilege, security by design, AAA, and authenticity/accountability/non-repudiation | Added dedicated pages |
| ISO 27k family | Needed deeper pages for ISO 27002, 27005, 27017/27018, 27701, 27035, 27031, and 27036 | Added detailed pages |
| ISMS | Needed stronger operating practices, responsible, accountable, consulted, and informed (RACI), document hierarchy, exceptions, evidence model, and objective management | Added detailed ISMS best-practice pages |
| Implementation | Missing greenfield, small or medium-sized enterprise (SME)/startup, enterprise, software as a service (SaaS)/cloud, and development, security, and operations (DevSecOps) implementation guides | Added implementation guide chapter |
| Security domains | Missing network, endpoint, supplier, privacy, secure development, asset management, and data protection domains | Added domain pages |
| Mappings | Missing NIST CSF, CIS Controls, SOC 2, General Data Protection Regulation (GDPR), ISO 22301, and OWASP mapping pages | Added mapping chapter |
| Templates | Needed exception register, supplier assessment, incident report, evidence register, business impact analysis (BIA), DR plan, and RACI templates | Added templates |
| Checklists | Needed onboarding/offboarding, supplier review, backup restore, cloud security, management review, internal audit, and change review | Added checklists |
| FAQ | Missing beginner and practitioner FAQ | Added FAQ chapter |

## Design principle

The repository now follows the principle discussed in the chat:

> Explain the concept first, then the ISO perspective, then the practical implementation, then evidence and audit expectations.

This keeps the content useful for both newcomers and experienced ISO 27k practitioners.


## Practical example

A new security lead uses this guidance to decide the next implementation step, assigns an owner, and records the decision so later work can be traced to an agreed plan.

## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- approved implementation decision or plan
- assigned actions and owners
- review notes showing why the chosen approach was proportionate

Intent documents are insufficient on their own; retain scoped operating records, approvals, exceptions, and verified follow-up.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
