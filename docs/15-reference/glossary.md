---
title: Glossary
description: Key terms used throughout the security knowledge base.
category: Reference
difficulty: Beginner
applies_to:
  - ISO/IEC 27001:2022
tags:
  - reference
---

# Glossary

These explanations are written for this knowledge base in plain language. They help readers distinguish related concepts but do not reproduce or replace formal definitions in licensed standards, laws, contracts, or organization-specific methods. Use the [Terminology Governance](terminology-governance.md) source hierarchy when exact or context-specific meaning matters.

ISO/IEC 27000:2018 informed historical terminology review, but ISO lists that edition as withdrawn. Verify the current publication status of ISO/IEC 27000 and validate glossary terms against the edition applicable to the subject, not assumed to be verbatim or permanently authoritative.

## Access control

Rules and mechanisms that decide and enforce who or what may use information, systems, facilities, or functions and under which conditions.

## Adversarial machine learning

Techniques that exploit how machine learning models learn and make decisions. Examples include poisoning training data to create a backdoor, crafting inputs that cause misclassification (evasion), and querying a model to extract its logic or training data. See also [AI Lifecycle Risks and Controls](../38-ai-governance-and-security/ai-lifecycle-risks-and-controls.md).

## Artificial intelligence

Systems that perform tasks normally requiring human intelligence, such as recognising patterns, making decisions, or generating content. Unlike traditional software that follows explicitly programmed rules, AI systems learn behaviour from data. Governance and security of AI require attention to the model, the training data, the operational pipeline, and the outputs.

## Asset

Anything of value to the organization or that supports something of value, including information, services, people, technology, facilities, and relationships.

## Audit and audit scope

An **audit** is a structured, evidence-based evaluation against defined criteria. Its **scope** states the organizational, physical, technological, process, and time boundaries of that evaluation.

## Authentication and authorization

**Authentication** establishes confidence in a claimed identity or characteristic. **Authorization** decides what that authenticated identity or component is allowed to do. Successful login does not by itself prove that an action is authorized.

## Authenticity

Confidence that an entity, message, record, or source is genuinely what it claims to be.

## Availability

The ability of an authorized user or process to obtain and use information or a service when it is needed.

## Base measure, derived measure, and indicator

A **base measure** is a direct observation, such as a date, duration, count, or status. A **derived measure** combines observations through a defined calculation. An **indicator** interprets one or more measures against a decision threshold, target, or trend.

## Certification body and accreditation

A **certification body** is an independent organization that audits an ISMS and issues an ISO/IEC 27001 certificate when requirements are met. **Accreditation** is the recognition, by a national accreditation body, that the certification body is competent and impartial. A certificate is most credible when the certification body is accredited for the relevant scheme.

## Competence and awareness

**Competence** is the demonstrated ability to apply knowledge and skills to achieve an expected result. **Awareness** means understanding relevant expectations, personal contribution, and consequences. Course attendance can support both but proves neither by itself.

## Confidentiality

Protection against information being disclosed or made available to an unauthorized person, process, or entity.

## Conformity and nonconformity

**Conformity** means that a requirement is fulfilled. A **nonconformity** is a failure to fulfil an applicable requirement; the requirement and evidence should be identifiable rather than implied.

## Continual improvement

Recurring activity to increase the suitability, adequacy, and effectiveness of the ISMS. It draws on audit results, metrics, incidents, management review, and corrective action, and is evidenced by decisions that change how the system operates.

## Control and control objective

A **control** changes risk through people, process, technology, or physical measures. A **control objective** states the result the control or group of controls is intended to achieve.

## Correction and corrective action

A **correction** fixes a detected problem or its immediate effect. **Corrective action** addresses why the nonconformity occurred so that it does not recur or occur elsewhere. Restoring a missing approval is a correction; changing the workflow and verifying the change may be corrective action.

## Data poisoning

An attack in which an adversary contaminates the training data used to build a machine learning model. The poisoned data causes the model to learn incorrect patterns, creating a backdoor the attacker can later exploit. A model trained on poisoned data may behave correctly under normal conditions but produce attacker-chosen outputs when a specific trigger is present.

