---
title: Clause 10 — Improvement
description: Detailed practical guidance for Clause 10 — Improvement.
---

# Clause 10 — Improvement

Clause 10 ensures the information security management system (ISMS) responds to nonconformities and improves over time. It distinguishes between fixing a problem (correction), fixing the cause (corrective action), and making the ISMS better regardless of whether anything failed (continual improvement).

## Why this matters

An ISMS that does not improve decays. Threats evolve, technology changes, and business priorities shift. Clause 10 ensures the organization has a mechanism to detect nonconformities, correct them, analyze root causes, and prevent recurrence. More importantly, it requires the organization to proactively seek improvement — not just react to failures.

## Key concepts

- **Nonconformity (10.2):** A failure to fulfil a requirement. This can be identified through audits, monitoring, incidents, complaints, or management review. The requirement and the evidence of failure must both be identifiable.
- **Correction:** Action to eliminate a detected nonconformity — fixing the immediate problem. Example: re-enabling a disabled firewall rule.
- **Corrective action:** Action to eliminate the cause of a nonconformity and prevent recurrence. Example: adding a peer review step to firewall change management after finding that a single administrator disabled a rule without approval.
- **Continual improvement (10.1):** Proactive enhancement of the ISMS's suitability, adequacy, and effectiveness. This is not triggered by a nonconformity — it is driven by metrics, trends, objectives, and management review decisions.

## Practical implementation

1. **Establish a nonconformity management process** with defined roles, a register or tracking system, and escalation rules. Ensure all sources of nonconformities are captured: audits, incidents, monitoring, complaints, management review.
2. **When a nonconformity is identified**, react promptly: contain the issue, correct it, and assess whether the nonconformity could occur elsewhere.
3. **Perform root cause analysis** using a structured technique (5 Whys, fishbone diagram, fault tree). Avoid stopping at the most obvious or convenient cause.
4. **Determine and implement corrective action** that addresses the root cause. Set an owner, target date, and verification method.
5. **Review the effectiveness** of corrective action after implementation. Did the nonconformity recur? Did the corrective action introduce new risks?
6. **Maintain an improvement backlog** sourced from audits, metrics, incidents, management review, and staff suggestions. Prioritize by risk impact and feasibility.
7. **Implement improvements** through planned changes to the ISMS. Verify that the improvement achieved its intended result without negative side effects.

### Correction vs corrective action vs continual improvement

| What happened | Action | Example |
|---|---|---|
| A nonconformity is detected | **Correction** — fix the immediate problem | Restore the missing access review record |
| The root cause is investigated | **Corrective action** — fix the cause | Redesign the access review workflow to prevent skipped applications |
| Nothing went wrong, but performance could be better | **Continual improvement** — enhance the ISMS | Automate access review data collection to reduce manual effort and errors |

## Security-team best practices

- Do not confuse the volume of corrective actions with ISMS failure — a system that finds and fixes problems is healthier than one that hides them.
- Verify corrective action effectiveness after a defined period, not immediately after implementation.
- When a nonconformity could occur in another team, system, or process, extend the corrective action scope.
- Use the improvement backlog as an input to management review — unfunded improvements should be visible to leadership.
- Celebrate improvements that prevent incidents, not just those that respond to them.

## Evidence

- nonconformity register with source, requirement reference, description, date identified, and owner
- root cause analysis records showing the method used, evidence considered, and conclusion
- corrective action plans with actions, owners, target dates, and completion evidence
- effectiveness review records confirming the nonconformity has not recurred
- improvement backlog with prioritization criteria and status
- implemented improvement records with before/after evidence

## Common mistakes

- Correcting the symptom without investigating the root cause — the same nonconformity recurs in the next audit.
- Writing corrective actions as vague commitments ("improve process") without specific changes, owners, or dates.
- Closing corrective actions before verifying effectiveness.
- Treating improvement as only reactive — waiting for audit findings rather than proactively analyzing metrics and trends.
- Confusing activity ("we held a training session") with improvement ("incidents caused by human error decreased by 40%").

## Related continual improvement lifecycle guidance

For the full operational lifecycle, use:

- [ISMS Continual Improvement Lifecycle](../23-continual-improvement/isms-continual-improvement-lifecycle.md)
- [Corrective Action vs Continual Improvement](../23-continual-improvement/corrective-action-vs-continual-improvement.md)
- [Effectiveness Review](../23-continual-improvement/effectiveness-review.md)
- [Continual Improvement Register Template](../10-templates/continual-improvement-register-template.md)

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Clause 10 requires the organization to continually improve the suitability, adequacy, and effectiveness of the ISMS (10.1), and to react to nonconformities and take corrective action to prevent recurrence (10.2).
- **Implementation guidance:** The nonconformity and corrective action process can use existing incident, problem, or quality management tools. Avoid creating a separate ISMS-only process unless necessary.
- **Best practice:** Link corrective actions to the risk register — a recurring nonconformity in a high-risk area should trigger a risk reassessment. Use trend analysis across nonconformities to identify systemic weaknesses.

## Practical example

An internal audit finds that three of twelve sampled leaver accounts were not disabled within the required 24-hour window. The immediate correction: disable the three accounts and confirm no unauthorized activity occurred. Root cause analysis (5 Whys) reveals that the HR-to-IT leaver notification is a manual email, and the IT administrator was on leave with no backup. Corrective action: implement an automated HRIS-to-IdP integration for leaver events, define a backup administrator, and add a weekly reconciliation report. Effectiveness is verified after 90 days: the next audit sample shows 100% of leavers were disabled within SLA. This improvement is recorded in the improvement backlog and reported in the next management review.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
