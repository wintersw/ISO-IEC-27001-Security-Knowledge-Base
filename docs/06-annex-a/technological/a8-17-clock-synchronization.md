---
title: A.8.17 Clock synchronization
description: Practical implementation, evidence, and audit guidance for A.8.17.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: expanded
---
# A.8.17 Clock synchronization

## Overview

Consistent time lets records from different systems be ordered and correlated. Systems should use approved, trustworthy time sources, monitor synchronization health, protect settings, and account for time zones and known offsets.

## Purpose

A.8.17 ensures that in-scope information-processing systems requiring consistent time use approved, trustworthy sources so security-relevant timestamps can be reliably correlated, ordered, and used as evidence across distributed systems.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Annex A controls are not automatically mandatory. Determine necessary controls through risk treatment, record applicability in the Statement of Applicability, and implement A.8.17 when selected or otherwise committed to.
- **Implementation guidance:** Define **clock synchronization** through its owner, scope, trigger, workflow, exceptions, and evidence.
- **Best practice:** Embed it in normal work, test operation and effectiveness, and review it after material change or failure.

## Practical implementation

Configure applicable servers, endpoints, network devices, security tools, and application platforms to synchronize clocks from approved, trustworthy time sources. Use a resilient time-service design appropriate to the environment, monitor clock drift, and alert when a system exceeds its defined maximum offset. Protect time-service configuration from unauthorized modification through access controls and change management. Document approved time sources, synchronization topology, acceptable drift thresholds, and procedures for correcting desynchronized systems. For geographically distributed environments, retain time-zone context and record security-relevant timestamps in a consistent format, preferably coordinated universal time (UTC).

### Measures that support decisions

- systems synchronized to approved sources
- maximum drift across the estate
- time-source availability
- unauthorized clock changes detected

## Common mistakes

- Relying on a single time source without redundancy or monitoring.
- Failing to document acceptable drift thresholds and alert on exceeded limits.
- Allowing unrestricted configuration changes to time-service settings.
- Recording timestamps without time zone offsets, making cross-system correlation unreliable.

## Auditor questions

- What time sources are approved, and how is their trustworthiness verified?
- How is clock drift monitored, and what is the current maximum drift across the estate?
- Are time-service configurations protected from unauthorized modification?
- Are security-relevant timestamps recorded in a consistent, comparable format?

## Checklist

- [ ] Applicable in-scope systems configured to synchronize from approved time sources
- [ ] Redundant time sources documented and monitored for availability
- [ ] Clock drift monitored with defined maximum offset and alerting
- [ ] Time-service configuration protected by access controls and change management
- [ ] Security timestamps recorded in consistent format with time zone indication

## Practical example

Servers and security tools synchronize to approved redundant time sources. Monitoring detects excessive drift, changes require privilege and logging, and incident records retain coordinated universal time with local display conversion.

## Evidence to retain

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

## Related controls, clauses, templates, and checklists

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
- [Control Assurance Review Checklist](../../11-checklists/control-assurance-review.md)
- [Abbreviations](../../15-reference/abbreviations.md)
