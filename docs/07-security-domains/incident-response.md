---
title: Incident Response
description: Practical domain guidance for ISO 27001 security teams.
category: Security Domains
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - security-domain
---

# Incident Response

Incident response is the organized process for identifying, assessing, containing, eradicating, recovering from, and learning from information security incidents.

## Key concepts

- prepare
- detect
- assess
- contain
- eradicate
- recover
- lessons learned


## ISO relevance

This domain supports multiple ISO/IEC 27001 clauses and Annex A controls. Use the domain guidance to implement controls in a practical, operationally sustainable way.

## Evidence

- policy or standard
- process documentation
- configuration evidence
- logs or reports
- review records
- exceptions
- remediation tickets

## Detailed implementation guidance

Incident response prepares the organization to detect, assess, contain, eradicate, recover, communicate, preserve evidence, and improve.

### Example

An unusual bulk export triggers an alert. The team validates the event, disables the account, preserves identity and application logs, identifies affected customers, coordinates legal and privacy assessment, restores safe operation, and updates access and monitoring controls.

### Best practices

- define severity and decision criteria
- maintain contact and escalation lists
- protect logging and time synchronization
- create playbooks for likely scenarios
- include legal, privacy, communications, suppliers, and management
- preserve evidence
- run tabletop exercises
- record lessons learned
- verify corrective action effectiveness

### Common weaknesses

Teams focus on technical containment but fail to preserve decisions, assess data impact, communicate consistently, or update controls after closure.

## Related chapters

- [Incident and Data Breach Management](../28-incident-and-data-breach-management/index.md)
- [Customer Data Breach Case Study](../35-end-to-end-case-studies/customer-data-breach.md)

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Incident response is addressed through Annex A controls A.5.24 (incident management planning and preparation), A.5.25 (assessment and decision on information security events), A.5.26 (response to information security incidents), A.5.27 (learning from information security incidents), and A.5.28 (collection of evidence). ISO/IEC 27035 provides additional guidance on incident management processes.
- **Implementation guidance:** Define incident severity levels, response team roles and responsibilities, escalation paths, communication templates, evidence collection procedures, and post-incident review requirements.
- **Best practice:** Incident response plans that are documented but never exercised provide false assurance. Conduct regular tabletop exercises and use post-incident reviews to drive corrective actions and update the plan.

## Practical example

An EDR alert flags suspicious PowerShell execution on a finance workstation. The SOC analyst triages the alert, confirms lateral movement to a file server, declares a severity-2 incident, isolates the host, and escalates to the incident commander — all within the documented SLA.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
