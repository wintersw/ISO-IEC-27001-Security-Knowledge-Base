---
title: SME and Startup Implementation Guide
description: Practical ISO 27001 implementation guidance for small teams.
category: Implementation
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - implementation
---

# small or medium-sized enterprise (SME) and Startup Implementation Guide

Small organizations should avoid over-engineering the information security management system (ISMS).

The objective is not to imitate a large enterprise. It is to create a small, dependable management system that protects the services on which the organization depends, makes risk decisions visible, and produces evidence as part of normal work.

## Recommended approach

- Keep the scope clear and realistic.
- Use lightweight but controlled documentation.
- Assign named owners even if people hold multiple roles.
- Use existing tools for evidence where possible.
- Focus on high-risk areas first: identity and access management (IAM), backups, vulnerability management, incident response, supplier security, and logging.

## Risk-based implementation sequence

1. Identify the services, information, people, suppliers, and technology whose loss or compromise could stop the business or harm customers.
2. Stabilize urgent basics: supported systems, secure administration, multifactor authentication, recoverable backups, patching, incident contacts, and controlled remote access.
3. Document scope, obligations, risks, owners, and treatment decisions only to the level needed for consistent operation and review.
4. Reuse service-management, ticketing, identity, finance, and cloud records as evidence instead of building parallel evidence processes.
5. Add depth where risk, customer commitments, incidents, or assurance results show that the minimum is insufficient.

This sequence is implementation guidance, not a substitute for evaluating every applicable ISO/IEC 27001 requirement and every necessary risk treatment.

## Make trade-offs explicit

A small team will not implement every improvement at once. Record what is deferred, the exposure created, the temporary safeguard, the authorized risk owner, and the review or expiry date. A constrained but governed decision is stronger than an undocumented claim that a control exists.

## Minimum viable ISMS

- scope statement
- policy
- asset inventory
- risk methodology
- risk register
- SoA
- treatment plan
- core procedures
- internal audit
- management review
- corrective action process

## Common mistakes

- buying governance, risk, and compliance (GRC) tools before defining processes
- copying enterprise policies
- ignoring software as a service (SaaS) and cloud dependencies
- waiting until the audit to collect evidence

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** This chapter explains **SME and Startup Implementation Guide** without reproducing standard text. Determine formal obligations from the applicable clauses, scope, risk treatment, Statement of Applicability, and binding legal or contractual requirements.
- **Implementation guidance:** Adapt the described roles, frequency, workflow, and evidence to the organization.
- **Best practice:** Enhancements are optional unless adopted through policy, contract, or risk treatment.

## Practical example

A 25-person software provider depends on a cloud hosting service, a source repository, and a customer-support platform. It first protects administrator accounts with multifactor authentication, verifies restoration from isolated backups, removes unsupported endpoints, and documents incident contacts. The next quarter it formalizes supplier review and centralized logging. Deferred improvements are recorded with compensating controls and expiry dates rather than hidden in an informal backlog.

## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- approved plan and scope
- milestones, owners, and dependencies
- completed work records
- review results and accepted deviations

Intent documents are insufficient on their own; retain scoped operating records, approvals, exceptions, and verified follow-up.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
