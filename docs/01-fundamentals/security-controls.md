---
title: Security Controls and Control Effectiveness
description: Preventive, detective, corrective, and other control types.
---

# Security Controls and Control Effectiveness

A control is a measure that modifies risk. Controls may be policies, processes, organizational arrangements, contractual clauses, physical safeguards, or technology.

## Common control functions

- **Preventive:** reduces the chance of an event, such as multifactor authentication (MFA).
- **Detective:** identifies events, such as monitoring and alerting.
- **Corrective:** limits damage or restores service, such as incident containment.
- **Recovery:** restores capability, such as backup recovery.
- **Deterrent:** discourages unwanted behavior.
- **Compensating:** provides an alternative where the preferred control is not feasible.

## Design and operating effectiveness

A well-designed control can still fail in operation. An access-review process is not effective merely because a procedure exists; reviews must occur, cover the right population, produce decisions, and result in timely remediation.

## Evidence

Retain evidence of both design and operation: approved procedure, system configuration, review output, exceptions, remediation tickets, and effectiveness metrics.


## Practical example

A ransomware incident is stopped mid-execution: MFA (preventive) prevents account takeover from credential stuffing, but the attacker uses a legacy service account without MFA. SIEM alerting (detective) catches anomalous encryption writes on a file server within 90 seconds. Automated containment (corrective) isolates the affected host, and backup restoration (recovery) returns file shares in under four hours. The post-incident review maps each control function to the timeline, identifying the legacy service account gap for remediation.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
