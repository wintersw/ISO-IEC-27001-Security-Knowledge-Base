---
title: Statement of Applicability
description: Practical guidance for Statement of Applicability.
---

# Statement of Applicability

The Statement of Applicability (SoA) is the mandatory ISMS document that explains which Annex A controls are applicable, which are not, why, and what the implementation status is for each. It is the bridge between risk treatment decisions and implemented controls.

## Core content

For each Annex A control within the ISMS scope, the SoA should contain at minimum the applicability decision and its justification. In practice, most organisations also record implementation status and evidence references for each applicable control:

- **Control ID:** the Annex A reference (e.g., A.5.15)
- **Applicability:** applicable or not applicable
- **Justification:** the risk treatment decision, legal requirement, contractual obligation, or business need that determines applicability — or the rationale for exclusion. Implementation that is partially complete should be recorded as implementation status, not as a separate applicability category.
- **Implementation status:** implemented, partially implemented, planned, or not implemented
- **Reference to evidence:** which document, record, or system demonstrates that the control operates
- **Related risks:** which risk register entries are treated through this control

## Practical implementation

1. Start from the risk treatment plan and identify which Annex A controls are needed to treat identified risks.
2. For each control, determine applicability — this is a decision, not a default. A control that is not relevant to the organization's context, risk profile, or technology must be explicitly excluded with justification.
3. Assess implementation status honestly: "implemented" means the control is designed, deployed, operating, and evidenced across its intended scope.
4. Link each applicable control to its evidence source — an approved policy, a system configuration, a review record, a test result. Avoid circular references.
5. Assign a control owner responsible for maintaining the SoA entry for their controls.
6. Review and update the SoA after risk reassessments, control changes, scope changes, or audit findings.
7. Approve the SoA through the same authority that approves risk treatment decisions — typically the ISMS owner or management representative.

## Example

An SoA excerpt for a cloud-native startup with no physical facilities:

| Control ID | Applicable | Justification | Status | Evidence |
|---|---|---|---|---|
| A.5.1 Policies for information security | Yes | Risk treatment requires documented policy framework; also a contractual requirement from enterprise customers | Implemented | Information Security Policy v2.3, approved 2025-01-15 |
| A.7.1 Physical security perimeters | No | Organization operates fully remote with no owned or leased facilities; all services are cloud-hosted | — | Scope statement confirms no physical sites |
| A.8.8 Management of technical vulnerabilities | Yes | Risk assessment identified vulnerability exploitation as a top-five risk | Implemented | Vulnerability management procedure; Qualys scan reports; Jira remediation tickets |
| A.8.25 Secure development life cycle | Yes | Required for customer-facing products and in-scope internal tooling | Partially implemented | SDLC policy; SAST in CI/CD for product repos; internal-tools migration tracked in the treatment plan |

## Evidence

- approved SoA document with version control and approval record
- control-by-control applicability decisions with justification
- references to risk register entries, treatment decisions, and evidence sources
- SoA review and update records (at minimum after each risk reassessment)
- records of stakeholder review and approval

## Common mistakes

- Marking all controls as "applicable" without risk-based justification — treating Annex A as a mandatory checklist.
- Leaving implementation status at "planned" indefinitely without target dates or owners.
- Justification fields that say "N/A" or "required by ISO" without explaining the organizational rationale.
- Failing to update the SoA after scope changes, new systems, or control redesigns.
- Evidence references that point to other documents which also point back to the SoA (circular references).


## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
