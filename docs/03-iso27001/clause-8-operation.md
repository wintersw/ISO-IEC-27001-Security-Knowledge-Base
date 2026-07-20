---
title: Clause 8 — Operation
description: Detailed practical guidance for Clause 8 — Operation.
category: ISO/IEC 27001
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - iso27001
---

# Clause 8 — Operation

Clause 8 turns plans into controlled operational work. It requires the organization to plan, implement, and control the processes needed to meet ISMS requirements — including risk assessment, risk treatment, and management of outsourced processes.

## Why this matters

Planning without execution is a paper ISMS. Clause 8 is where documented intentions are tested against operational reality. It ensures that risk assessments are actually performed, treatment plans are executed, and processes that are delegated to suppliers or partners remain under control. Auditors test operation by sampling records, not by reading policies.

## Key concepts

- **Operational planning and control (8.1):** The organization must plan, implement, and control the processes needed to meet requirements and implement the actions determined in Clause 6. This includes establishing criteria for processes and controlling them in accordance with those criteria.
- **Information security risk assessment (8.2):** Risk assessments must be performed at planned intervals or when significant changes occur, using the methodology defined under Clause 6. Results must be retained as documented information.
- **Information security risk treatment (8.3):** The risk treatment plan produced in Clause 6 must be implemented. Residual risk must be reviewed against acceptance criteria.
- **Outsourced processes (8.1):** When the organization outsources any process that affects ISMS conformity, it must ensure those processes are controlled. The type and extent of control must be defined within the ISMS.

## Practical implementation

1. **Translate the risk treatment plan into operational tasks** with owners, deadlines, and acceptance criteria. Integrate with existing workflows — project management, change management, procurement — rather than creating a parallel ISMS-only process.
2. **Schedule and perform risk assessments** at defined intervals (typically annually) and after triggers (major acquisition, new product line, significant incident, regulatory change). Use the documented methodology consistently.
3. **Implement controls** identified through risk treatment. Assign control owners, define operating procedures, collect evidence, and test effectiveness.
4. **Manage outsourced processes** by identifying each outsourced process that affects the ISMS, defining control requirements in contracts or SLAs, assessing supplier capability, monitoring performance, and retaining evidence of control.
5. **Control changes to planned arrangements** — when operational reality deviates from the plan, assess the impact on ISMS outcomes and document the approved deviation or replanning.
6. **Retain documented information** that demonstrates processes were carried out as planned — this is the operating evidence auditors will sample.

### Outsourced processes — practical controls

When a process that affects information security is outsourced (e.g., cloud hosting, SOC monitoring, payroll processing, secure destruction):

- Determine the type and extent of control based on the risk the outsourced process presents.
- Define security requirements in the contract, SLA, or statement of work — not in a separate document the supplier never sees.
- Assess the supplier's capability before contracting and periodically thereafter.
- Monitor performance through reports, audits, certifications, or test results.
- Retain evidence that the outsourced process operates under control. A supplier's ISO 27001 certificate is supporting evidence, not proof of your own control.

## Security-team best practices

- Operate risk assessments as facilitated workshops, not spreadsheet exercises — engage asset owners, not just the security team.
- Track treatment actions to closure; an overdue treatment action is a control failure in waiting.
- Define minimum control requirements for outsourced processes before procurement selects a supplier.
- When an outsourced process fails, the accountability remains with your organization, not the supplier.
- Use operational metrics (assessment completion rate, treatment action age, supplier review status) to drive management review.

## Evidence

- risk assessment records with scope, date, methodology version, participants, results, and approvals
- risk treatment plan implementation records showing completed actions, dates, and verification
- operational control evidence for each implemented control (logs, reports, approvals, test results)
- outsourced process register with control requirements, supplier assessments, and monitoring records
- documented information showing processes were carried out as planned (not just planned)
- change records where planned arrangements were modified

## Common mistakes

- Risk assessments are performed but treatment actions are never tracked to completion.
- Outsourced processes are assumed to be secure because the supplier "has ISO 27001."
- Operational controls are documented in policy but no one follows them — and no one checks.
- Risk assessments are copied forward each year with minor edits instead of fresh analysis.
- Exceptions and workarounds accumulate without review, making the documented process fictional.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Clause 8 requires the organization to plan and control operations (8.1), perform risk assessments at planned intervals (8.2), and implement the risk treatment plan (8.3). Outsourced processes must be controlled and the type and extent of control defined.
- **Implementation guidance:** Operational control can use existing business processes (change management, project delivery, procurement). Add security control steps rather than creating duplicate ISMS-only workflows.
- **Best practice:** Automate evidence collection where possible — system logs, workflow records, and automated reports are more reliable and less burdensome than manual evidence assembly.

## Practical example

A SaaS company's risk treatment plan identifies the need for a web application firewall (WAF) as a control for A.8.20 (Networks security) and A.8.21 (Security of network services). The security engineer creates an implementation task in the engineering backlog with acceptance criteria: WAF deployed in blocking mode, logging to SIEM, alert on critical events, and rules reviewed quarterly. The task flows through the normal change and deployment pipeline. Evidence includes the change ticket, deployment record, configuration export, SIEM integration test, and the first quarterly rule review. The outsourced cloud hosting provider's shared responsibility model is documented, and the provider's SOC 2 report is retained alongside the organization's own monitoring of WAF effectiveness.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
