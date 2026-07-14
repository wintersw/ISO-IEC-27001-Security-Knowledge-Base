---
title: Lab 1 — Define an ISMS Scope
description: Guided scope-definition exercise for a growing technology company.
category: Guided Labs
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - lab
  - workshop
  - practical
---

# Lab 1 — Define an ISMS Scope

## Scenario

BrightDesk Ltd. develops a cloud-based helpdesk platform. It has 80 employees, uses a public cloud provider, outsources payroll, and operates from one office plus remote locations. The organization wants certification for the service customers buy.

Marketing websites are hosted separately. Finance uses an unrelated accounting SaaS platform. Customer support can access production customer tickets. Development and production use separate cloud accounts.

## Learning objectives

By completing the lab, you should be able to:

- define clear organizational and technical boundaries
- identify interfaces and dependencies
- avoid vague or misleading certification scope
- link scope to interested parties and assets

## Tasks

1. Draft a one-paragraph scope statement.
2. List included organizational units.
3. List included systems and suppliers.
4. List exclusions and justify them.
5. Identify at least five interfaces or dependencies.
6. Identify three interested parties whose requirements affect scope.

## Expected deliverables

- completed ISMS scope statement
- boundary table
- interface/dependency list
- interested-party list

## Suggested answer

A reasonable scope includes the design, development, operation, support, and security of the BrightDesk SaaS service; the production and development cloud environments; source-code and CI/CD services; customer support systems; identity services; employee endpoints used by scoped teams; and critical suppliers supporting the service.

Payroll can be excluded from direct scope while remaining an interface because HR joiner/mover/leaver data affects identity lifecycle. The marketing website may be excluded if it does not process customer-service data, but shared identity, DNS, and incident-response dependencies should be documented.

## Review questions

- Would a customer reasonably believe the support process is included?
- Are remote workers inside the organizational boundary?
- Are outsourced cloud and CI/CD providers addressed?
- Are exclusions framed as exclusions from certification scope rather than absence of risk?
