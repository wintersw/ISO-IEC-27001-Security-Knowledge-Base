---
title: Risk Register
description: Practical guidance for Risk Register.
category: Risk Management
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - risk-management
---

# Risk Register

A risk register is a controlled record of identified risks and their treatment status. It is the operational tool that makes risk visible, assigned, and tracked — not a compliance artifact to be filed and forgotten.

## Core content

Each risk entry should contain:

- **Risk ID:** a unique, stable identifier for traceability
- **Risk scenario:** a structured description — what could happen, to which asset or process, caused by what threat, with what consequence
- **Asset or process affected:** the information, system, service, or business process at risk
- **Risk owner:** the person or role with authority to manage the risk and approve treatment
- **Existing controls:** what is already in place that reduces likelihood or impact
- **Inherent impact and likelihood:** assessment before considering additional treatment
- **Risk level:** the combined score or rating from impact and likelihood
- **Treatment decision:** modify, retain, avoid, or share — with specific actions, owners, and target dates
- **Residual risk:** reassessed impact, likelihood, and level after treatment
- **Status:** identified, under treatment, treated (pending verification), accepted, or closed
- **Review date:** next scheduled review or event-based trigger

## Practical implementation

1. Use a consistent template or tool with mandatory fields and validation — a spreadsheet is sufficient for a small ISMS if version-controlled and protected from unauthorized changes.
2. Assign a unique risk ID and never reuse it, even after a risk is closed.
3. Write risk scenarios that an uninformed reader can understand: "An attacker exploits an unpatched vulnerability in the customer-facing web application to exfiltrate personal data" rather than "Web app hack."
4. Assign risk owners who have the authority to accept risk and approve resources for treatment — not just the security team.
5. Record treatment decisions and link to the risk treatment plan and SoA.
6. Reassess residual risk after treatment and obtain risk owner acceptance.
7. Review the register at planned intervals (at least annually) and after triggers (incidents, changes, audits).

## Example

A risk register entry for a SaaS company:

| Field | Entry |
|---|---|
| Risk ID | RISK-2025-014 |
| Scenario | A database administrator with legitimate access intentionally or accidentally deletes production customer data, causing data loss, service disruption, and potential regulatory notification |
| Asset | Production PostgreSQL database (customer data) |
| Risk owner | VP Engineering |
| Existing controls | Role-based access, quarterly access reviews, audit logging |
| Inherent impact | High (4) — regulatory penalty, reputational damage, customer churn |
| Inherent likelihood | Low (2) — limited number of DBAs, access reviews in place |
| Risk level | 8 (Medium) |
| Treatment | Modify: implement just-in-time access for production DB, require peer approval for destructive commands, enable point-in-time recovery with 1-hour RPO, conduct quarterly backup restore tests |
| Residual risk | Impact: Medium (3), Likelihood: Very Low (1), Level: 3 (Low) |
| Status | Under treatment — JIT access and peer approval implemented; backup testing in progress |
| Review date | Next scheduled review (e.g., start of next quarter or per defined review cycle) |

## Evidence

- risk register in a controlled, versioned format with access restrictions
- risk owner assignment and acknowledgement records
- treatment action tracking with status and completion evidence
- residual risk acceptance approvals
- review history showing changes, updates, and closure decisions

## Common mistakes

- Risks described so vaguely they cannot be assessed or treated ("security breach" or "data loss").
- All risks assigned to the CISO or security team regardless of the affected asset or process.
- Inherent risk scored using an inconsistent baseline — the organization must define whether inherent risk is assessed before any controls, before additional treatment only, or at another defined point, and apply that definition consistently across all risk entries.
- The register is updated only before audits — it does not reflect current operational reality.
- Closed risks are deleted rather than retained with closure rationale and date.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** The risk register is not a standalone ISO requirement. It is the primary instrument for meeting the risk assessment and risk treatment requirements of ISO/IEC 27001 clause 6.1.2 and clause 6.1.3, and for demonstrating the link between identified risks, risk treatment decisions, and the Statement of Applicability.
- **Implementation guidance:** Define mandatory fields (risk ID, description, asset/process, threat, vulnerability, inherent score, treatment option, residual score, owner, target date, status), ensure the register is maintained as controlled documented information, and link each risk entry to the relevant control in the SoA.
- **Best practice:** Keep closed risks in the register with closure rationale and date rather than deleting them — the audit trail demonstrates the risk management lifecycle.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
