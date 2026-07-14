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
- Detailed pages for several key controls
- Stub pages for all remaining Annex A controls
- Security-domain guides for IAM, cryptography, cloud, application security, incident response, and business continuity
- Templates, checklists, diagrams, examples, glossary, and editorial standards

## Important notice

This project explains standards in original language. It does not reproduce copyrighted ISO/IEC standard text and is not a substitute for purchasing or consulting official ISO/IEC publications.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
mkdocs serve
```

## Suggested learning paths

- **New security-team member:** Getting Started → Fundamentals → GRC → ISMS → Risk Management
- **ISO implementer:** ISO 27001 Clauses → ISMS → Risk Management → Annex A → Auditing
- **Security engineer:** Security Domains → Annex A → Checklists → Evidence by Design
- **Internal auditor:** Clauses → Risk and SoA → Audit Evidence → Corrective Action


## Version 0.4 expansion

This version adds the missing chapters identified by comparing the chat-planned architecture with the generated repository structure:

- deeper fundamentals
- ISO 27k family pages
- ISMS responsibility, evidence, objectives, and exception management
- implementation guides
- expanded security domains
- framework mappings
- more templates and checklists
- FAQ
- project gap analysis page

## Version 0.5 professional toolkit expansion

This version adds an ISMS Professional Toolkit with operational content for ISMS managers, control owners, risk owners, auditors, and security leaders:

- annual ISMS operating calendar
- ISMS health dashboard
- control assurance methodology
- control owner self-assessment
- risk owner review pack
- management review pack
- internal audit program
- evidence management model
- user awareness and security culture surveys
- supplier assurance pack
- incident tabletop scenarios
- metrics library
- policy and procedure starter library
- additional professional templates and checklists

## Version 0.6 BSI ISMS.1 enhancement

This version uses the German ISMS.1 material as a gap source and adds BSI-inspired ISMS management depth:

- ISMS threat landscape
- security concept guide
- security organization model
- ISB role profile
- external ISB contract checklist
- employee integration playbook
- management security reporting
- security process documentation
- economic resource allocation
- elevated protection needs
- BSI-to-ISO mapping
- supporting templates and checklists

## Version 0.7 ethics and framework relationships expansion

This version adds a non-Austria-specific ethics and standards-relationship layer:

- ethical basics of standards
- norms, values, institutions, and controls
- ethical principles of standardization
- ISO, IEC, JTC 1, and SC 27 relationship
- ISO/IEC 27000 family relationship
- ISMS as operating model
- ITIL, ISO/IEC 20000, and ISMS relationship
- COBIT and ISMS relationship
- OECD culture-of-security guidance
- standardization and organizational culture
- perceived participation and security change
- sustainable ISMS for SMEs/startups
- standards selection decision guide
- protection-needs and combined risk-analysis approach
- generic mobile/SaaS risk example
- new templates, surveys, and checklists

## Version 0.8 ISMS documentation template pack

This version adds a tried-and-tested ISMS documentation template pack:

- ISMS documentation roadmap
- guidance for applying templates in the project
- template-to-clause/control map
- document lifecycle guide
- minimum ISO 27001 document set
- governance templates
- risk assessment templates
- Statement of Applicability templates
- audit, corrective action, evidence, and management review templates
- operational record templates
- quality checklists for tailoring, risk assessment, SoA, policies, document control, and management review

## Version 0.9 continual improvement lifecycle expansion

This version adds a dedicated continual improvement lifecycle package and cross-reference layer:

- ISMS continual improvement lifecycle
- PDCA cycle for ISMS
- improvement sources
- improvement backlog
- corrective action vs continual improvement
- improvement prioritization
- effectiveness review
- continual improvement metrics
- management review and improvement
- continual improvement templates and checklists
- related document map to reduce duplication and improve linking between chapters

## Version 1.0 PDF source integration expansion

This version adds content derived from the newly uploaded German and English PDFs:

- PDF source integration overview
- source-based gap analysis
- ISMS building-block model
- governance/risk/compliance operating model
- enhanced ISMS implementation roadmap
- ISMS process architecture
- ISMS operating process catalog
- certification and scope assurance guide
- regulatory readiness operating model
- integrated management systems guidance
- policy and document architecture enhancement
- resource economics and central solutions
- supporting templates and checklists

## Version 1.1 modern data security expansion

This version adds a modern data security and privacy expansion:

- Data Security Governance
- Privacy Engineering and Data Protection
- Zero Trust and Data-Centric Security
- Incident and Data Breach Management
- Emerging Data Security Trends
- Source Research and Mapping
- modern templates and checklists for data assets, flows, classification, privacy engineering, Zero Trust, breach response, AI security, post-quantum readiness, IoT/edge security, metrics, and trend watch


## Version 1.2 operational depth, lifecycle, and IT governance expansion

This version responds to a content-quality review:

- removed the standalone `14-diagrams` section
- embedded lifecycle diagrams into the chapters where they provide context
- added a dedicated Security Lifecycle Management chapter
- added a dedicated IT Governance and ITSM chapter
- added explanatory examples, practical scenarios, and best practices in the new chapters
- added a Content Depth Quality Standard to prevent keyword-only pages
- added templates and checklists for security lifecycle management, IT governance, ITSM evidence, service design, change security, and CMDB security completeness

The project still contains many historical pages that can be expanded further, but the editorial direction is now explicit: future pages should explain concepts, show examples, describe evidence, list common mistakes, and link to related chapters rather than only using keyword lists.

## Version 2.0 content enrichment edition

This release changes the project from a broad outline-oriented repository into a more explanatory implementation resource.

Major additions:

- all 93 Annex A control pages expanded with plain-language implementation guidance, worked examples, implementation steps, evidence, metrics, audit questions, common weaknesses, and related links
- NIST CSF 2.0 cybersecurity governance chapter
- Secure by Design and Secure by Default chapter
- deeper COBIT and ITSM integration
- six connected end-to-end case studies
- ten guided labs with suggested answers
- twelve worked risk scenarios
- expanded security-domain, auditing, evidence, automation, and security-program pages
- governance, product-security, risk, and lab templates/checklists

The editorial standard now requires descriptive text, examples, evidence guidance, best practices, common mistakes, and cross-references for substantive pages.
