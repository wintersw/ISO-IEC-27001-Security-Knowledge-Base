---
title: A.5.37 Documented operating procedures
description: Starter page for A.5.37 Documented operating procedures; expand using the Annex A control page template.
category: Annex A
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - annex-a
status: stub
---

# A.5.37 Documented operating procedures

!!! note "Expansion status"
    This starter page exists so the documentation project has a stable file path for every Annex A control. Expand it using the [control page template](../control-page-template.md).

## Overview

This control should be documented using the standard control structure.

## Implementation notes

When expanding this page, explain the concept in plain English, then describe practical implementation patterns and audit evidence. Avoid copying official standard text.

## Starter checklist

- [ ] Control owner assigned
- [ ] Applicability decision recorded in the SoA
- [ ] Related risks identified
- [ ] Implementation approach documented
- [ ] Evidence sources identified
- [ ] Review frequency defined

## Practical implementation guidance

This control supports a defined information security outcome. Implementation should be risk-based, assigned to an owner, integrated into normal work, evidenced, monitored, and improved when conditions change.

For A.5.37, begin by identifying the specific risk, legal requirement, contractual commitment, or operational need that makes the control necessary. The control owner should then define what is in scope, which roles perform the activity, which systems or data sources are authoritative, how exceptions are handled, and what evidence proves that the control operated.

A useful control description answers five questions:

1. **What outcome is expected?** State the security result rather than only the activity.
2. **Who is accountable?** Name the control owner and the operational roles.
3. **How is the control performed?** Connect it to a normal workflow, service, system, or process.
4. **How is failure detected?** Define monitoring, exception handling, and escalation.
5. **How is effectiveness verified?** Use sampling, testing, metrics, audit, or observation.

## Worked example

The organization identifies a process in which the control is needed, assigns an owner, integrates the requirement into the normal workflow, records evidence, and reviews performance after an incident, change, or audit.

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

- control operation completed on time
- exceptions open
- control failures
- corrective actions verified effective

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
