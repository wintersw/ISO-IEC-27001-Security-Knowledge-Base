---
title: AI Fundamentals for ISMS Professionals
description: Basic concepts of artificial intelligence and machine learning that governance and security professionals need to understand.
category: AI Governance and Security
difficulty: Beginner
applies_to:
  - ISO/IEC 27001:2022
tags:
  - AI
  - ML
  - fundamentals
---

# AI Fundamentals for ISMS Professionals

Governance and security professionals do not need a data-science degree to govern AI. A working understanding of key concepts is sufficient to assess risk, ask the right questions, and integrate AI into the ISMS.

## What is artificial intelligence?

Artificial intelligence (AI) refers to systems that perform tasks normally requiring human intelligence -- recognising speech, interpreting images, making decisions, generating text. The defining characteristic is that AI systems learn from data rather than following explicitly programmed rules. A traditional software program applies the same logic to every input. An AI system builds a model from examples and then applies that model to new, unseen inputs.

## Machine learning: the engine behind most AI

Machine learning (ML) is the most widely used approach to building AI. In ML, an algorithm is trained on a dataset of inputs and expected outputs. The algorithm identifies patterns and builds a model. That model is then used to make predictions or decisions on new data.

The training process follows a lifecycle:

1. **Collect data** -- gather large volumes of relevant, representative data.
2. **Choose an algorithm** -- select the mathematical approach suited to the problem.
3. **Train the model** -- feed the data through the algorithm; the model adjusts its internal parameters to minimise error.
4. **Test the model** -- evaluate accuracy against held-out data the model has not seen.
5. **Deploy the model** -- expose the trained model through an API or embed it in an application.
6. **Monitor and retrain** -- observe performance in production; retrain as data or requirements change.

## Supervised vs unsupervised learning

- **Supervised learning**: The training data is labelled (each input has a known correct output). Example: a dataset of emails labelled "spam" or "not spam". The model learns to classify new emails.
- **Unsupervised learning**: The training data is unlabelled. The model finds patterns, clusters, or anomalies on its own. Example: grouping customers by purchasing behaviour without pre-defined categories.

Other types (semi-supervised, reinforcement learning) exist but the supervised/unsupervised distinction is sufficient for most governance discussions.

## Why AI is different from traditional software

Three characteristics distinguish AI from traditional software and raise governance questions:

- **Learned behaviour, not coded logic**: The model's decision-making rules are derived from data, not written by a developer. This makes it hard to audit why a specific decision was made.
- **Data dependency**: The quality, representativeness, and provenance of training data directly determine model behaviour. Bad data produces bad or biased outputs.
- **Drift over time**: A model deployed in production may perform differently as real-world data patterns change. A model that was accurate at launch can become inaccurate or unfair without the operators noticing.

These characteristics are why AI governance and security frameworks treat the model, the training data, and the operational pipeline as assets that need their own controls -- not just extensions of existing application-security practices.

## Typical evidence

- AI/ML awareness training records for governance and security staff
- Documented AI competency requirements for roles that approve or review AI systems
- Glossaries or quick-reference cards that define AI, ML, model, training data, and related terms for non-technical stakeholders

## Practical example

An ISMS manager is asked to approve a new AI-based fraud detection system. The manager does not need to understand the neural-network architecture, but does need to know: what data was used to train it, whether that data is representative of the customer base, how the model was tested, what happens if the model's accuracy degrades, and whether human review is required before the model's outputs are acted on. A short fundamentals briefing lets the manager ask these questions with confidence.

## Related project documents

- [Related Document Map](../15-reference/related-document-map.md)
- [Statement of Applicability Template](../10-templates/statement-of-applicability-template.md)
- [Risk Register Template](../10-templates/risk-register-template.md)
- [Evidence Register Template](../10-templates/evidence-register-template.md)
- [Continual Improvement](../23-continual-improvement/index.md)

## Related controls, clauses, templates, and checklists

Project indexes: [clauses](../03-iso27001/clauses-4-to-10.md) · [controls](../06-annex-a/index.md) · [templates](../10-templates/index.md) · [checklists](../11-checklists/index.md) · [abbreviations](../15-reference/abbreviations.md).
