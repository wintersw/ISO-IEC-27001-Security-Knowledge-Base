---
title: Clause 6 — Planning
description: Detailed practical guidance for Clause 6 — Planning.
---

# Clause 6 — Planning

Clause 6 connects organizational context, risks, selected controls, security objectives, treatment plans, and the Statement of Applicability. It is where the ISMS shifts from describing the organization to defining what the organization will do about information security.

## Why this matters

Planning is where strategic intent meets operational execution. Without a defined methodology, risk assessments produce inconsistent results that cannot be compared or aggregated. Without clear objectives, teams cannot demonstrate progress. Without a properly maintained Statement of Applicability, the link between risk treatment and control implementation is invisible to auditors.

## Key concepts

- **Risk assessment methodology (6.1.2):** A defined, repeatable process with criteria for impact, likelihood, and risk acceptance. The methodology must produce consistent, comparable results across the ISMS scope.
- **Risk treatment (6.1.3):** For each assessed risk, a decision to modify, retain, avoid, or share the risk. Treatment produces the Statement of Applicability and may generate a risk treatment plan.
- **Statement of Applicability (6.1.3 d):** The mandatory document listing each Annex A control, whether it is applicable, the justification, and implementation status.
- **Information security objectives (6.2):** Measurable goals aligned with the policy, communicated within the organization, and updated as needed.
- **Planning of changes (6.3):** When the ISMS itself must change — scope, methodology, governance, major processes — the change must be planned, resourced, and verified.

## Practical implementation

1. **Define and document the risk assessment methodology** before performing assessments. Include impact and likelihood scales, risk acceptance criteria, review triggers, and owner responsibilities.
2. **Perform risk assessment** across the ISMS scope. Identify assets, threats, vulnerabilities, existing controls, and assign impact and likelihood using the defined methodology.
3. **Decide risk treatment** for each risk above acceptance criteria. Record the chosen option, residual risk level, risk owner, and approval.
4. **Produce the Statement of Applicability** as a controlled document linking each Annex A control to applicable risks, requirements, and implementation evidence.
5. **Set measurable security objectives** — for example, "reduce unresolved critical vulnerabilities older than 30 days to zero" or "complete quarterly access reviews with 100% remediation of findings within 14 days." Assign owners and target dates.
6. **Plan ISMS changes** as governed activities, not ad-hoc edits. Evaluate the impact on scope, risks, controls, resources, and evidence before implementing.

### Plan changes to the management system

Clause 6 planning includes changes to the information security management system (ISMS), not only technical change control. When scope, risk methods, governance, major processes, control architecture, suppliers, or assurance arrangements change, record:

- the purpose and expected outcome;
- affected requirements, risks, controls, documents, evidence, and interfaces;
- likely unintended consequences and continuity needs;
- required people, competence, time, and funding;
- accountable owner, approvals, sequence, dependencies, and rollback or correction path; and
- how successful implementation and ongoing effectiveness will be verified.

A proportional record may be a change ticket for a small adjustment or a governed programme for a merger or scope redesign.

## Security-team best practices

- Test the risk methodology on a small, well-understood scope before scaling to the entire ISMS.
- Use a consistent risk register format with mandatory fields enforced by workflow, not trust.
- Review the SoA at least quarterly or after any material change to scope, risks, or controls.
- Align security objectives with business priorities so progress is visible and valued.
- Treat the SoA as a living control document, not an audit artifact produced once per cycle.

## Evidence

- documented risk assessment methodology with version control
- risk register with identified risks, owners, impact, likelihood, treatment decisions, and residual risk
- risk treatment plan with owners, actions, target dates, and completion status
- approved Statement of Applicability with control-by-control applicability, justification, and implementation status
- residual risk acceptance records signed by authorized risk owners
- measurable security objectives with assigned owners and progress tracking
- ISMS change assessments, approvals, implementation records, and effectiveness reviews

## Common mistakes

- Performing risk assessment before defining the methodology, leading to inconsistent results.
- Treating the SoA as a one-time deliverable that is never updated after certification.
- Setting security objectives that are vague ("improve security") or unmeasurable.
- Accepting residual risk without documenting the rationale, conditions, and review trigger.
- Failing to plan ISMS changes — allowing scope creep, methodology drift, or undocumented control changes.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Clause 6 requires a defined risk assessment process (6.1.2), risk treatment leading to the SoA (6.1.3), measurable security objectives (6.2), and planned ISMS changes (6.3). These are mandatory ISMS requirements.
- **Implementation guidance:** The methodology can be simple for small organizations — what matters is consistency and comparability of results. The SoA format is not prescribed; choose a structure that supports maintenance and audit.
- **Best practice:** Integrate risk assessment with change management and project initiation so risks are identified early, not retrofitted. Use the SoA as a control inventory that drives testing, metrics, and improvement.

## Practical example

A fintech company defines its risk methodology during ISMS setup: a 5×5 impact/likelihood matrix with defined criteria for financial, regulatory, reputational, and operational impact. The CISO owner approves acceptance criteria (risks rated 12 and above require treatment). The first assessment identifies 34 risks; 22 require treatment. The risk treatment plan assigns owners and target dates. The SoA is produced with 87 applicable controls, 6 not applicable with justification (e.g., A.7.1 physical perimeters — cloud-only SaaS with no owned facilities). Security objectives include "100% of high-risk findings remediated within SLA" and "management review completed within 30 days of quarter-end." When the company acquires a payments subsidiary, a formal ISMS change plan is approved before scope expansion.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
