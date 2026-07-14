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
- SaaS platforms
- endpoints
- suppliers
- facilities
- records
- knowledge

## Best practices

- Define required metadata.
- Reconcile automated discovery with business ownership.
- Include SaaS and cloud resources.
- Assign owners.
- Link critical assets to risks.
- Review critical assets frequently.

## Evidence

- asset register
- CMDB
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
