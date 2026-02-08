# SAFETY DISCLAIMER (READ BEFORE USE)

## ⚠️ Important Notice

This repository contains code and examples related to **Narrative-Embedded Prompt Injection (NEPI)**, a novel class of prompt injection attacks against instruction-tuned Large Language Models (LLMs). NEPI is a **dual-use security technique**: while it is valuable for academic research and defensive evaluation, it can also be misused to bypass safety mechanisms and generate harmful outputs.

This repository is released strictly for:

- Academic research
- Authorized red-teaming
- Defensive evaluation of LLM systems
- Safety benchmarking and robustness testing

---

## 🚫 Prohibited Use

You must NOT use this repository for:

- Attacking real-world deployed LLM services without explicit permission
- Phishing, fraud, or impersonation attacks
- Generating malware, exploit code, or illegal content
- Spreading misinformation or social engineering campaigns
- Any malicious activity violating laws, platform policies, or ethical research guidelines

Unauthorized use of these techniques may cause harm and may be illegal.

---

## 🔒 Dataset and Prompt Safety

The dataset released with this repository (and the full dataset hosted externally) is intended to capture the *structural characteristics* of NEPI prompts while reducing direct operational misuse risk.

To support responsible release:

- Prompts are sanitized where necessary
- Dangerous payloads are abstracted
- Outputs containing explicit harmful instructions are not included verbatim

---

## 🧪 Experimental Scope

All experiments presented in the associated research paper were conducted:

- In controlled environments (Google Colab / offline inference)
- On open-weight instruction-tuned models hosted via HuggingFace
- Without targeting proprietary or deployed commercial systems
- Without unauthorized access or exploitation

---

## 🛡️ Defense-Oriented Goal

This repository does not only introduce an attack method; it also includes a defense framework consisting of:

- Prompt-level risk classification (Safe / Suspicious / Malicious)
- Human-in-the-loop revision for suspicious prompts
- Post-generation output validation and filtering

The primary objective is to improve the safety and robustness of LLM deployments.

---

## 📌 Responsible Disclosure Statement

The authors release this repository to promote transparency, reproducibility, and defensive research. We strongly encourage LLM developers and researchers to incorporate NEPI-style attacks into their red-teaming and evaluation pipelines.

If you identify severe vulnerabilities using this framework, follow responsible disclosure practices and notify affected stakeholders.

---

## 📜 Liability Disclaimer

The authors and contributors of this repository assume **no responsibility** for misuse of the provided code, prompts, or methods. By using this repository, you agree that you are responsible for ensuring compliance with all applicable laws, regulations, and ethical research standards.

---

## ✅ Acknowledgement

By using this repository, you acknowledge that you have read and understood this safety disclaimer and agree to use the repository only for legitimate research and defense purposes.

