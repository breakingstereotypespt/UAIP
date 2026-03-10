"""Simple UAIP prompt wrapper."""

from pathlib import Path

DEFAULT_PROMPT_PATH = Path(__file__).resolve().parents[1] / "prompts" / "uaip_system_prompt.txt"

def uaip_wrap(user_prompt: str, protocol_path: Path = DEFAULT_PROMPT_PATH) -> str:
    """Return a combined system+user prompt block."""
    protocol = protocol_path.read_text(encoding="utf-8").strip()
    return f"{protocol}\n\nUser Request:\n{user_prompt.strip()}\n"

if __name__ == "__main__":
    demo = "Analyze the ethical risks of AI-assisted hiring."
    print(uaip_wrap(demo))
