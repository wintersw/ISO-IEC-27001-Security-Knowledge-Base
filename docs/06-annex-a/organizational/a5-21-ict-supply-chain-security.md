---
title: A.5.21 ICT supply chain security
description: Practical implementation, evidence, and audit guidance for A.5.21.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.5.21 ICT supply chain security

## Overview

Information and communication technology supply chains include providers, components, software dependencies, support channels, and sub-suppliers. Security must consider hidden dependencies and changes that can affect trustworthy delivery.

## Purpose

This control ensures that information and communication technology (ICT) supply chain risks involving hardware, software, services, components, and sub-suppliers are identified, assessed, and managed. Dependencies can introduce vulnerabilities or disruption outside the direct supplier relationship, so assurance should follow the relevant supply chain rather than stop at the first tier.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.5.21 when selected or otherwise committed to.
- **Implementation guidance:** Define **ict supply chain security** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

A product team inventories critical third-party libraries and build services, verifies update sources, monitors disclosed vulnerabilities, restricts release credentials, and defines a response when a compromised dependency is detected.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- Supply chain risk assessment stops at the direct supplier — sub-suppliers, open-source dependencies, and embedded components are invisible.
- Software bills of materials (SBOMs) are not maintained — when a vulnerability is disclosed, no one knows which systems are affected.
- Supplier security is evaluated once at procurement and never revisited — even though supplier ownership, infrastructure, and practices change.
- ICT supply chain risks are treated as a procurement issue — security, legal, and operational teams are not involved in assessment.

## Auditor questions

- How are ICT supply chain risks identified, and who is responsible for assessment?
- How far down the supply chain does the organization look — direct suppliers only, or sub-suppliers and components?
- How are supply chain vulnerabilities (e.g., Log4j, SolarWinds-style attacks) detected and responded to?
- Show evidence that critical ICT suppliers and components have been identified and assessed.

## Checklist

- [ ] ICT supply chain risk assessment process defined
- [ ] critical suppliers and components identified
- [ ] sub-supplier and dependency mapping performed
- [ ] SBOM or equivalent maintained for critical systems
- [ ] supply chain vulnerability monitoring in place
- [ ] response plan for supply chain compromise defined

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
