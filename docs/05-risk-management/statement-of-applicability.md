---
title: Statement of Applicability
description: Practical guidance for Statement of Applicability.
category: Risk Management
difficulty: Intermediate
applies_to:
  - ISO/IEC 27001:2022
tags:
  - risk-management
---

# Statement of Applicability

The Statement of Applicability (SoA) is required documented information that records the controls the organization has determined are necessary, why they are included, whether they are implemented, and why any Annex A reference controls are excluded. Necessary controls can come from Annex A, the organization's own designs, other frameworks, or legal, regulatory, and contractual requirements. The SoA is the bridge between risk treatment decisions and implemented controls.

## Core content

First record every necessary control, including controls not found in Annex A. Then compare that set with Annex A to verify that no necessary reference control was overlooked and record the rationale for any excluded Annex A control. A useful SoA contains:

- **Control ID and source:** an Annex A reference or an organization-defined identifier, with its source recorded
- **Necessary / included:** why the control is needed, such as risk treatment, law, regulation, contract, or business requirement
- **Annex A exclusion rationale:** why an Annex A reference control is not necessary, where applicable
- **Implementation status:** whether the necessary control is implemented; local workflow states such as planned or partially implemented may add useful detail
- **Reference to evidence:** which document, record, or system demonstrates that the control operates
- **Related risks:** which risk register entries are treated through this control

## Practical implementation

1. Start from risk treatment and other binding requirements and determine all necessary controls, whether or not they appear in Annex A.
2. Compare the necessary-control set with every Annex A reference control. Add any necessary control that the comparison reveals; justify Annex A exclusions.
3. Assess implementation status honestly: "implemented" means the control is designed, deployed, operating, and evidenced across its intended scope.
4. Link each necessary control to its evidence source — an approved policy, a system configuration, a review record, or a test result. Avoid circular references.
5. Assign a control owner responsible for maintaining the SoA entry for their controls.
6. Review and update the SoA after risk reassessments, control changes, scope changes, or audit findings.
7. Approve the SoA through the same authority that approves risk treatment decisions — typically the ISMS owner or management representative.

## Example

An SoA excerpt for a cloud-native startup with no physical facilities:

| Control ID | Source | Necessary? | Inclusion or exclusion rationale | Implemented? | Evidence |
|---|---|---|---|---|---|
| A.5.1 Policies for information security | Annex A | Yes | Risk treatment and customer contracts require a governed policy framework | Yes | Information Security Policy v2.3 and approval record |
| A.7.1 Physical security perimeters | Annex A | No | The scope has no organization-controlled facilities; supplier physical security is addressed through SUP-01 | — | Scope statement and supplier assessment |
| A.8.8 Management of technical vulnerabilities | Annex A | Yes | Vulnerability exploitation is a material assessed risk | Yes | Procedure, scoped scan results, and remediation tickets |
| SUP-01 Cloud-provider facility assurance | Organization-defined | Yes | Treats physical and concentration risks inherited from the hosting provider | Yes | Contract, assurance report review, and exception record |

## Evidence

- approved SoA document with version control and approval record
- the complete necessary-control set, including organization-defined controls
- comparison with Annex A and justified exclusions
- references to risk register entries, treatment decisions, and evidence sources
- SoA review and update records (at minimum after each risk reassessment)
- records of stakeholder review and approval

## Common mistakes

- Treating Annex A as the complete universe of possible controls and omitting organization-defined controls.
- Marking all Annex A controls as necessary without a reasoned inclusion rationale.
- Leaving implementation status at "planned" indefinitely without target dates or owners.
- Justification fields that say "N/A" or "required by ISO" without explaining the organizational rationale.
- Failing to update the SoA after scope changes, new systems, or control redesigns.
- Evidence references that point to other documents which also point back to the SoA (circular references).


## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
