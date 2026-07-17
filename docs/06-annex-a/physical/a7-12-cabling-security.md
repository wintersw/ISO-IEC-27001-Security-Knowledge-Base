---
title: A.7.12 Cabling security
description: Practical implementation, evidence, and audit guidance for A.7.12.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.7.12 Cabling security

## Overview

Power and data cabling can be damaged, intercepted, disconnected, or confused during work. Routing, separation, labeling, access, inspection, and change control should protect service and information needs.

## Purpose

Cabling security protects power and data cables from interception, interference, damage, and accidental disconnection through appropriate routing, separation, labeling, access controls, and regular inspection.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.7.12 when selected or otherwise committed to.
- **Implementation guidance:** Define **cabling security** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

Network cabling to a restricted area runs through controlled conduits, is separated from interference sources, labeled without revealing sensitive destinations, and is inspected after building work.

## Evidence to retain

- site risk assessment
- access records
- visitor records
- inspection or maintenance records
- incident and corrective-action records

## Common mistakes

- Running sensitive network cables through publicly accessible areas without conduit or physical protection
- Placing data cables alongside power cables without adequate separation, causing interference
- Labeling cables with information that reveals the sensitivity or destination of the connected systems
- Not inspecting cabling after building work, office moves, or contractor activity in ceiling or floor spaces

## Auditor questions

- How are cables carrying sensitive or critical data physically protected from interception and damage?
- Are power and data cables adequately separated to prevent interference?
- What information is shown on cable labels, and could it reveal system or network sensitivity?
- When was cabling last inspected after building or maintenance work?

## Checklist

- [ ] Cable routing documented and protected from unauthorized access and environmental damage
- [ ] Power and data cables separated to prevent electromagnetic interference
- [ ] Cable labeling scheme defined that does not reveal sensitive system information
- [ ] Inspection triggered after building work, office moves, or contractor activity
- [ ] Change control covers cabling additions, modifications, and removals

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
