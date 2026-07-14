---
title: ISMS Exception Management
description: Explains how to manage control exceptions without weakening the ISMS.
category: ISMS
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - isms
  - best-practice
---

# ISMS Exception Management

An exception is a formally approved, time-limited deviation from a policy, standard, or control requirement. It does not remove the underlying risk or obligation.

## Purpose

Exceptions allow justified deviations to be governed without silently weakening the information security management system (ISMS). The process makes residual risk, compensating controls, ownership, approval, expiry, and remediation visible.

## Key concepts

- **Exception:** permission to deviate from a defined requirement.
- **Compensating control:** an alternative safeguard that reduces some or all of the added risk.
- **Risk acceptance:** an authorized decision to retain residual risk within defined conditions.
- **Expiry:** the date on which the exception must close, renew, or be escalated.

## Minimum exception fields

| Field | Purpose |
|---|---|
| Exception ID | Stable reference |
| Requirement | Policy/control being excepted |
| Business justification | Why exception is needed |
| Risk assessment | Security impact |
| Compensating controls | Risk reduction |
| Owner | Accountable person |
| Approver | Authorized risk decision-maker |
| Expiry date | Prevents permanent exceptions |
| Review date | Ensures reassessment |

## Best practices

- Require risk owner approval.
- Set expiry dates.
- Track compensating controls.
- Review aging exceptions.
- Report high-risk exceptions to management.

## Practical implementation

1. Identify the exact requirement and affected scope.
2. Record the business reason, duration, and consequences of refusing the exception.
3. Assess added risk and define compensating controls.
4. Obtain approval from an authority permitted to accept the residual risk.
5. Monitor conditions and compensating controls until remediation or expiry.
6. Close, renew, or escalate the exception through a recorded decision.

## Practical example

A legacy server cannot meet the current authentication standard until replacement in four months. The service owner documents the affected accounts and risk, restricts network access, increases logging and review, obtains risk-owner approval, and links the exception to the funded replacement. The exception expires automatically if it is not renewed through a new assessment.

## Evidence to retain

- exception register
- requirement and affected-scope record
- risk assessment and residual-risk decision
- approvals
- compensating control evidence
- review records
- closure records

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** ISO/IEC 27001 does not prescribe a centralized exception register, but deviations affecting selected controls, risk treatment, or documented commitments must remain consistent with authorized risk decisions and the Statement of Applicability (SoA).
- **Implementation guidance:** Use a controlled workflow that connects each deviation to its requirement, scope, owner, risk, safeguards, approval, and expiry.
- **Best practice:** Prohibit permanent exceptions; repeated renewal should trigger root-cause analysis, remediation planning, or management escalation.

## Common mistakes

- treating an informal waiver or ticket comment as risk acceptance;
- approving an exception without an exact scope or expiry;
- naming compensating controls without checking that they operate;
- allowing the control owner to approve risk beyond delegated authority; and
- repeatedly renewing exceptions without addressing their cause.

## Related controls, clauses, templates, and checklists

- [Risk treatment](../05-risk-management/risk-treatment.md)
- [Statement of Applicability](../05-risk-management/statement-of-applicability.md)
- [Exception Register Template](../10-templates/exception-register-template.md)
- [Exception Waiver Record Template](../10-templates/exception-waiver-record-template.md)
- [Monthly ISMS Operations Checklist](../11-checklists/isms-monthly-operations.md)
- [A.5.36 Compliance with policies, rules, and standards](../06-annex-a/organizational/a5-36-compliance-with-policies-rules-and-standards.md)
