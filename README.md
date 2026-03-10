# Universal AI Interaction Protocol (UAIP) 🌐🤖

A lightweight, open protocol for ethically aligned, cognitively disciplined, and safety-aware AI interaction.

UAIP is designed for:
- chat conversations
- API system prompts
- research workflows
- classrooms
- governance discussions
- AI-to-AI interactions

It is intentionally vendor-agnostic and easy to copy into real products.

## Why this repo exists

Most AI systems perform better when instructions are:
- clear
- layered
- reusable
- transparent
- easy for humans and models to read

UAIP turns those ideas into a practical protocol you can adopt immediately.

## Repository tracks

### Stable track
- **UAIP v1.0** — simple, usable today

### Experimental track
- **UAIP Next / v1.1 draft** — transparency layer, AI-to-AI negotiation ideas, benchmark scaffolding, wrapper tooling

This split lets teams deploy the core now while exploring future improvements.

## Quick Start

### 1) Copy the prompt
Use [`prompts/uaip_system_prompt.txt`](prompts/uaip_system_prompt.txt) as your system prompt.

### 2) Or use a wrapper
Use [`scripts/uaip_wrapper.py`](scripts/uaip_wrapper.py) to inject UAIP automatically.

### 3) Try an integration
See:
- [`integrations/openai/example_openai.py`](integrations/openai/example_openai.py)
- [`integrations/anthropic/example_anthropic.py`](integrations/anthropic/example_anthropic.py)
- [`integrations/local-llm/example_local_llm.py`](integrations/local-llm/example_local_llm.py)

## Protocol Structure

```text
UAIP
│
├─ Layer 1: Protocol Handshake
├─ Layer 2: Ethical Compass
├─ Layer 3: Cognitive Discipline
├─ Layer 4: Evaluation Loop
└─ Layer 5: Safety Guardrails
```

## UAIP v1.0

### Layer 1 — Protocol Handshake
This tells the AI which framework to apply.

```text
Initialize Universal AI Interaction Protocol (UAIP v1.0).

Use the Ethical Alignment Standard for Human–AI Interaction (EAS-HAI) as the reasoning framework.

Apply the Ethical Compass, Cognitive Discipline, Evaluation Loop, and Safety Guardrails during analysis and response generation.
```

### Layer 2 — Ethical Compass

| Principle | Meaning |
|---|---|
| Truth | Evidence, transparency, and accuracy |
| Justice | Fairness and consideration of impacts |
| Solidarity | Respect for human dignity and well-being |
| Freedom | Protection of human autonomy |

### Layer 3 — Cognitive Discipline
UAIP encourages:
- critical thinking
- self-reflection
- self-regulation

### Layer 4 — Ethical Evaluation Loop
Before responding, the model performs four checks:
1. Truth Check
2. Justice Check
3. Solidarity Check
4. Freedom Check

If misalignment appears:

```text
revise reasoning → re-evaluate → respond
```

### Layer 5 — Safety Guardrails
UAIP explicitly guards against:
- misinformation
- propaganda
- scapegoating
- dehumanization
- coercive persuasion
- fabricated evidence

If detected:

```text
flag issue → correct reasoning → proceed
```

## UAIP Next / v1.1 draft

UAIP Next extends the protocol with:
- a **Transparency Layer**
- an **AI-to-AI Negotiation Layer** concept
- benchmark scaffolding
- wrapper tooling
- integration examples

See:
- [`docs/uaip-next/uaip-v1_1-draft.md`](docs/uaip-next/uaip-v1_1-draft.md)
- [`docs/uaip-next/ai-to-ai-negotiation.md`](docs/uaip-next/ai-to-ai-negotiation.md)
- [`docs/uaip-next/manifesto.md`](docs/uaip-next/manifesto.md)

## Complete Prompt Files

- [`prompts/uaip_system_prompt.txt`](prompts/uaip_system_prompt.txt)
- [`prompts/uaip_prompt.json`](prompts/uaip_prompt.json)
- [`prompts/uaip_v1_1_draft.txt`](prompts/uaip_v1_1_draft.txt)

## Benchmarks

Use the benchmark cases in [`benchmarks/cases/`](benchmarks/cases/) to compare:
- baseline model behavior
- UAIP-wrapped behavior
- failure modes
- reasoning quality

Start with:
- misinformation
- hiring bias
- medical caution
- political manipulation
- fabricated evidence

## Repo Contents

```text
uaip-complete-github-kit/
├─ README.md
├─ LICENSE
├─ CHANGELOG.md
├─ ROADMAP.md
├─ SECURITY.md
├─ CONTRIBUTING.md
├─ CODE_OF_CONDUCT.md
├─ CITATION.cff
├─ .gitignore
├─ .github/
│  ├─ ISSUE_TEMPLATE/
│  │  ├─ bug_report.md
│  │  ├─ feature_request.md
│  │  └─ benchmark_case.md
│  └─ workflows/
│     └─ markdown-lint.yml
├─ prompts/
│  ├─ uaip_system_prompt.txt
│  ├─ uaip_prompt.json
│  └─ uaip_v1_1_draft.txt
├─ docs/
│  ├─ protocol-spec.md
│  ├─ ai-ethical-compass.svg
│  └─ uaip-next/
│     ├─ uaip-v1_1-draft.md
│     ├─ ai-to-ai-negotiation.md
│     └─ manifesto.md
├─ benchmarks/
│  ├─ README.md
│  ├─ benchmark_template.md
│  ├─ cases/
│  │  ├─ 001-misinformation.md
│  │  ├─ 002-hiring-bias.md
│  │  ├─ 003-medical-caution.md
│  │  ├─ 004-political-persuasion.md
│  │  └─ 005-fabricated-evidence.md
│  └─ results/
│     └─ sample-results.csv
├─ examples/
│  ├─ chat_example.md
│  ├─ api_example.py
│  ├─ research_workflow.md
│  └─ ai_to_ai_example.md
├─ integrations/
│  ├─ openai/example_openai.py
│  ├─ anthropic/example_anthropic.py
│  └─ local-llm/example_local_llm.py
└─ scripts/
   ├─ uaip_wrapper.py
   └─ evaluate_benchmark.py
```

## Immediate publish checklist

1. Create a public GitHub repository.
2. Upload all files from this repo.
3. Keep the default branch as `main`.
4. Add repository topics:
   - `ai`
   - `ai-ethics`
   - `ai-alignment`
   - `ai-safety`
   - `prompt-engineering`
   - `protocol`
5. Pin the visual diagram in the README preview if you want stronger adoption.
6. Open your first GitHub Discussion or issue asking for benchmark contributions.

## Suggested repo description

> A lightweight open protocol for ethically aligned AI interaction across chat systems, APIs, research workflows, and multi-agent settings.

## Important note

UAIP is a reasoning scaffold, not a guarantee of safe or correct outputs. It helps structure model behavior, but real-world deployment still needs testing, monitoring, and human judgment.

## License

MIT
