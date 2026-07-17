---
title: A.8.20 Networks security
description: Practical implementation, evidence, and audit guidance for A.8.20.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.20 Networks security

## Overview

Network security protects data flows and connected services through architecture, configuration, access control, monitoring, maintenance, and response. Controls should reflect trust boundaries and service needs rather than relying on a single perimeter.

## Purpose

This control ensures that networks and network devices are designed, configured, managed, and monitored to protect information in transit and the services that depend on them. Network security is not a single perimeter but a layered set of controls spanning architecture, access, encryption, monitoring, and maintenance.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.20 when selected or otherwise committed to.
- **Implementation guidance:** Define **networks security** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical example

A cloud network exposes only the application gateway publicly, separates management and data paths, restricts flows to documented dependencies, logs denied connections, and tests that direct database access is blocked.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Common mistakes

- Security relies entirely on a perimeter firewall — internal traffic is unencrypted and unmonitored.
- Network device management interfaces are accessible from user networks or the internet.
- Default SNMP community strings, vendor passwords, and unused services remain enabled on network devices.
- Network diagrams are outdated or do not exist — the security team does not know what is connected.

## Auditor questions

- How are network security controls documented, and where are the current network diagrams?
- How are network devices hardened, and how is configuration drift detected?
- How is internal network traffic monitored for anomalous or malicious activity?
- Show evidence that administrative access to network devices is restricted, authenticated, and logged.

## Checklist

- [ ] network architecture and security zones documented
- [ ] network devices hardened against vendor defaults
- [ ] administrative access restricted and logged
- [ ] encryption applied to sensitive traffic in transit
- [ ] network monitoring and anomaly detection in place
- [ ] network diagrams maintained and reviewed regularly

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
