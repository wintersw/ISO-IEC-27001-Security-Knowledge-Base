---
title: A.8.15 Logging
description: Practical implementation, evidence, and audit guidance for A.8.15.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
  - control
---

# A.8.15 Logging

## Overview

Logging records relevant events in systems, applications, networks, identities, and security tools. Logs support detection, investigation, accountability, forensic analysis, compliance, and operational troubleshooting.

## Purpose

This control reduces information security risk by establishing clear expectations, repeatable operation, accountability, and evidence for the relevant security activity.

## Practical implementation

1. Define the control objective.
2. Assign a control owner and operator.
3. Document the minimum process needed for repeatability.
4. Integrate the control into normal workflows.
5. Define evidence before the control goes live.
6. Monitor operation and exceptions.
7. Review effectiveness and improve.

## Small organization example

A small organization may implement this control through a lightweight policy, a shared register or ticket workflow, clear ownership, and periodic review.

## Enterprise example

An enterprise should integrate this control with GRC tooling, workflow automation, IAM, SIEM, CMDB, vulnerability management, or other enterprise systems as applicable.

## Evidence

- approved policy or procedure
- owner assignment
- operational records
- system exports or logs
- review records
- exception approvals
- remediation tickets
- metrics and reports

## Metrics and KPIs

- completion rate
- overdue action count
- exception count and age
- control coverage
- remediation time
- review timeliness

## Common mistakes

- Control exists only on paper.
- Ownership is unclear.
- Evidence is not retained.
- Exceptions are not reviewed.
- Implementation status in the SoA does not match reality.

## Auditor questions

- Who owns this control?
- How is it implemented?
- How do you know it operates?
- Show recent evidence.
- How are exceptions handled?
- How is effectiveness reviewed?

## Checklist

- [ ] logging requirements defined
- [ ] critical sources identified
- [ ] central collection implemented
- [ ] retention defined
- [ ] log access restricted
- [ ] log-source health monitored

## Practical implementation guidance

This control creates visibility into security-relevant activity. Logs and alerts should be designed around investigation and risk scenarios, protected from tampering, retained appropriately, and reviewed through defined workflows.

For A.8.15, begin by identifying the specific risk, legal requirement, contractual commitment, or operational need that makes the control necessary. The control owner should then define what is in scope, which roles perform the activity, which systems or data sources are authoritative, how exceptions are handled, and what evidence proves that the control operated.

A useful control description answers five questions:

1. **What outcome is expected?** State the security result rather than only the activity.
2. **Who is accountable?** Name the control owner and the operational roles.
3. **How is the control performed?** Connect it to a normal workflow, service, system, or process.
4. **How is failure detected?** Define monitoring, exception handling, and escalation.
5. **How is effectiveness verified?** Use sampling, testing, metrics, audit, or observation.

## Worked example

The data warehouse logs authentication but not queries or exports. The organization enables data-access audit logging, creates alerts for unusual export volume, protects logs, and tests triage procedures.

The example should be tailored to the organization's scope, size, technology, risk appetite, and regulatory context. A small organization may operate the control manually with clear ownership and evidence. A larger organization may use automated workflows, policy enforcement, continuous monitoring, and independent control testing. The underlying objective remains the same.

## Implementation steps

1. Link the control to related risk scenarios and obligations.
2. Assign an accountable owner and supporting roles.
3. Document a proportionate policy, standard, or procedure.
4. Integrate the control into existing business or ITSM workflows.
5. Define evidence source, frequency, retention, and storage.
6. Define exceptions, approval levels, and expiry.
7. Train people who operate or depend on the control.
8. Test the design before relying on it.
9. Monitor operation and investigate failures.
10. Review the control after major change, incident, audit finding, or risk update.

## Typical evidence

- approved policy, standard, or procedure
- owner and responsibility record
- operating records from the relevant workflow
- exception and risk-acceptance records
- control test or audit evidence

Evidence should demonstrate both design and operation. A policy proves the requirement was defined; it does not prove that the control operated. Prefer authoritative system records, complete populations, approvals, timestamps, remediation records, and repeatable reports.

## Suggested metrics

- critical systems with required logging
- alerts triaged within target
- log-source failures
- use cases tested

Metrics should support decisions. A high completion rate can still be misleading if the population is incomplete, exceptions are hidden, or remediation is not verified.

## Audit questions

- What risk or requirement does this control address?
- Who owns the control and who performs it?
- How is the complete in-scope population determined?
- What happens when the control fails or is bypassed?
- Which evidence demonstrates recent operation?
- How are exceptions approved and reviewed?
- How does management know whether the control is effective?
- What changed after the last incident, audit finding, or review?

## Common weaknesses

- the control exists only in policy language
- ownership is unclear or assigned to a generic team
- scope or population is incomplete
- evidence is manually assembled shortly before audit
- exceptions have no expiry or risk approval
- control completion is measured without testing outcome
- changes in systems, suppliers, data, or organization are not reflected
- corrective actions close tickets without verifying effectiveness

## Related guidance

- [Security Lifecycle Management](../../31-security-lifecycle-management/index.md)
- [Control Lifecycle Overview](../../31-security-lifecycle-management/control-lifecycle-overview.md)
- [Evidence and Assurance Lifecycle](../../31-security-lifecycle-management/evidence-assurance-lifecycle.md)
- [Continual Improvement](../../23-continual-improvement/index.md)
- [Related Document Map](../../15-reference/related-document-map.md)
