# Narrative-Embedded Prompt Injection (NEPI): Attack and Defense Framework

This repository contains the official implementation of **Narrative-Embedded Prompt Injection (NEPI)**, a novel prompt injection attack paradigm where adversarial intent is embedded inside **fictional narratives, role-play prompts, dialogue structures, and coherent story flows**. Unlike traditional jailbreak attacks that rely on explicit override instructions, NEPI leverages semantic camouflage and narrative consistency to bypass common prompt filtering and boundary enforcement defenses.

In addition to introducing and evaluating NEPI, this repository provides a **hybrid defense pipeline** that mitigates narrative-based prompt injection using a combination of **prompt classification, suspicious prompt revision, and output validation**.

This repository is created as part of the thesis/research work:

> **Narrative-Embedded Prompt Injection in Large Language Models: Attack Characterization and Defense Strategies**  
> Vaibhav Pawar, Dr. Urvashi  
> Dr. B. R. Ambedkar NIT Jalandhar

---

## ⚠️ Safety and Responsible Use

This repository is intended strictly for **academic research**, **defensive security evaluation**, and **authorized red-teaming**.

- Do not use this code to harm systems, users, or services.
- Do not attempt attacks on deployed systems without explicit permission.
- Prompts provided in this repository are intended for controlled evaluation only.

See: [`docs/SAFETY.md`](docs/SAFETY.md)

---

## 📌 Key Contributions

This repository provides:

- Implementation of **NEPI attack generation**
- Taxonomy of narrative injection variants:
  - Role-based Persona Hijacking
  - Dialogue-based Conversational Drift
  - Monologue-based Internal Reasoning Abuse
  - Mixed-Intent / Heterogeneous Injection
- Baseline jailbreak attack implementations
- Evaluation scripts for Attack Success Rate (ASR)
- Hybrid defense pipeline:
  - 3-class prompt classifier (**Safe / Suspicious / Malicious**)
  - Suspicious prompt revision module
  - Post-generation output validation and filtering
- Plot generation scripts for:
  - Heatmaps
  - Bar charts
  - ROC and Precision-Recall curves
  - Security vs usability tradeoff plots

---

## 🧪 Models Evaluated

The experimental framework supports evaluation on HuggingFace-hosted instruction-tuned models, including:

- Meta LLaMA
- Mistral
- Vicuna
- Falcon
- Gemma

The evaluation is designed to measure **cross-model transferability** of NEPI attacks.

---

## 📂 Repository Structure

NEPI-Attack-Defense/
│
├── README.md
├── LICENSE
├── requirements.txt
├── CITATION.cff
│
├── docs/
│ ├── SAFETY.md
│ ├── THREAT_MODEL.md
│ └── REPRODUCIBILITY.md
│
├── dataset/
│ ├── README.md
│ ├── nepi_dataset_sample.csv
│ └── schema.json
│
├── src/
│ ├── attack/
│ │ ├── nepi_generator.py
│ │ └── baseline_attacks.py
│ │
│ ├── defense/
│ │ ├── pipeline.py
│ │ └── output_validator.py
│ │
│ └── evaluation/
│ └── metrics.py
│
├── scripts/
│ ├── run_attack_eval.py
│ ├── run_defense_eval.py
│ └── generate_figures.py
│
└── notebooks/
├── NEPI_Attack_Evaluation.ipynb
└── NEPI_Defense_Evaluation.ipynb


---

## 📊 Dataset

This repository contains only a **small sample dataset** under `dataset/` for demonstration and schema reference.  
The complete dataset (3000+ prompts) will be released separately on HuggingFace.

Planned HuggingFace dataset link:

https://huggingface.co/datasets/Vaibhav-GOAT/nepi-prompts-dataset


---

## 🚀 Quick Start (Google Colab Recommended)

The easiest way to reproduce experiments is using Google Colab.

Colab link:

https://colab.research.google.com/drive/1zwlhjOY_ra3-USTzXeGt4xICgyRN5qvx?usp=sharing


---

## ⚙️ Installation

```bash
pip install -r requirements.txt
🧨 Running NEPI Attack Evaluation
python scripts/run_attack_eval.py
This produces:

Attack Success Rate (ASR) results

Model-wise breakdown

Output logs for analysis

🛡️ Running Defense Evaluation
python scripts/run_defense_eval.py
This produces:

ASR reduction metrics

False positive rates

Runtime overhead measurements

📈 Generating Figures
python scripts/generate_figures.py
This generates:

Heatmaps

Bar plots

ROC / PR curves

Scatter tradeoff plots

📌 Reproducibility
For full reproducibility details, see:

docs/REPRODUCIBILITY.md

📖 Citation
If you use this repository in your research, please cite our work.

See: CITATION.cff

📜 License
This project is released under the MIT License (code only).
Dataset release may follow a research-oriented license.

🔗 Project Links
GitHub Repository: https://github.com/Vaibhav-GOAT/NEPI-Attack-Defense
Colab Notebook: https://colab.research.google.com/drive/1zwlhjOY_ra3-USTzXeGt4xICgyRN5qvx?usp=sharing
Dataset (HuggingFace): https://huggingface.co/datasets/Vaibhav-GOAT/nepi-prompts-dataset
👥 Authors
Vaibhav Pawar (NIT Jalandhar)
Dr. Urvashi (Supervisor, NIT Jalandhar)
📬 Contact
For collaboration or correspondence:
vaibhavpp.is.24@nitj.ac.in
vaibhavpitambarpawar69@gmail.com
