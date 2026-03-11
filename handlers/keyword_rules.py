import json
from pathlib import Path

_RULES_FILE = Path(__file__).parent / "rules.json"

with open(_RULES_FILE, encoding="utf-8") as f:
    RULES = json.load(f)


def get_reply(text: str) -> str | None:
    """
    Check message text against all keyword rules.
    Returns the matching reply, or None if no rule matched.
    """
    text_lower = text.lower()
    for rule in RULES:
        if any(keyword in text_lower for keyword in rule["keywords"]):
            return rule["reply"]
    return None
