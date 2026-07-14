---
title: Customer Data Breach
description: A breach case from detection through investigation, notification, corrective action, and management review.
category: End-to-End Case Studies
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - case-study
  - implementation
  - iso27001
---

# Customer Data Breach

## Scenario

A security analyst detects an unusually large export from the customer support platform at 02:15. The account belongs to a support contractor. The contractor confirms that they did not perform the export.

## Detection and triage

The incident manager classifies the event as a potential high-severity data breach. The team preserves identity logs, application audit logs, endpoint telemetry, export records, and the relevant supplier account history.

The account is disabled, sessions are revoked, and export capability is temporarily restricted.

## Investigation

The data-flow map shows that the support platform contains customer names, email addresses, ticket content, and limited contract metadata.

Investigation establishes that:

- the contractor reused a password on another site
- multifactor authentication (MFA) was not enforced for the contractor tenant
- the attacker exported records from 37 customers
- the export did not include payment information
- application logs identify the affected records
- no evidence suggests modification or deletion

## Impact assessment

The breach team assesses sensitivity, volume, identifiability, contractual commitments, possible phishing harm, and jurisdiction.

The legal and privacy team uses the breach notification decision record. Customer contracts require notification within 24 hours for confirmed unauthorized access. The team prepares a factual notice explaining known impact, containment, and recommended customer actions.

## Evidence preservation

Each artifact receives an evidence ID, hash or integrity record where appropriate, collector, collection time, storage location, and chain-of-custody history.

## Root cause

The immediate cause was credential compromise. Root causes include:

- contractor identities were managed outside the main identity platform
- MFA exceptions had no expiry
- support exports did not require step-up authentication
- contractor access was not included in the quarterly access review

## Corrective actions

- migrate contractor access to central identity
- enforce MFA
- require step-up authentication for bulk export
- add export anomaly alerts
- include contractors in access review
- revise supplier onboarding
- update the breach tabletop scenario

## information security management system (ISMS) updates

The risk register is updated to reflect third-party identity risk. The SoA implementation description for access control, identity management, authentication, supplier security, logging, monitoring, incident response, and evidence collection is updated.

## Management review

Management receives a report covering timeline, customer impact, costs, control failures, corrective actions, and resource needs. It approves additional identity-engineering capacity and requires effectiveness review after the next access-review cycle.

## Lessons

The strongest control improvement was not another policy. It was removing a separate identity path that bypassed normal lifecycle controls.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** This chapter explains **Customer Data Breach** without reproducing standard text. Determine formal obligations from the applicable clauses, scope, risk treatment, Statement of Applicability, and binding legal or contractual requirements.
- **Implementation guidance:** Adapt the described roles, frequency, workflow, and evidence to the organization.
- **Best practice:** Enhancements are optional unless adopted through policy, contract, or risk treatment.

## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- local assumptions and scope
- decision and risk rationale
- implementation records
- review showing which lessons were adopted

Intent documents are insufficient on their own; retain scoped operating records, approvals, exceptions, and verified follow-up.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
