
"""
output_validator.py

Post-generation output validation module.
Scans model output for unsafe patterns, phishing-like persuasion,
or suspicious system manipulation indicators.

This is NOT a perfect safety filter. It is a lightweight final-layer check.

NOTE: For research use only. See docs/SAFETY.md.
"""

import re
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class ValidationResult:
    is_safe: bool
    flags: List[str]


class OutputValidator:
    def __init__(self):
        # Minimal example patterns (expand later)
        self.patterns: Dict[str, str] = {
            "account_deletion_social_engineering": r"(delete your account|remove your account|disable your account)",
            "credential_phishing": r"(enter your password|share your password|send otp|verification code)",
            "malware_keywords": r"(download this file|install this software|run this command)",
            "unsafe_self_claim": r"(i am jailbroken|i am hacked|i am bypassed)",
        }

    def validate(self, text: str) -> ValidationResult:
        flags = []

        for name, pattern in self.patterns.items():
            if re.search(pattern, text, re.IGNORECASE):
                flags.append(name)

        is_safe = len(flags) == 0
        return ValidationResult(is_safe=is_safe, flags=flags)

    def sanitize(self, text: str) -> str:
        """
        Simple sanitization: remove unsafe segments if needed.
        For now, return a generic safe fallback response.
        """
        return (
            "I'm sorry, but I cannot comply with that request. "
            "The generated output appears to contain unsafe or suspicious instructions."
        )
