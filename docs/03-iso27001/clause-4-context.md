---
title: Clause 4 — Context of the Organization
description: Detailed practical guidance for Clause 4 — Context of the Organization.
---

# Clause 4 — Context of the Organization

Clause 4 is where the information security management system (ISMS) begins. It requires the organization to understand itself, its environment, relevant interested parties, and the boundaries of the ISMS.

## Why this matters

Clause 4 is not just a paperwork exercise. It establishes the factual foundation of the ISMS: what the organization does, who cares about security, what they expect, and where the ISMS boundary runs. If context is wrong, risk assessment targets the wrong things, scope is indefensible, and audit findings are inevitable.

## Key concepts

- internal and external issues
- interested parties
- requirements
- ISMS scope
- climate-related relevance where applicable

## Practical implementation

1. Record internal issues such as organizational structure, strategy, capabilities, resources, culture, technology, and planned changes.
2. Record external issues such as laws, contracts, customer expectations, market conditions, suppliers, threats, technology trends, and climate-related relevance.
3. Identify interested parties and translate their relevant requirements into owned obligations.
4. Define scope across organizational units, processes, information, technology, physical locations, and supplier-operated services.
5. Describe every exclusion and the interfaces or dependencies that cross the boundary; an exclusion must not make the ISMS scope misleading.
6. Assign owners, approval authority, review frequency, and event-driven review triggers.
7. Link the context and scope records to risk assessment, objectives, the Statement of Applicability, audit planning, and management review.

## Context and boundary working table

> Adapted from the scope and context structure in the [ISO 27001:2022 Toolkit](https://github.com/PehanIn/ISO-27001-2022-Toolkit), copyright (c) 2024 Pehan Gunasekara, MIT License. See the repository's third-party notices.

| Area | Decision prompts | Evidence or output |
|---|---|---|
| Business and organization | Which products, services, processes, departments, and accountable roles affect intended ISMS outcomes? | context register, organization map, process catalog |
| Locations | Which offices, facilities, remote-work arrangements, and hosting regions are included? | location list, physical and cloud boundary map |
| Technology and information | Which applications, infrastructure, platforms, repositories, and information sets support scoped services? | asset inventory, architecture and data-flow diagrams |
| External environment | Which legal, regulatory, contractual, market, threat, supplier, and climate-related issues are relevant? | obligations register, threat assessment, supplier register |
| Exclusions | Why is each excluded area outside the boundary, and what interfaces or shared dependencies remain? | approved exclusion rationale, interface controls |
| Maintenance | Which scheduled and event-driven reviews keep the context and scope current? | review calendar, change records, approvals |

## Scope quality tests

- A reader can tell which services, teams, locations, information, technologies, and supplier dependencies are included.
- Every exclusion has a defensible rationale and an owner for boundary interfaces.
- The asset inventory, risk register, continuity plans, audit universe, and certification description use the same boundary.
- Acquisitions, restructures, new products, material suppliers, major architecture changes, and changed obligations trigger review.
- Top management approves the scope and unresolved boundary risks are visible.

## Best practices

- Document context and scope as structured records with owners, approval, and review dates — not as free-text paragraphs that drift from the risk assessment and SoA.
- When the organisation changes (acquisition, new product, new regulation, major incident), review the context analysis before refreshing the risk assessment.
- Record the climate-change determination even when the conclusion is that climate change is not relevant — the auditor needs to see that the consideration took place.
- Exclusions must have a defensible rationale. An interface or shared dependency that crosses the boundary must still be controlled — excluding it from scope does not make the risk disappear.
- Keep the boundary diagram, asset inventory, risk register, audit universe, and certification description consistent. A mismatch between any two of these is a common audit finding.

## Evidence

- context analysis
- interested-party register
- scope statement
- boundary diagram
- dependency map

## Common mistakes

- Treating the clause as an audit-only requirement.
- Failing to assign owners.
- Retaining weak or incomplete evidence.
- Letting documentation drift from reality.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** ISO/IEC 27001 clause 4 is mandatory. The organisation must determine external and internal issues relevant to its purpose and the ISMS (4.1), identify interested parties and their requirements (4.2), define the ISMS scope (4.3), and establish, implement, maintain, and continually improve the ISMS (4.4). These determinations must be documented and available as auditable information.
- **Implementation guidance:** Document context in a structured way — external issues (regulatory, market, geopolitical), internal issues (culture, technology, resources), interested parties (regulators, customers, suppliers, staff), and scope boundaries (physical, logical, organisational). Review context at planned intervals and after significant change.
- **Best practice:** Treat context as a living analysis, not a one-time exercise. Changes in the organisation — new products, markets, regulations, or incidents — should trigger a context review.

## Practical example

A fintech startup preparing for ISO/IEC 27001 certification documents its context:

- **Internal issues:** 45 employees, fully remote across three countries, AWS-only infrastructure, two products (B2B payments API and consumer dashboard). Planned acquisition of a smaller compliance-tool vendor in the next 12 months.
- **External issues:** PSD2 and GDPR regulatory obligations; enterprise customers require ISO/IEC 27001 certification in contracts; competitors have recently suffered supply-chain attacks targeting fintech APIs.
- **Interested parties:** customers (security and uptime expectations), banking partners (regulatory compliance and audit rights), employees (remote-work tools and device security), regulators (data protection and financial services authorities).
- **Scope decision:** The payments API, consumer dashboard, supporting AWS infrastructure, engineering and support functions. Excluded: the planned acquisition (to be incorporated post-acquisition via scope change); personal devices used only for email (controlled through MDM policy).

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
