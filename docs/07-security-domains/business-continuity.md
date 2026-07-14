---
title: Business Continuity and ICT Readiness
description: Practical domain guidance for ISO 27001 security teams.
---

# Business Continuity and ICT Readiness

Business continuity ensures the organization can continue critical activities during disruption. ICT readiness ensures technology services can support continuity needs.

## Key concepts

- BIA
- RTO
- RPO
- DRP
- backup
- restore testing
- resilience

## Best practices

- Define ownership and scope.
- Integrate with risk management.
- Document minimum requirements.
- Automate evidence collection where practical.
- Review exceptions and control performance.
- Link operational practices to Annex A and the SoA.

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

A customer portal has an RTO of four hours and an RPO of fifteen minutes. The recovery design includes redundant infrastructure, protected backups, identity dependencies, DNS, monitoring, supplier escalation, and customer communication. A restore test proves data recovery, while a tabletop tests decision-making and communication.

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

- [Service Continuity and ISMS](../32-it-governance-and-itsm/service-continuity-and-isms.md)
- [Backup and Restore Test Record Template](../10-templates/backup-restore-test-record-template.md)
