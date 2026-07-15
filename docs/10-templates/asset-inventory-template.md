---
title: Asset Inventory Template
description: Tried-and-tested ISMS template: Asset Inventory Template.
category: Templates
difficulty: Beginner
applies_to:
  - ISO/IEC 27001:2022
tags:
  - template
  - isms-documentation
  - iso27001
---

# Asset Inventory Template

> Based in part on the asset and classification tables in the [ISO 27001:2022 Toolkit](https://github.com/PehanIn/ISO-27001-2022-Toolkit), copyright (c) 2024 Pehan Gunasekara, MIT License. Fields and handling rules have been corrected, generalized, and expanded.

| Asset ID | Asset name | Type | Owner / custodian | Location / authoritative source | Classification | Criticality | Related process / dependencies | Required controls | Retention / lifespan | Lifecycle status | Last updated / next review |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AST-001 |  | Information / software / hardware / service / supplier / facility |  |  | Public / Internal / Confidential / Restricted | Low / Medium / High / Critical |  | Access / encryption / backup / monitoring |  | Planned / Active / Retiring / Disposed |  |

## Classification handling profile

Define these rules in the organization's classification policy; do not assume a label alone protects information.

| Classification | Marking | Storage and access | Transmission | Backup | Disposal |
|---|---|---|---|---|---|
| Restricted | [Required marking] | [Named roles, approved repositories, strong access controls] | [Approved encrypted channels and recipient checks] | [Encrypted, access-controlled, restore-tested] | [Verified secure deletion or destruction] |
| Confidential |  |  |  |  |  |
| Internal |  |  |  |  |  |
| Public |  |  |  |  |  |

## Criticality decision table

Do not assign criticality from intuition alone. Define levels using the organization's impact and recovery criteria, then record the rationale in or alongside the inventory.

| Criticality | Decision characteristics | Typical governance response |
|---|---|---|
| Critical | Loss or prolonged unavailability could exceed tolerance, threaten essential services, cause severe legal or safety consequences, or create systemic dependency failure | named executive or service owner, stringent recovery objectives, dependency mapping, tested resilience and enhanced monitoring |
| High | Material operational, contractual, financial, privacy, or reputational impact is plausible but essential operations can continue temporarily | documented recovery priority, strong access and change controls, scheduled control assurance |
| Medium | Manageable disruption or information impact can be recovered through normal escalation and established procedures | standard controls, owned recovery and review schedule |
| Low | Limited localized impact with straightforward replacement or recovery | baseline controls and proportionate review |

Classification describes sensitivity and handling; criticality describes business consequence and recovery priority. Keep them as separate fields.

## Usage guidance

Include:

- information assets
- applications
- infrastructure
- cloud resources
- software as a service (SaaS) services
- suppliers
- facilities
- backup sets
- privileged tools
- repositories

## Evidence to retain

Retain the approved record, source evidence, approval history, exceptions, and follow-up actions under the organization's retention and protection rules.

## Practical example

For one in-scope service, the owner completes the **Asset Inventory** record, links authoritative evidence, obtains review, and tracks rejected or incomplete items to closure.

## ISO requirement, implementation guidance, and best practice

This exact template is not an ISO requirement; it is guidance for recording **Asset Inventory** consistently. Controlled values, named owners, timestamps, approvals, and authoritative evidence improve assurance.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
