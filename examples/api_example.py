"""Minimal generic API example using a UAIP system prompt."""

from pathlib import Path

system_prompt = Path("prompts/uaip_system_prompt.txt").read_text(encoding="utf-8")

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "Evaluate risks and benefits of AI-assisted loan approvals."},
]

print("Load your model client here and send `messages` to your provider SDK.")
