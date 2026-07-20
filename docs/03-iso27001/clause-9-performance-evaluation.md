---
title: Clause 9 — Performance Evaluation
description: Detailed practical guidance for Clause 9 — Performance Evaluation.
category: ISO/IEC 27001
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - iso27001
---

# Clause 9 — Performance Evaluation

Clause 9 checks whether the information security management system (ISMS) is working through monitoring, measurement, internal audit, and management review. It answers: how do we know the ISMS is effective?

## Why this matters

Without performance evaluation, the organization cannot distinguish an ISMS that operates from one that merely exists. Internal audit provides independent assurance. Management review ensures leadership sees and acts on ISMS performance. Together they form the feedback loop that drives improvement and maintains certification.

## Key concepts

- **Monitoring, measurement, analysis and evaluation (9.1):** The organization must determine what to monitor and measure, the methods, when to perform it, and when to analyze and evaluate results. This includes the effectiveness of controls and the ISMS itself.
- **Internal audit (9.2):** Planned, independent audits against the organization's own ISMS requirements and ISO/IEC 27001. Audits must be objective, impartial, and conducted by competent auditors (who do not audit their own work).
- **Management review (9.3):** Top management must review the ISMS at planned intervals. The review must consider inputs including audit results, risk status, nonconformities, improvement opportunities, and changes in context. Outputs must include decisions on improvement and resource needs.

## Practical implementation

1. **Define what to measure** — start with the information needs of decision-makers. A metric that answers no question wastes effort. Focus on control effectiveness (is it working?), coverage (is it deployed everywhere it should be?), and operational performance (are SLAs met?).
2. **Document the measurement method** — data source, calculation, frequency, owner, target or threshold, and escalation path. Prefer system-generated data over manual collection.
3. **Plan the internal audit programme** annually. Define scope, criteria, auditors, schedule, and reporting. Ensure auditors are competent and independent of the areas they audit.
4. **Conduct audits** using a consistent methodology: opening meeting, evidence collection through interviews and records, documented findings, closing meeting, and audit report.
5. **Classify findings** as conformity, nonconformity, or opportunity for improvement. Record objective evidence for each finding.
6. **Prepare the management review** with a structured input pack: audit results, risk register status, incident trends, control effectiveness, objectives progress, nonconformities, improvement actions, and changes in context.
7. **Hold management review** as a decision-making forum, not a presentation. Record decisions, actions, owners, and target dates.

## Security-team best practices

- Design metrics that answer specific questions: "Are our critical vulnerabilities being remediated within SLA?" rather than "How many vulnerabilities did we find?"
- Use an audit programme that covers all clauses and controls over the certification cycle, not just the areas that are easy to audit.
- Train internal auditors on the ISMS scope, audit techniques, and nonconformity writing — competence is a requirement.
- Prepare the management review input pack at least a week before the meeting so reviewers can engage, not just listen.
- Close the loop: every management review output should be traceable to an implemented action.

## Evidence

- measurement plan with defined metrics, methods, owners, frequency, and targets
- monitoring records, dashboard exports, and trend reports
- internal audit programme and schedule
- audit reports with scope, criteria, findings, objective evidence, and auditor independence declaration
- nonconformity records with root cause, correction, corrective action, and effectiveness verification
- management review input pack, minutes, attendance records, decisions, and action tracker

## Common mistakes

- Measuring everything that is easy to count while ignoring what matters (vanity metrics).
- Internal auditors auditing their own work — the most common auditor independence failure.
- Audit findings that describe symptoms without identifying the requirement that was not met.
- Management review that is a status presentation with no decisions, actions, or resource commitment.
- Audit nonconformities are recorded but corrective actions are never verified for effectiveness.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Clause 9 requires the organization to monitor, measure, analyze, and evaluate the ISMS (9.1), conduct internal audits at planned intervals (9.2), and hold management reviews (9.3). These are mandatory for certification.
- **Implementation guidance:** Internal audit can use a combination of full-system audits and focused audits. A small organization may use an external auditor or a trained internal resource from a different function.
- **Best practice:** Align the audit programme, measurement plan, and management review calendar so they feed each other — audit results inform measurements, both inform management review, and management review decisions update the audit programme.

## Practical example

An e-commerce company defines its measurement plan around three information needs: "Are critical vulnerabilities being fixed?" (mean time to remediate, overdue count), "Are access reviews effective?" (completion rate, findings per review, remediation time), and "Is security awareness improving?" (phishing simulation click rate trend, reported incidents). The internal audit programme schedules one full-system audit per year and two focused audits (supplier management, access control). The management review is held in February after Q4 data is available. The CEO chairs, the CISO presents the input pack, and decisions are recorded: approve two additional headcount for security operations, accept one residual risk with six-month review, and prioritize the SSO migration project for Q2.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
