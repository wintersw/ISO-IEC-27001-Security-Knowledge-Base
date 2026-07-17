---
title: A.8.21 Security of network services
description: Practical implementation, evidence, and audit guidance for A.8.21.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.21 Security of network services

## Overview

Network services need defined security features, service levels, responsibilities, monitoring, and assurance whether provided internally or by suppliers. Requirements should reflect the information and business services carried.

## Purpose

This control ensures that security features, service levels, and management requirements for network services — whether internal or supplier-provided — are identified, agreed, implemented, and monitored. Without defined service security requirements, the organization inherits whatever the provider delivers by default.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.21 when selected or otherwise committed to.
- **Implementation guidance:** Define **security of network services** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

A managed connectivity agreement defines encryption, administrative access, availability, logging, incident notification, change notice, evidence, and exit assistance. The owner reviews reports and unresolved service failures quarterly.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- Network services are procured without security requirements specified in the contract or SLA.
- Supplier-provided network services are assumed secure — no independent verification or audit of controls is performed.
- Service changes (routing updates, new features, capacity upgrades) are implemented without security review.
- Responsibility boundaries are unclear — the organization assumes the provider handles security while the provider assumes the opposite.

## Auditor questions

- Where are the security requirements for each network service documented?
- How are supplier-provided network services monitored for compliance with security requirements?
- How are changes to network services reviewed for security impact before implementation?
- Show evidence of recent service reviews and any identified security gaps.

## Checklist

- [ ] security requirements defined for each network service
- [ ] requirements included in contracts and SLAs for supplier services
- [ ] service monitoring and compliance verification in place
- [ ] security review required for service changes
- [ ] responsibility boundaries documented and agreed
- [ ] service review records retained

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
