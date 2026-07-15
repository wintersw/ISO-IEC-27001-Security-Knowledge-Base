---
title: Business Continuity and ICT Readiness
description: Practical domain guidance for ISO 27001 security teams.
---

# Business Continuity and information and communication technology (ICT) Readiness

Business continuity ensures the organization can continue critical activities during disruption. ICT readiness ensures technology services can support continuity needs.

## Key concepts

- business impact analysis (BIA)
- RTO
- RPO
- disaster recovery plan (DRP)
- backup
- restore testing
- resilience


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

Business continuity ensures that the organization can continue or recover critical activities during disruption. Information security contributes by protecting availability, integrity, recoverability, and trustworthy communication.

Continuity planning should begin with business impact rather than technology. Critical services, recovery time objectives, recovery point objectives, dependencies, minimum resources, supplier commitments, and manual workarounds should be defined before selecting technical recovery solutions.

### Example

A customer portal has an RTO of four hours and an RPO of fifteen minutes. The recovery design includes redundant infrastructure, protected backups, identity dependencies, Domain Name System (DNS), monitoring, supplier escalation, and customer communication. A restore test proves data recovery, while a tabletop tests decision-making and communication.

### Best practices

- link services to business processes
- include cyber scenarios such as ransomware
- test restores rather than backup completion
- identify identity, supplier, network, and people dependencies
- define crisis roles and decision authority
- record exercise findings
- verify supplier recovery claims
- update plans after major change

### Common weaknesses

Plans may name systems but not business priorities, assume suppliers will be available, ignore identity dependencies, use untested backups, or treat tabletop discussion as proof of technical recovery.

## Related chapters

- [Service Continuity and information security management system (ISMS)](../32-it-governance-and-itsm/service-continuity-and-isms.md)
- [Backup and Restore Test Record Template](../10-templates/backup-restore-test-record-template.md)

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Business continuity and ICT readiness are addressed through Annex A controls A.5.29 (information security during disruption) and A.5.30 (ICT readiness for business continuity). Clause 8 operational planning and control also requires that processes needed to meet ISMS requirements are planned, implemented, and controlled — which includes continuity arrangements.
- **Implementation guidance:** Identify critical business processes and their supporting ICT services, define recovery time and recovery point objectives, document continuity plans, test them at planned intervals, and update them based on test results and changes.
- **Best practice:** Integrate information security continuity with the organisation's overall business continuity management. A continuity plan that restores IT systems but ignores information security controls is not adequate under A.5.29.

## Practical example

A ransomware scenario is selected for the annual business continuity exercise. The team validates the critical application recovery procedure, measures the achieved RTO against the documented target, identifies a missing dependency on a restored authentication service, and updates the plan.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
