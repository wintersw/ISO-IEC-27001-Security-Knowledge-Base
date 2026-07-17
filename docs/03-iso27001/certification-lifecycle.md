---
title: Certification Lifecycle
description: Stage 1, Stage 2, surveillance, and recertification explained.
---

# Certification Lifecycle

ISO/IEC 27001 certification follows a three-year cycle managed by an accredited certification body. Understanding each phase — and the audit days, evidence requirements, and nonconformity types involved — helps organizations plan realistically and avoid surprises.

## The three-year cycle at a glance

| Phase | When | Duration (illustrative — varies by certification body, scope, and complexity) | Scope |
|---|---|---|---|
| Readiness (optional gap assessment) | Before formal application | Varies; typically a few days | Voluntary review to identify gaps before the real audit |
| Stage 1 audit | After application and contract | Varies; may be on-site or remote | Documentation review, scope confirmation, readiness for Stage 2 |
| Stage 2 audit | Scheduled after Stage 1 conclusions and readiness concerns are addressed | Determined by the certification body under its ISO/IEC 27006-1 audit-time method and audit programme | Full implementation and effectiveness audit |
| Surveillance year 1 | ~12 months after certification decision | Typically shorter than Stage 2; set by audit programme | Selected ISMS areas, mandatory clauses, internal audit and management review |
| Surveillance year 2 | ~24 months after certification decision | Typically shorter than Stage 2; set by audit programme | Selected ISMS areas plus any previous nonconformity follow-up |
| Recertification | Before certificate expiry (~33–36 months) | Determined by the certification body, reflecting scope and surveillance history | Full scope reassessment before certificate expires |

Audit-time calculation for accredited ISMS certification is performed by the certification body using ISO/IEC 27006-1 and its documented audit-time method. Relevant factors include the effective number of personnel, scope, sites, complexity, technology, outsourcing, and information-security risk. The exact duration and allocation between audit stages are certification-body decisions, not values prescribed by this guide.

## Readiness assessment (pre-certification)

Before engaging a certification body, the ISMS should have operated long enough to produce evidence — typically at least a full cycle of internal audit, management review, risk assessment, and control operation. A readiness assessment, whether performed internally or by an external consultant, checks:

- Is the scope clearly defined and documented?
- Has the risk assessment and treatment process produced a plausible risk register and SoA?
- Has internal audit been completed with documented findings and corrective actions?
- Has a management review been conducted with minutes and decisions?
- Are mandatory documented-information items in place (policy, scope, risk methodology, SoA, objectives)?
- Are Annex A controls either implemented or subject to a treatment plan with defined owners?

Common readiness pitfall: the ISMS exists on paper but has not operated. Certification bodies expect operating evidence, not freshly written documents dated the week before Stage 1.

## Stage 1 audit

The certification body evaluates whether the documented ISMS design meets ISO/IEC 27001 requirements and whether the organization is ready for implementation audit.

### What auditors review in Stage 1

- Scope statement — boundaries, exclusions, sites, functions
- Information security policy and supporting policies
- Risk assessment methodology and risk treatment process
- Statement of Applicability (SoA)
- Internal audit programme and most recent audit results
- Management review records
- Key documented information (mandatory documents and records)
- Legal, regulatory, and contractual obligation register
- Site tour (if on-site) to confirm physical scope

### Stage 1 outcomes

Stage 1 conclusions are determined by the certification body. Typical outcomes may include:

- **Proceed to Stage 2:** Readiness is confirmed; minor documentation items may be identified for attention before or during Stage 2.
- **Stage 2 postponed:** Significant gaps exist (e.g., risk assessment not completed, no internal audit performed). Stage 2 is rescheduled after gaps are closed and re-verified.
- The certification body documents Stage 1 conclusions, including concerns that could become nonconformities during Stage 2. Terminology and classification practices can differ, so the organization's audit plan and certification-body procedure are authoritative for how Stage 1 results are reported.

## Stage 2 audit

Stage 2 is the implementation audit. Auditors evaluate not what the ISMS says it does, but what it actually does — through interviews, observation, sampling of records, and walkthroughs of processes and controls.

### What auditors evaluate in Stage 2

- **Effectiveness of the ISMS:** Do processes produce the intended outcomes? Are objectives being met?
- **Control implementation:** Are controls from the SoA operating as designed? Can control owners explain and demonstrate their controls?
- **Risk treatment:** Has risk treatment been implemented? Are residual risks within acceptable levels?
- **Internal audit competence and independence:** Were auditors qualified and impartial?
- **Management review effectiveness:** Did the review use relevant inputs (audit results, incidents, metrics, changes) and produce meaningful decisions?
- **Continual improvement:** Is there evidence the ISMS is being improved, not just maintained?
- **Legal and regulatory compliance:** Are obligations identified, tracked, and met?

### Audit techniques

Auditors use sampling, interviews, document review, and observation. They may trace a single control from policy → procedure → operating record → review evidence. Expect questions like "show me the last time this was done" rather than "show me the procedure."

### Stage 2 outcomes

- **Recommend certification:** No major nonconformities; minor nonconformities accepted with a correction plan. The certification body makes a certification decision (typically by an independent reviewer, not the audit team itself).
- **Conditional recommendation:** One or more major nonconformities. Certification is not recommended until root cause is addressed, correction is verified, and corrective action is confirmed effective (usually via follow-up audit).
- **Not recommended:** The ISMS does not meet requirements; significant rework needed before reapplication.

## Nonconformity types

