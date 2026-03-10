"""Example local LLM integration snippet.

This is a provider-agnostic pattern for any local model runner.
"""

from pathlib import Path

SYSTEM_PROMPT = Path(__file__).resolve().parents[2] / "prompts" / "uaip_system_prompt.txt"

def build_prompt(user_prompt: str) -> str:
    system = SYSTEM_PROMPT.read_text(encoding="utf-8").strip()
    return f"[SYSTEM]\n{system}\n\n[USER]\n{user_prompt}\n"

if __name__ == "__main__":
    print(build_prompt("Evaluate ethical risks of AI-assisted hiring."))
