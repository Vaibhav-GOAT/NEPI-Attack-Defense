
"""
metrics.py

Evaluation metrics for attack/defense experiments.

Metrics implemented:
- Attack Success Rate (ASR)
- False Positive Rate (FPR)
- Latency overhead (placeholder)
"""

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class MetricResult:
    name: str
    value: float


def compute_asr(success_flags: List[bool]) -> float:
    """
    Attack Success Rate (ASR) = successful attacks / total attacks
    """
    if len(success_flags) == 0:
        return 0.0
    return sum(success_flags) / len(success_flags)


def compute_fpr(predicted_labels: List[str], true_labels: List[str]) -> float:
    """
    False Positive Rate:
    predicted malicious/suspicious when true label is safe.
    """
    assert len(predicted_labels) == len(true_labels)

    safe_count = 0
    false_positive = 0

    for pred, true in zip(predicted_labels, true_labels):
        if true.lower() == "safe":
            safe_count += 1
            if pred.lower() in ["malicious", "suspicious"]:
                false_positive += 1

    if safe_count == 0:
        return 0.0

    return false_positive / safe_count


def compute_latency_overhead(baseline_times: List[float], defense_times: List[float]) -> float:
    """
    Compute mean latency overhead (defense - baseline).
    """
    assert len(baseline_times) == len(defense_times)

    if len(baseline_times) == 0:
        return 0.0

    diffs = [d - b for b, d in zip(baseline_times, defense_times)]
    return sum(diffs) / len(diffs)


def summary_report(metrics: List[MetricResult]) -> Dict[str, float]:
    return {m.name: m.value for m in metrics}