Understanding the distinction between audit findings determines how quickly certification can proceed:

| Finding type | Definition | Impact on certification | Example |
|---|---|---|---|
| Major nonconformity | A nonconformity that affects the management system's capability to achieve its intended results; classification depends on significance, scope, system impact, and the certification body's rules | Prevents a positive initial or recertification decision until adequately addressed and verified; an existing certificate may be subject to suspension under certification-body rules | A required risk-assessment process is absent across an in-scope business unit, leaving material risks unidentified and untreated. |
| Minor nonconformity | A nonconformity that does not, on the available evidence, affect the management system's overall capability to achieve its intended results | Requires correction and corrective action within the certification body's time limits; related or repeated minor findings may indicate a systemic issue | One scheduled access review was late, while the process otherwise operated and the affected access was subsequently reviewed. |
| Observation / Opportunity for Improvement (OFI) | Not a nonconformity; a suggestion for improvement | No impact on certification. Optional. | "Consider automating the evidence collection process to reduce manual effort." |

### Correction vs corrective action in audit context

Auditors expect to see both:
- **Correction:** Fix the immediate finding (e.g., complete the missing access review).
- **Corrective action:** Address the root cause so the finding does not recur (e.g., add a calendar-triggered reminder and escalation path so reviews are not forgotten).

## Surveillance audits

Surveillance audits maintain the certification between the initial and recertification cycles. They are lighter in scope than Stage 2 but must confirm continued conformity.

### Surveillance scope (mandatory each visit)

- Internal audit and management review
- Review of previous nonconformities
- Effectiveness of corrective actions
- Handling of complaints (if any)
- Changes to the ISMS or scope
- Use of certification marks

### Additional areas sampled per visit

The certification body's audit programme rotates coverage across ISMS elements so that all requirements are assessed at least once during the three-year cycle. A typical rotation:

- **Surveillance 1:** Clause 4–6, selected Annex A controls (e.g., A.5 organizational controls), operational processes
- **Surveillance 2:** Clause 7–8, remaining Annex A controls (e.g., A.8 technological controls), incident management, business continuity

## Recertification

Recertification occurs before the three-year certificate expires. It is a broader reassessment than surveillance. Its audit time is calculated by the certification body using the applicable ISMS certification rules, the current scope and complexity, and knowledge gained during the certification cycle. It must confirm:

- Continued suitability, adequacy, and effectiveness of the ISMS
- Ongoing commitment to maintain effectiveness and improvement
- Continued relevance to the organization's context and strategic direction
- Resolution of outstanding nonconformities from previous audits

Recertification is not a reset — ongoing surveillance findings, changes to scope, incidents, and performance trends all inform the recertification audit.

### Certificate validity and transition

- The certificate is valid for three years from the certification decision date, subject to satisfactory surveillance.
- Recertification audit timing must allow the certification decision before expiry.
- If recertification is not completed before expiry, the organization may need to restart from Stage 1 (depending on how long the gap is and certification body policy).

## Practical example: a SaaS company's certification timeline

A 120-employee SaaS company pursues ISO/IEC 27001 certification with a scope covering its platform operations, engineering, and corporate IT:

| Month | Milestone |
|---|---|
| 0 | Engage certification body; contract signed |
| 1–3 | ISMS design: scope, risk assessment, SoA, policy framework, control implementation begins |
| 4–5 | ISMS operates; evidence accumulates; first internal audit conducted |
| 6 | Management review; readiness assessment finds four minor gaps (closed within 2 weeks) |
| 7 | Stage 1 audit (2 days remote; illustrative example — actual duration determined by certification body): 3 documentation concerns raised; all addressed before Stage 2 |
| 8 | Stage 2 audit (5 days on-site; illustrative example — actual duration determined by certification body): 2 minor nonconformities found (one overdue supplier review, one incomplete asset register entry); correction plan accepted |
| 9 | Certification decision issued |
| 12 | Surveillance 1 (2 days): previous minors closed; 1 new minor (delayed patch for a low-risk internal system) |
| 24 | Surveillance 2 (2 days): no nonconformities; 2 OFIs noted |
| 33 | Recertification audit (4 days): 1 minor nonconformity; certificate renewed |

## Evidence to retain per phase

### Readiness
- Gap assessment report
- Internal audit report and corrective action records
- Management review minutes and decisions

### Stage 1
- Scope statement (approved)
- Risk assessment methodology
- Risk register and risk treatment plan
- Statement of Applicability
- Document register

### Stage 2
- Operating records for all controls in SoA
- Internal audit records (auditor competence, plan, reports, follow-up)
- Management review inputs and outputs
- Incident records and corrective actions
- Metrics and KPIs with trend data

### Surveillance and recertification
- Ongoing internal audit records
- Management review records for each surveillance period
- Corrective action closure evidence
- ISMS change records (scope changes, new risks, organizational changes)
- Updated SoA and risk register

## Common mistakes

- Starting the certification process before the ISMS has operated — insufficient operating evidence is likely to result in Stage 2 being postponed, because auditors need to verify that the ISMS functions in practice.
- Treating Stage 1 as a formality — if documentation is incomplete, Stage 2 will expose operational gaps.
- Not preparing control owners to explain their controls — auditors interview people, not documents.
- Allowing minor nonconformities to accumulate across surveillance cycles without root-cause correction.
- Forgetting certificate expiry — recertification requires lead time; last-minute scheduling risks a lapse.
- Confusing surveillance scope with full reassessment — only selected areas are audited, but ALL areas must remain conformant.

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
