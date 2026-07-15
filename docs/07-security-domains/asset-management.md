---
title: Security Asset Management
description: Asset management practices for ISO 27001 security teams.
category: Security Domains
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - security-domain
---

# Security Asset Management

Asset management identifies what must be protected and who is accountable for it.

## Key asset types

- information
- applications
- infrastructure
- cloud resources
- software as a service (SaaS) platforms
- endpoints
- suppliers
- facilities
- records
- knowledge


## Evidence

- asset register
- configuration management database (CMDB)
- cloud inventory
- owner review records
- lifecycle records

## Detailed implementation guidance

Asset management provides the foundation for risk, vulnerability management, incident response, continuity, access control, and audit. The objective is not to build the largest possible inventory. It is to maintain enough accurate information to make security decisions.

Assets include information, data sets, applications, cloud services, APIs, infrastructure, endpoints, identities, keys, suppliers, facilities, and business services.

### Example

Automated cloud discovery identifies a database with no owner. The asset process determines which service uses it, assigns a business and technical owner, records data classification and criticality, links it to backup and vulnerability processes, and confirms whether it is still required.

### Best practices

- define authoritative sources by asset type
- combine automated discovery with owner validation
- record ownership and business service
- include cloud, SaaS, data, service accounts, and APIs
- track lifecycle status
- reconcile inventories
- treat missing ownership as a finding
- link assets to recovery, risks, controls, and suppliers
- retire assets through controlled workflows

### Evidence and metrics

Evidence includes inventories, discovery reports, owner attestations, reconciliation results, retirement records, and exception logs. Useful metrics include critical assets without owners, stale records, discovered-but-unregistered assets, and retired assets still reachable.

## Related chapters

- [Asset, Data, and Service Lifecycle](../31-security-lifecycle-management/asset-data-service-lifecycle.md)
- [Configuration Management and CMDB](../32-it-governance-and-itsm/configuration-management-and-cmdb.md)

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Asset management is addressed through Annex A controls A.5.9 (inventory of information and associated assets), A.5.10 (acceptable use), A.5.11 (return of assets), A.5.12 (classification), and A.5.13 (labelling). The organisation must identify assets within the ISMS scope, assign ownership, and maintain an inventory that supports risk assessment and control implementation.
- **Implementation guidance:** Define asset categories, mandatory metadata fields (owner, classification, location, criticality), and an update trigger (onboarding, change, decommissioning). Integrate the asset inventory with risk assessment, vulnerability management, and incident response.
- **Best practice:** Use automated discovery to validate the inventory against operational reality. An inventory that exists only as a spreadsheet and is never reconciled with what is actually deployed provides false assurance.

## Practical example

An organisation discovers unmanaged cloud databases during an automated asset scan. The team assigns owners, records data classification and criticality, links each asset to its supporting service, and triggers risk assessment for any asset with an unknown owner.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
