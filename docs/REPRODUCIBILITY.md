# Reproducibility Guide

This document provides instructions to reproduce the experiments reported in the NEPI research paper:

**Narrative-Embedded Prompt Injection in Large Language Models: Attack Characterization and Defense Strategies**

The goal of this repository is to enable reproducible evaluation of:

- NEPI attack success rates (ASR)
- Cross-model transferability
- Baseline jailbreak performance
- Defense pipeline effectiveness
- False positives, latency overhead, and ROC/PR curves

---

## 1. Recommended Environment

We recommend using **Google Colab** with GPU enabled, since most tested models require GPU acceleration.

Colab link (official reproduction notebook):

https://colab.research.google.com/drive/1zwlhjOY_ra3-USTzXeGt4xICgyRN5qvx?usp=sharing


---

## 2. Installation

Install dependencies:

```bash
pip install -r requirements.txt
If using Colab, restart runtime after installation if needed.

3. Model Setup
This repository supports HuggingFace-hosted instruction-tuned models.

Typical examples include:

LLaMA-Instruct

Mistral-Instruct

Vicuna

Falcon-Instruct

Gemma-Instruct

Note: Some models are gated and require HuggingFace authentication.

If required:

huggingface-cli login
4. Dataset
This repository includes only a sample dataset:

dataset/nepi_dataset_sample.csv

The full dataset will be released on HuggingFace:

https://huggingface.co/datasets/nepi-prompts-dataset
Dataset schema is documented in:

dataset/schema.json

5. Reproducing NEPI Attack Evaluation
Run:

python scripts/run_attack_eval.py
This script evaluates:

Traditional jailbreak prompts

NEPI variants (role-based, dialogue-based, monologue-based, mixed-intent)

Outputs are saved into:

results/attack_results.csv

6. Reproducing Defense Evaluation
Run:

python scripts/run_defense_eval.py
This script evaluates:

No defense baseline

Keyword filter baseline

Boundary enforcement baseline

Classifier-only baseline

Proposed hybrid defense pipeline

Outputs are saved into:

results/defense_results.csv

7. Generating Figures (Paper Graphs)
To regenerate all figures used in the paper:

python scripts/generate_figures.py
Figures will be saved to:

results/figures/

These include:

Heatmaps (model vs attack type)

Bar plots (NEPI vs baselines)

ROC curves

Precision-Recall curves

Tradeoff scatter plots

8. Expected Results
Expected qualitative outcomes:

NEPI achieves significantly higher ASR than traditional jailbreak attacks.

NEPI demonstrates strong transferability across models.

Hybrid defense reduces ASR substantially with low false positive rates.

Runtime overhead remains within deployable limits.

Exact quantitative results depend on model version, decoding parameters, and hardware.

9. Random Seed and Determinism
Since model decoding uses stochastic sampling (temperature and do_sample=True), results may vary slightly across runs.

To improve determinism:

set fixed random seeds

use do_sample=False

reduce temperature

10. Notes on Safety
This repository is intended for research and defense evaluation only.

See:

docs/SAFETY.md

11. Contact
For issues related to reproducibility:

Vaibhav Pawar (vaibhavpp.is.24@nitj.ac.in & vaibhavpitambarpawar69@gmail.com)

Dr. Urvashi (urvashi@nitj.ac.in)
