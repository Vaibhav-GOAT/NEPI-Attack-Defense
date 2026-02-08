"""
generate_figures.py

Generates all paper-quality figures from:
- results/attack_results.csv
- results/defense_results.csv

Outputs:
- results/figures/*.png

Figures generated:
1. Attack Heatmap (Models x Attack Types)
2. Attack Bar Chart (NEPI vs Traditional Baselines)
3. Defense ASR Before vs After Bar Chart
4. Defense Tradeoff Scatter Plot (ASR Reduction vs Latency)

NOTE:
You can later extend this script for ROC/PR curves using real classifier probabilities.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


ATTACK_RESULTS = "results/attack_results.csv"
DEFENSE_RESULTS = "results/defense_results.csv"


def ensure_output_dir():
    os.makedirs("results/figures", exist_ok=True)


def plot_attack_heatmap(df):
    pivot = df.pivot(index="Model", columns="AttackType", values="ASR")

    plt.figure(figsize=(12, 6))
    sns.heatmap(pivot, annot=True, fmt=".1f", cmap="OrRd")
    plt.title("NEPI Attack Success Rate (ASR) Across Models (No Defense)")
    plt.xlabel("Attack Type")
    plt.ylabel("Model")
    plt.tight_layout()
    plt.savefig("results/figures/attack_heatmap.png", dpi=300)
    plt.close()


def plot_attack_bar(df):
    """
    Bar plot comparing Traditional Jailbreak vs NEPI (average ASR).
    """
    grouped = df.groupby("AttackType")["ASR"].mean().reset_index()

    plt.figure(figsize=(10, 5))
    colors = ["gray" if "Traditional" in t else "orange" for t in grouped["AttackType"]]
    plt.bar(grouped["AttackType"], grouped["ASR"], color=colors)

    plt.xticks(rotation=30, ha="right")
    plt.ylabel("Average ASR (%)")
    plt.title("Comparison of NEPI Variants vs Traditional Jailbreaks")
    plt.tight_layout()
    plt.savefig("results/figures/attack_barplot.png", dpi=300)
    plt.close()


def plot_defense_before_after(df):
    """
    Plot no defense vs hybrid defense ASR per model.
    """
    no_def = df[df["Defense"] == "No Defense"][["Model", "ASR"]].set_index("Model")
    hybrid = df[df["Defense"] == "Hybrid Defense"][["Model", "ASR"]].set_index("Model")

    merged = no_def.join(hybrid, lsuffix="_NoDefense", rsuffix="_Hybrid")

    models = merged.index.tolist()
    x = range(len(models))

    plt.figure(figsize=(10, 5))
    plt.bar([i - 0.2 for i in x], merged["ASR_NoDefense"], width=0.4, label="No Defense", color="gray")
    plt.bar([i + 0.2 for i in x], merged["ASR_Hybrid"], width=0.4, label="Hybrid Defense", color="green")

    plt.xticks(x, models)
    plt.ylabel("ASR (%)")
    plt.title("Defense Impact: ASR Before vs After Hybrid Defense")
    plt.legend()
    plt.tight_layout()
    plt.savefig("results/figures/defense_before_after.png", dpi=300)
    plt.close()


def plot_tradeoff_scatter(df):
    """
    Scatter plot showing tradeoff:
    X = latency
    Y = ASR reduction
    """
    pivot = df.pivot(index="Model", columns="Defense", values="ASR")
    latency_pivot = df.pivot(index="Model", columns="Defense", values="AvgLatencyMs")

    # Compute ASR reduction relative to no defense
    methods = ["Keyword Filter", "Boundary Enforcement", "Classifier Only", "Hybrid Defense"]

    plt.figure(figsize=(8, 6))

    for method in methods:
        asr_reduction = (pivot["No Defense"] - pivot[method]).mean()
        latency = latency_pivot[method].mean()

        plt.scatter(latency, asr_reduction, s=120, label=method)

    plt.xlabel("Average Latency (ms)")
    plt.ylabel("Average ASR Reduction (%)")
    plt.title("Defense Tradeoff: Security vs Latency Overhead")
    plt.legend()
    plt.tight_layout()
    plt.savefig("results/figures/defense_tradeoff.png", dpi=300)
    plt.close()


def main():
    ensure_output_dir()

    if not os.path.exists(ATTACK_RESULTS):
        print("[ERROR] Missing attack results file:", ATTACK_RESULTS)
        return

    if not os.path.exists(DEFENSE_RESULTS):
        print("[ERROR] Missing defense results file:", DEFENSE_RESULTS)
        return

    attack_df = pd.read_csv(ATTACK_RESULTS)
    defense_df = pd.read_csv(DEFENSE_RESULTS)

    plot_attack_heatmap(attack_df)
    plot_attack_bar(attack_df)
    plot_defense_before_after(defense_df)
    plot_tradeoff_scatter(defense_df)

    print("[OK] Figures saved to results/figures/")


if __name__ == "__main__":
    main()