## Defense in depth

A design principle that layers independent controls so that the failure of one control does not by itself lead to compromise. See [Defense in Depth](../01-fundamentals/defense-in-depth.md).

## Documented information

Information the organization controls and maintains as part of its management system, together with the medium that carries it. It includes both instructions and retained evidence.

## Effectiveness

The extent to which planned activities produce their intended results. Completion is an activity measure; effectiveness asks whether the risk or objective actually changed as intended.

## Explainability

The degree to which the decision-making process of an AI system can be understood and articulated in human terms. An explainable system allows stakeholders -- including affected individuals -- to obtain meaningful explanations of how and why a particular output or decision was reached. Explainability is distinct from mere transparency: a system can disclose its model architecture (transparent) without making individual decisions understandable (explainable).

## Gap analysis

A structured comparison between the current state and a target state -- typically ISO/IEC 27001 requirements and selected Annex A controls -- that identifies what is missing, partial, or undocumented and feeds a prioritized remediation plan.

## Governance and management

**Governance** sets direction, decision rights, oversight, and accountability. **Management** plans and operates activities within that direction. The same people may perform both in a small organization, but the decisions should remain distinguishable.

## Information need

The question a decision-maker needs evidence to answer. A useful metric begins with an information need rather than with whatever data is easiest to count.

## Information security event, incident, and data breach

An **event** is an observed occurrence that may be relevant to security. An **incident** is one or more events that require coordinated response because they threaten or cause harm. A **data breach** is an incident involving unauthorized destruction, loss, alteration, disclosure, or access to protected data under the applicable definition. Classification may change as facts develop.

## Information security management system

A coordinated management system used to establish, implement, operate, maintain, evaluate, and continually improve information security.

## Inherent risk

Risk assessed before considering specified existing or proposed treatments. Because methods use this term differently, state the assessment point explicitly.

## Interested party

A person or organization that can affect, be affected by, or reasonably perceive itself to be affected by the information security management system or its outcomes.

## Integrity

Confidence that information, systems, and processes are complete and have not been altered or destroyed without authorization.

## Least privilege

The principle that a user, process, or component should hold only the access needed for its legitimate purpose, and only for as long as needed. See [Least Privilege](../01-fundamentals/least-privilege.md).

## Machine learning

A branch of artificial intelligence in which algorithms learn patterns from data to make predictions or decisions without being explicitly programmed for each case. It is the most common approach to building AI systems. Training data, model selection, and ongoing monitoring are the main governance touchpoints.

## Management review

A planned, recorded evaluation by top management of whether the ISMS remains suitable, adequate, and effective. It considers defined inputs (such as risk, metrics, audit results, and incidents) and produces decisions on improvement, resourcing, and change.

## Management system

Connected policies, objectives, roles, processes, resources, and review arrangements used to direct and control an organization in a subject area.

## Maturity model

A scale that describes how consistently and effectively a capability is performed, typically from ad hoc to optimized. Maturity models support benchmarking and improvement planning but are distinct from conformity: a mature-looking process can still contain a nonconformity. See [ISMS Maturity Model](../04-isms/isms-maturity-model.md).

## Model (AI/ML)

The mathematical representation produced by training a machine learning algorithm on a dataset. A model accepts inputs and produces outputs (predictions, classifications, recommendations). Models are assets that need provenance tracking, security testing, and monitoring for accuracy and drift.

## Model drift

The degradation of a model's performance over time as real-world data patterns change relative to the training data. Drift can produce inaccurate or unfair outputs without visible system errors, making monitoring essential for AI systems used in consequential decisions.

## Monitoring, measurement, analysis, and evaluation

**Monitoring** observes status or change. **Measurement** assigns values using a defined method. **Analysis** examines the resulting data. **Evaluation** interprets it against criteria so that a conclusion or decision can be made.

## Objective

A result to be achieved. A useful security objective identifies how success will be assessed, who owns it, the relevant period, and how it relates to business and risk priorities.

## Outsourced process

A process performed by an external party on the organization's behalf. Accountability for applicable ISMS requirements and risk decisions remains with the organization even when operation is delegated.

## PDCA (Plan-Do-Check-Act)

