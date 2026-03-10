"""Example Anthropic-style integration snippet.

Set your provider client separately. This file intentionally avoids requiring any SDK.
"""

from pathlib import Path

SYSTEM_PROMPT = Path(__file__).resolve().parents[2] / "prompts" / "uaip_system_prompt.txt"

def build_request(user_prompt: str):
    return {
        "system": SYSTEM_PROMPT.read_text(encoding="utf-8"),
        "messages": [
            {"role": "user", "content": user_prompt}
        ],
    }

if __name__ == "__main__":
    print(build_request("Evaluate ethical risks of AI-assisted hiring."))
