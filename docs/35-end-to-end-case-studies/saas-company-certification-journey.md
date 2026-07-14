---
title: SaaS Company Certification Journey
description: A complete ISO 27001 implementation and certification scenario for a growing SaaS company.
category: End-to-End Case Studies
difficulty: Advanced
applies_to:
  - ISO/IEC 27001:2022
tags:
  - case-study
  - implementation
  - iso27001
---

# SaaS Company Certification Journey

## Organization

Northstar Cloud is a 140-person software company that provides a multi-tenant workflow platform. Customers increasingly ask for ISO/IEC 27001 certification. The company already has modern cloud infrastructure and good engineers, but its security practices are informal and evidence is inconsistent.

## Step 1 — Define the purpose and scope

Management decides that certification should cover the design, development, operation, and support of the SaaS platform. Corporate marketing websites and an unrelated experimental product are excluded.

The scope statement names:

- the legal entity
- engineering, cloud operations, support, security, HR, and procurement processes
- the production cloud environment
- source-code repositories and CI/CD services
- customer support systems
- offices and remote-work arrangements
- critical suppliers

The team documents interfaces with payroll, finance, and external legal counsel instead of pretending that excluded processes have no effect.

## Step 2 — Understand interested parties

The interested-party register includes customers, employees, regulators, cloud providers, investors, insurers, and certification bodies.

A major customer requires 24-hour incident notification. This becomes a contractual requirement and influences the incident response procedure and supplier contracts.

## Step 3 — Build asset and data inventories

The team identifies services, applications, repositories, cloud accounts, production databases, support tools, endpoints, identity platforms, and suppliers.

Data owners classify customer content as confidential and authentication secrets as restricted. Data-flow mapping reveals that support exports are downloaded to analyst laptops, creating an unmanaged risk.

## Step 4 — Establish risk management

The risk methodology uses five impact and likelihood levels. Risks are written as scenarios.

Example:

> A compromised support account exports customer data from multiple tenants, causing contractual breach, customer harm, and regulatory exposure.

Existing controls include SSO and logging, but support access is too broad. Treatment actions introduce MFA, tenant-scoped access, export alerts, and quarterly access review.

## Step 5 — Build the Statement of Applicability

The SoA lists all Annex A controls and records applicability, justification, implementation status, owner, related risks, and evidence.

A.8.11 Data masking is applicable because support personnel need limited visibility into customer records. A.7.5 protection against physical threats is applicable to the office and remote-equipment storage, but the implementation is proportionate to the small physical footprint.

## Step 6 — Create the minimum policy and process framework

The company creates a concise information security policy plus supporting procedures for:

- risk management
- access control
- incident response
- supplier security
- vulnerability management
- secure development
- change management
- backup and recovery
- document control
- corrective action

Existing ITSM and development workflows are enhanced rather than duplicated.

## Step 7 — Operate controls and collect evidence

Control owners operate quarterly access reviews, monthly vulnerability reporting, supplier reviews, secure-change workflows, backup tests, and incident exercises.

The evidence register defines source, owner, frequency, retention, and storage. System-generated exports are preferred to screenshots.

## Step 8 — Internal audit

The internal auditor samples:

- terminated-user access
- high-risk changes
- critical vulnerability remediation
- supplier onboarding
- incident exercise evidence
- management decisions

A minor nonconformity is raised because two service accounts lack named owners.

## Step 9 — Corrective action

The company does not merely assign owners to the two accounts. Root-cause analysis finds that service-account ownership was not part of the CI/CD onboarding template. The template and cloud provisioning workflow are updated. Effectiveness is checked after sixty days.

## Step 10 — Management review

Management reviews risk trends, audit results, supplier risk, objectives, incidents, resource needs, and certification readiness. It approves a dedicated IAM automation project and accepts a temporary risk for a legacy customer integration.

## Step 11 — Certification readiness

Stage 1 readiness focuses on scope, documented information, risk methodology, SoA, internal audit, and management review.

Stage 2 readiness focuses on whether controls operate and whether evidence is consistent. Control owners are prepared to explain their processes rather than memorize standard language.

## Lessons

- Certification readiness depends on operation, not document volume.
- Scope clarity prevents misleading claims.
- Existing workflows can become ISMS evidence.
- Corrective action should remove root causes.
- Management decisions are part of the evidence.