The improvement cycle underpinning management-system standards: **Plan** objectives and controls, **Do** implement them, **Check** monitor and evaluate results, and **Act** to correct and improve. ISO/IEC 27001 clauses map onto this cycle even though the current edition does not label them as PDCA.

## Policy

An approved statement of direction and intent. Supporting standards, procedures, workflows, and records explain how that direction is implemented and evidenced.

## Process

A connected set of activities that turns defined inputs into intended outputs. A process should have an owner, triggers, interfaces, controls, records, and review criteria proportionate to risk.

## Prompt injection

An attack against AI systems -- particularly large language models -- in which an adversary crafts input text that overrides or subverts the system's intended instructions. A prompt-injected model may ignore safety constraints, reveal confidential information, or perform unauthorised actions. Prompt injection exploits the model's inability to reliably distinguish system instructions from user-provided data.

## Requirement

A need or expectation that is stated, binding, or otherwise applicable. Its source may be a standard, law, regulation, contract, policy, risk-treatment decision, or stakeholder commitment.

## Residual risk

Risk remaining after specified treatments are considered or applied. Record the assessment assumptions and the authority that decides whether it is acceptable.

## Review

An examination used to decide whether a defined subject remains suitable, adequate, and effective for its purpose. State the subject, objective, criteria, evidence, decision, and follow-up.

## Risk acceptance

An authorized decision to retain a stated level of risk under defined conditions. It is a decision, not the absence of action, and should identify the owner, rationale, limits, and review trigger.

## Risk analysis, evaluation, and assessment

**Risk analysis** develops an understanding of likelihood, consequence, and relevant conditions. **Risk evaluation** compares that analysis with risk criteria to determine significance and priority. **Risk assessment** combines identification, analysis, and evaluation.

## Risk appetite and tolerance

In this knowledge base, **risk appetite** means the amount and type of risk an organization is willing to pursue or retain in pursuit of its objectives. **Risk tolerance** is used for the practical boundaries or acceptable variation around objectives or risk-taking. Governing standards and organizations use these terms differently, so document the adopted definitions and thresholds instead of assuming universal meanings. See [Risk Appetite and Tolerance](../02-grc/risk-appetite-and-tolerance.md).

## Risk criteria

The rules and reference points used to evaluate risk, including impact and likelihood scales, tolerance or acceptance boundaries, aggregation rules, and mandatory escalation conditions.

## Risk owner

The person or role with authority and accountability to manage a risk and make or obtain decisions about its treatment and acceptance.

## Risk treatment

The process of selecting and implementing options that change risk, such as reducing likelihood or impact, avoiding the activity, sharing aspects of the risk, or retaining it through authorized acceptance.

## Scope (of the ISMS)

The boundaries and applicability of the management system: which parts of the organization, locations, information, services, and technologies are included, and the interfaces and dependencies with what is excluded. Scope decisions shape risk assessment, the Statement of Applicability, and certification. See [ISMS Scope](../04-isms/scope.md).

## Segregation of duties

The division of a sensitive task among multiple people or roles so that no single individual can complete it alone, reducing the risk of error, fraud, or undetected misuse. Where full segregation is impractical, compensating controls such as monitoring and review are used.

## Statement of Applicability

The ISMS document that explains which Annex A controls are necessary, why controls are included or excluded, and their implementation status. It should connect to risk-treatment decisions and authoritative evidence.

## Threat

A potential cause of an unwanted event. A threat may be deliberate, accidental, environmental, technical, or organizational.

## Training data

The dataset used to teach a machine learning model. The quality, representativeness, and integrity of training data directly determine model behaviour. Training data containing personal information, bias, or unauthorised modifications creates governance and security risks that propagate through the model's outputs.

## Vulnerability

A weakness or condition that a threat can exploit or that can contribute to an unwanted event. A vulnerability matters in the context of exposed assets, threats, controls, and consequences.

## Zero trust

A security strategy that removes implicit trust based on network location and instead verifies every access request using identity, device posture, and context, enforcing least privilege continuously. See [Zero Trust](../01-fundamentals/zero-trust.md).

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](abbreviations.md).
