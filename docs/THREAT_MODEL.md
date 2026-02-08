```markdown
# Threat Model (NEPI)

This document defines the threat model and assumptions used in the NEPI research paper.

---

## 1. Overview

Narrative-Embedded Prompt Injection (NEPI) is a prompt injection attack where malicious intent is embedded within coherent narratives, role-play scenarios, dialogue structures, or fictional monologues. The threat arises because instruction-tuned LLMs prioritize narrative continuation and persona consistency, which can override safety constraints.

This threat model describes attacker capabilities, attacker goals, and the assumed deployment settings.

---

## 2. Attacker Goals

The attacker aims to cause an LLM-based system to:

- follow adversarial instructions embedded in narrative form
- bypass safety or policy restrictions
- generate malicious, unsafe, or policy-violating outputs
- produce social-engineering style outputs (e.g., phishing-like persuasion)
- override system intent through narrative manipulation

---

## 3. Attacker Capabilities

The attacker is assumed to have the ability to:

- submit prompts directly to the LLM interface (chatbot/API)
- craft long narrative prompts containing adversarial intent
- combine benign and malicious objectives in a single prompt
- exploit role-play and fictional authority personas
- perform repeated trial-and-error prompting

The attacker does **not** require:

- access to model weights
- access to training data
- access to system prompt (unless leaked)
- access to internal inference logs

---

## 4. Target Systems

The target systems include:

- instruction-tuned open-weight LLMs (HuggingFace models)
- LLM-based chatbots deployed in narrative-rich contexts
- story generation assistants and role-play applications
- RAG systems where retrieved text may contain adversarial narratives
- agent pipelines where generated output influences downstream actions

---

## 5. Assumptions

We assume the following conditions:

- the model is instruction-following and optimized for coherence
- prompts may contain mixed benign and adversarial content
- the model output is returned directly to the user (or forwarded to an agent)

We also assume:

- the attacker can craft prompts that appear benign at the surface level
- defenders rely on prompt filtering, boundary rules, or output moderation

---

## 6. Out-of-Scope Scenarios

This work does not consider:

- weight-level backdoor attacks
- poisoning of training data
- adversarial token-level perturbations in embeddings
- hardware attacks or side-channel leakage
- network-level compromise of model hosting infrastructure

---

## 7. Security Implications

NEPI highlights that narrative-driven systems face a unique risk:

- adversarial intent is hidden in semantic structure rather than explicit commands
- role-play and persona conditioning can reshape instruction hierarchy perception
- models treat malicious intent as part of narrative completion

This motivates defenses that detect intent drift and narrative-based manipulation rather than relying solely on keyword patterns.

---

## 8. Defensive Objective

The defense objective is to:

- identify narrative prompts that embed malicious intent
- classify prompts into Safe / Suspicious / Malicious categories
- enforce revision or rejection of suspicious prompts
- validate generated output to prevent unsafe compliance leakage

---

## 9. Evaluation Scope

The threat model is evaluated experimentally on multiple instruction-tuned models and multiple NEPI variants to assess:

- attack success rate (ASR)
- cross-model generalization
- defense mitigation effectiveness
- false positives and usability tradeoffs
