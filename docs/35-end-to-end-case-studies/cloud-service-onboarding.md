---
title: Cloud Service Onboarding
description: End-to-end onboarding of a SaaS service with security, privacy, ITSM, supplier, and exit controls.
category: End-to-End Case Studies
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - case-study
  - implementation
  - iso27001
---

# Cloud Service Onboarding

## Scenario

The finance team wants a cloud-based expense-management platform. The service will process employee identity data, bank details, expense receipts, and approval records.

## Business request

The service owner describes the business need, expected users, data, integrations, availability requirements, and target date.

The request triggers security, privacy, procurement, legal, and architecture review.

## Data and risk assessment

The data owner classifies bank details and identity documents as restricted. A data-flow map covers HR import, identity federation, bank export, mobile app upload, analytics, and deletion.

Key risks include:

- over-privileged finance administrators
- insecure mobile receipt uploads
- supplier breach
- uncontrolled subprocessors
- data retained after employee departure
- unavailable service during payroll deadlines

## Supplier due diligence

The review examines:

- security governance and certifications
- SSO and MFA support
- encryption
- audit logs
- data location
- incident notification
- business continuity
- subprocessors
- vulnerability management
- deletion and export
- privileged support access

A certification is treated as evidence, not proof that every required control is in scope.

## Contract requirements

The contract includes:

- security obligations
- incident notification
- audit cooperation
- subprocessor notification
- data return and deletion
- continuity requirements
- termination support
- access-control expectations

## Architecture and configuration

The service uses SSO, MFA, role-based access, restricted administrator roles, audit logging, API integration through approved service identities, and mobile device controls.

## ITSM integration

The service is registered in the service catalogue and CMDB. Support contacts, service owner, criticality, data classification, supplier, recovery expectations, and escalation paths are recorded.

Changes to integrations follow change enablement. Access requests use the standard service-request workflow.

## Go-live acceptance

Evidence includes:

- approved risk assessment
- supplier assessment
- contract clauses
- data-flow map
- configuration screenshots or exports
- access model
- test results
- support and incident procedures
- exit plan

## Ongoing review

The supplier is reviewed annually and after material incidents or service changes. Access is reviewed quarterly. Subprocessor changes are assessed. The exit plan is tested before contract renewal.

## Lesson

Cloud onboarding is not a questionnaire. It is a lifecycle that combines ownership, data, risk, contract, configuration, operation, monitoring, and exit.
