# ISO/IEC 27001 Security Knowledge Base

A practical, vendor-neutral documentation project for security teams implementing, operating, auditing, and improving an Information Security Management System (ISMS).

## Contents

This repository includes:

- Information security fundamentals
- Governance, risk, and compliance guidance
- Detailed ISO/IEC 27000-family overview
- ISO/IEC 27001:2022 clause guidance
- ISO/IEC 27001:2022/Amd 1:2024 climate-action guidance
- ISMS operating model, policy framework, control lifecycle, maturity model, metrics, and best practices
- Risk-management methods, templates, worked examples, and labs
- Corrected Annex A catalog with all 93 controls
- Linked guidance pages for all 93 Annex A controls, with deeper implementation and assurance material for selected controls
- Security-domain guides spanning identity, cloud, applications, operations, people, physical security, OT, email, cryptography, keys, and secrets
- Secure-by-design guidance for threat modeling and software supply-chain security
- Current framework and EU regulatory landscape mappings with review dates and primary sources
- Templates, checklists, diagrams, examples, glossary, and editorial standards
- Docusaurus local search plus the official sitemap plugin, canonical metadata, and crawler guidance

## Important notice

This project explains standards in original language. It does not reproduce copyrighted ISO/IEC standard text and is not a substitute for purchasing or consulting official ISO/IEC publications.

Selected content is adapted from MIT-licensed third-party material. Copyright, source, license, and adaptation details are retained in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md); locally derived tables and templates also carry a source note.

## Quick start

```bash
npm install
npm start
```

Before publishing changes, run:

```bash
python -m pip install "PyYAML>=6,<7"  # required by the content validator
npm run validate
npm run validate:links
npm run build
```

Production builds generate `build/sitemap.xml` through the official `@docusaurus/plugin-sitemap` package and copy `static/robots.txt`. The content validator checks the package/configuration, metadata, source requirements, local links, and exact file manifest. The external-link check uses network access and reports explicit warnings when an authoritative publisher blocks automated requests.

## Suggested learning paths

- **New security-team member:** Getting Started → Fundamentals → GRC → ISMS → Risk Management
- **ISO implementer:** ISO 27001 Clauses → ISMS → Risk Management → Annex A → Auditing
- **Security engineer:** Security Domains → Annex A → Checklists → Evidence by Design
- **Internal auditor:** Clauses → Risk and SoA → Audit Evidence → Corrective Action


## Project status

The knowledge base includes all 93 Annex A controls, ISO/IEC 27001 clauses 4–10, implementation guides, reusable records, audit checklists, case studies, guided labs, framework relationship pages, and worked risk scenarios. Depth varies by subject: use the [content depth quality standard](docs/15-reference/content-depth-quality-standard.md) when extending a page.

See the Git history for the change history. Edition-sensitive sources and their review dates are maintained in the [external reference register](docs/30-source-research-and-mapping/external-reference-register.md).
