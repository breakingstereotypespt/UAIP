"""Example MiniMax integration snippet.

MiniMax provides OpenAI-compatible Chat Completions API.
API base URL: https://api.minimax.io/v1
Models: MiniMax-M2.5, MiniMax-M2.5-highspeed

Set your provider client separately. This file intentionally avoids requiring any SDK.
"""

from pathlib import Path

SYSTEM_PROMPT = Path(__file__).resolve().parents[2] / "prompts" / "uaip_system_prompt.txt"


def build_messages(user_prompt: str):
    return [
        {"role": "system", "content": SYSTEM_PROMPT.read_text(encoding="utf-8")},
        {"role": "user", "content": user_prompt},
    ]


# --- optional: working example using the openai SDK ---
#
# import os
# from openai import OpenAI
#
# client = OpenAI(
#     api_key=os.environ["MINIMAX_API_KEY"],
#     base_url="https://api.minimax.io/v1",
# )
#
# response = client.chat.completions.create(
#     model="MiniMax-M2.5",
#     messages=build_messages("Evaluate ethical risks of AI-assisted hiring."),
# )
# print(response.choices[0].message.content)


if __name__ == "__main__":
    print(build_messages("Evaluate ethical risks of AI-assisted hiring."))
