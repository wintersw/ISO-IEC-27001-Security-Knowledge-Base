---
title: ISMS Scope
description: Practical ISMS guidance for ISMS Scope.
---

# ISMS Scope

The scope defines the boundaries of the information security management system (ISMS) — which organizational units, locations, processes, technologies, services, information, and external dependencies are covered, and which are excluded.

## Why this matters

Scope determines everything downstream: which assets are in the risk assessment, which controls apply, what auditors examine, and what the certificate describes. A scope that is too narrow misses material risks. A scope that is too broad may be unmanageable. An unclear scope creates confusion and audit findings.

## Key requirements

- **Understandable to internal and external parties:** customers, auditors, and staff should recognize what is covered from the scope statement.
- **Covers dependencies needed to deliver in-scope services:** if a supplier, cloud service, or internal team is essential to a scoped service, it must be within the scope boundary or controlled as an external dependency.
- **Identifies interfaces with excluded areas:** what crosses the boundary, and how is it controlled?
- **Avoids misleading exclusions:** you cannot exclude the data center but include the services it hosts without explaining the dependency.
- **Matches real operational responsibility:** scope should reflect what the organization actually controls, not aspirational boundaries.

## Practical implementation

1. **Describe the organization** — products, services, mission, size, sector, and regulatory environment. This establishes why the scope looks the way it does.
2. **Define organizational scope** — which departments, teams, legal entities, and geographic locations are included.
3. **Define service and process scope** — which services and supporting processes are covered. Be specific: "customer data analytics platform and its supporting development, hosting, and support processes" rather than "IT services."
4. **Define technology and information scope** — which applications, infrastructure, platforms, networks, and information assets are in scope.
5. **Identify physical locations** — offices, data centers, co-location facilities, and remote working arrangements.
6. **Identify supplier dependencies** — which cloud providers, SaaS platforms, managed services, and outsourced processes are essential to scoped services.
7. **Document exclusions** — what is outside the boundary and why. Each exclusion should have a rationale and identify any cross-boundary interfaces or dependencies.
8. **Map the boundary** — a diagram is more effective than paragraphs for showing what is inside, outside, and at the interface.
9. **Review and approve** — scope should be approved by top management and reviewed after organizational changes.

## Scope quality tests

- Can a new employee read the scope and understand what the ISMS covers?
- Does the asset inventory, risk register, SoA, and audit plan use the same boundary?
- Are all material dependencies either inside the scope or externally controlled?
- Would excluding any element make the scope statement misleading?
- Has the scope been reviewed in the last 12 months and after any major change?

## Evidence examples

- approved scope statement or ISMS scope document
- boundary diagram showing in-scope and out-of-scope elements
- dependency map for externally provided services
- exclusion rationales with cross-boundary interface controls
- scope review and approval records

## Common mistakes

- Writing scope at the level of "all information security" or "the entire organization" without specifying what that means.
- Excluding cloud infrastructure because it is "the provider's responsibility" — the shared responsibility model requires your controls to be in scope.
- Remote workers excluded from scope while accessing scoped systems and data.
- Scope approved once during setup and never revisited after acquisitions, new products, or infrastructure changes.
- The certificate description, audit plan, risk assessment, and SoA use different boundaries.

## ISO requirement, implementation guidance, and best practice

- **ISO requirement:** Clause 4.3 requires the organization to determine the boundaries and applicability of the ISMS. The scope must be available as documented information and consider external and internal issues, interested parties, and their requirements.
- **Implementation guidance:** The internal ISMS scope is controlled documented information. The certificate normally contains a public certification-scope description derived from it, but that public description is not necessarily identical to the complete internal scope statement. Write the internal scope for precision and completeness; ensure the certificate description is understandable to customers and auditors.
- **Best practice:** Maintain the internal scope document with detailed technical boundaries, derive the external certification-scope description from it, and ensure both are consistent. Review after every significant organizational change.

## Practical example

A 150-person SaaS company defines its ISMS scope as: "The design, development, hosting, and support of the Acme Analytics platform, including the AWS production environment (us-east-1), the corporate IT environment (Google Workspace, GitHub, Jira), and the engineering and customer support functions based in Berlin and remote within Germany. Excluded: the separate Acme Consulting professional services division (operates under its own management system); physical office facilities (all staff remote, no customer data on-premises)." The boundary diagram shows the platform, supporting tools, people functions, and the interface controls with AWS (shared responsibility), the consulting division (separate network, no shared systems), and customers (API and support portal).

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
