---
title: Generic Mobile / SaaS Risk Example
description: Generic non-country-specific example inspired by the uploaded case structure.
category: Ethics and Framework Relationships
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
  - ISO/IEC 27000 family
tags:
  - ethics
  - standards
  - isms
---

# Generic Mobile / software as a service (SaaS) Risk Example

This page provides a generalized example based on the structure of the uploaded paper, excluding Austria-specific content.

## Scenario

A small software company operates a mobile and web application. The application synchronizes content between a central server and user devices. Users can authenticate, store preferences, add notes, and access offline content.

## Assets

- mobile application
- web application
- application programming interface (API) services
- application server
- database server
- user devices
- payment provider integration
- administrative workstation
- source code repository
- cloud hosting environment

## Security objectives

| Asset | Confidentiality | Integrity | Availability | Notes |
|---|---|---|---|---|
| User account data | High | High | Normal | Privacy relevance |
| User notes | High | High | Normal | Potential sensitive content |
| API services | High | High | High | Core synchronization function |
| Database | Very high | High | High | Central data store |
| Mobile client | High | High | High | Offline use and local data |
| Payment integration | Very high | High | Normal | Usually handled by provider |

## Example risks

| Risk | Treatment |
|---|---|
| Unauthorized access to user notes | strong authentication, encryption, access control |
| API injection attack | input validation, secure coding, testing |
| Compromised administrator account | multifactor authentication (MFA), privileged access management (PAM), logging, access review |
| Loss of local device data | device encryption, secure storage, session timeout |
| Cloud misconfiguration | cloud baseline, monitoring, review |
| Payment data exposure | outsource payment handling, supplier assurance |

## Example controls

- secure authentication
- encryption in transit and at rest
- API authorization
- vulnerability management
- secure development lifecycle
- logging and monitoring
- supplier assurance
- backup and restore testing
- incident response


## Evidence to retain

Retain records showing both design decisions and actual operation, such as:

- framework-selection rationale
- stakeholder and obligation analysis
- approved governance decision
- review showing the approach remains suitable

Intent documents are insufficient on their own; retain scoped operating records, approvals, exceptions, and verified follow-up.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
