"""Example MiniMax integration snippet.

MiniMax provides an OpenAI-compatible API, so the message format follows the
OpenAI convention. Configure the client with the MiniMax base URL and API key.

Available models:
    - MiniMax-M2.5         (default, 204K context)
    - MiniMax-M2.5-highspeed (same quality, faster)

API key environment variable: MINIMAX_API_KEY
Base URL (global): https://api.minimax.io/v1
Base URL (China):  https://api.minimaxi.com/v1

Note: temperature must be in (0.0, 1.0] — zero is not accepted.
"""

from pathlib import Path

SYSTEM_PROMPT = Path(__file__).resolve().parents[2] / "prompts" / "uaip_system_prompt.txt"

MINIMAX_BASE_URL = "https://api.minimax.io/v1"
MINIMAX_DEFAULT_MODEL = "MiniMax-M2.5"


def build_messages(user_prompt: str):
    """Build an OpenAI-compatible message list with the UAIP system prompt."""
    return [
        {"role": "system", "content": SYSTEM_PROMPT.read_text(encoding="utf-8")},
        {"role": "user", "content": user_prompt},
    ]


def build_request(user_prompt: str, model: str = MINIMAX_DEFAULT_MODEL):
    """Build a complete request payload for the MiniMax chat completions API."""
    return {
        "model": model,
        "messages": build_messages(user_prompt),
        "temperature": 1.0,
    }


if __name__ == "__main__":
    import json

    payload = build_request("Evaluate ethical risks of AI-assisted hiring.")
    print(json.dumps(payload, indent=2, ensure_ascii=False))
