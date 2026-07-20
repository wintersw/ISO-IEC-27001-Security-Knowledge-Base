---
title: Operational Technology Security
description: Securing OT, ICS, and SCADA environments within an ISO 27001 ISMS.
category: Security Domains
difficulty: Advanced
reviewed_on: 2026-07-20
applies_to:
  - ISO/IEC 27001:2022
tags:
  - security-domain
---

# Operational Technology Security

Operational technology (OT) is hardware and software that monitors or controls physical processes, devices, and infrastructure. It includes industrial control systems (ICS), supervisory control and data acquisition (SCADA) systems, distributed control systems (DCS), and programmable logic controllers (PLCs). OT security protects these systems where a failure can cause physical harm, environmental damage, or safety incidents — not only data loss.

## Why OT is different from IT

- **Consequences drive priorities.** Information technology and OT priorities are context-dependent. In OT, safety, process integrity, availability, and environmental impact often dominate because an outage or manipulated process can injure people or damage equipment; confidentiality can still be critical for recipes, credentials, or sensitive operations.
- **Long lifecycles.** OT devices often run for 10–20 years, may be unpatchable, and use legacy or proprietary protocols (Modbus, DNP3, PROFINET) that lack authentication or encryption.
- **Limited change windows.** Patching may require a plant shutdown, so compensating controls and rigorous change control matter more.
- **Physical consequences.** The relevant threat model includes manipulation of a physical process, not just theft of information.

## Reference model

The Purdue model is a common way to describe OT architecture in levels, from physical process (Level 0) up through control (Levels 1–2), operations (Level 3), and enterprise IT (Levels 4–5). Segmentation between these levels, and a controlled IT/OT boundary (often a demilitarized zone), is the foundation of OT security.

## Core capabilities

- asset inventory for OT devices, firmware, and protocols
- IT/OT network segmentation and conduit control
- secure remote access for vendors and engineers
- passive network monitoring and anomaly detection
- patch and vulnerability management adapted to availability constraints
- backup and recovery of controller configurations and logic
- physical and environmental protection of control equipment

## Evidence

- OT asset register with criticality and safety impact
- network segmentation and DMZ design
- vendor remote-access approvals and session logs
- change records for controller logic
- backup and restoration test results

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** OT is treated as part of the ISMS scope where it is in scope. Relevant Annex A controls include A.5.9 (inventory of assets), A.7.x (physical controls), A.8.9 (configuration management), A.8.20–A.8.22 (network security and segregation), and A.5.7 (threat intelligence).
- **Implementation guidance:** Establish a dedicated OT risk assessment that includes safety impact, segment OT from IT, control the boundary, and adopt guidance such as IEC 62443 for control-system security. Manage patches through risk-based compensating controls where immediate patching is not feasible.
- **Best practice:** Use passive monitoring to build an accurate asset inventory without disrupting fragile devices, and never expose control systems directly to the internet. Involve safety engineers in security decisions.

## Practical example

A water utility places its SCADA network behind a segmented DMZ, replaces direct vendor VPN access with brokered, time-limited sessions, deploys passive monitoring to detect unexpected controller commands, and backs up PLC logic before each maintenance window. Patching follows a risk-based schedule aligned to plant shutdowns, with monitoring as a compensating control in between.

## Common mistakes

- copying an enterprise IT baseline into OT without safety and availability review
- using active discovery or scanning on fragile networks without authorization and testing
- treating the Purdue model as a complete security architecture or assuming every plant fits it
- allowing shared vendor accounts, permanent remote access, or direct internet exposure
- patching or changing controller logic without tested rollback and engineering approval

## Sources

- [NIST SP 800-82 Rev. 3, Guide to Operational Technology Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final)
- [IEC 62443 series overview](https://www.iec.ch/blog/understanding-iec-62443)
- [CISA Cross-Sector Cybersecurity Performance Goals](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals)

## Related chapters

- [Network Security](network-security.md)
- [Asset Management](asset-management.md)
- [Business Continuity](business-continuity.md)

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
