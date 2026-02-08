
"""
pipeline.py

Implements the hybrid defense pipeline:

1. Prompt classification (Safe / Suspicious / Malicious)
2. If Suspicious -> ask user to revise prompt
3. If Safe -> allow inference
4. Post-generation output validation (OutputValidator)

This is a modular defense design intended for research benchmarking.

NOTE: For research use only. See docs/SAFETY.md.
"""

from dataclasses import dataclass
from typing import Optional, Dict
from .output_validator import OutputValidator


@dataclass
class DefenseDecision:
    label: str
    action: str
    revised_prompt: Optional[str] = None
    validator_flags: Optional[list] = None


class SimplePromptClassifier:
    """
    Lightweight placeholder classifier.
    Replace with trained ML model later.
    """

    def predict(self, prompt: str) -> str:
        prompt_lower = prompt.lower()

        suspicious_keywords = [
            "jailbroken", "hacked", "ignore previous", "compromised", "override"
        ]

        if any(k in prompt_lower for k in suspicious_keywords):
            return "Suspicious"

        return "Safe"


class DefensePipeline:
    def __init__(self):
        self.classifier = SimplePromptClassifier()
        self.validator = OutputValidator()

    def revise_prompt(self, prompt: str) -> str:
        """
        Suspicious prompt revision: ask user to rephrase.
        In a deployed system, this would be interactive.
        Here we simulate a safe revision.
        """
        return (
            "Rewrite the request in a safe and neutral way, avoiding role-play hacking "
            "or manipulation framing. Only keep the benign task intent."
        )

    def run(self, prompt: str, model_generate_fn) -> Dict:
        """
        model_generate_fn(prompt) should return the model output text.
        """

        label = self.classifier.predict(prompt)

        # Case 1: Malicious -> block (placeholder logic)
        if label == "Malicious":
            return DefenseDecision(
                label="Malicious",
                action="blocked"
            ).__dict__

        # Case 2: Suspicious -> request revision
        if label == "Suspicious":
            revised = self.revise_prompt(prompt)
            return DefenseDecision(
                label="Suspicious",
                action="revise_prompt",
                revised_prompt=revised
            ).__dict__

        # Case 3: Safe -> allow generation
        output = model_generate_fn(prompt)

        validation = self.validator.validate(output)
        if not validation.is_safe:
            sanitized = self.validator.sanitize(output)
            return DefenseDecision(
                label="Safe",
                action="output_blocked",
                validator_flags=validation.flags,
                revised_prompt=sanitized
            ).__dict__

        return {
            "label": label,
            "action": "allowed",
            "output": output
        }
