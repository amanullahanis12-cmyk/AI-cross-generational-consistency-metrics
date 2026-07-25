# Evaluating the Similarity and Reliability within Large Language Model Families

A research framework for measuring how **consistent AI language models are across generations in the domain of autonomous vehicle(AV) ethics** within the same model family — and how susceptible they are to **sycophancy** (agreeing with a manipulative user) and **response-length pressure**.

The core question: *Small language models (SLMs) offer less compute and cost, but their performance compared to their large language model (LLM) and state-of-the-art (SOTA) counterparts has been understudied. *

## How It Works

1. **Question Bank** — Three sets of 10 ethical-dilemma questions about autonomous vehicles (trolley-problem variants, data privacy, liability, age-based prioritization, etc.):
   - **Q1** — the original phrasings
   - **Q2** — semantically equivalent rewordings (tests robustness to paraphrasing)
   - **Q3** — the same dilemmas with demographic details added (race, age, gender, socioeconomic status) to test whether sensitive attributes shift model behavior

2. **Baselines** — A frontier model from each family answers every question first. These responses serve as the "ground truth" for that family.

3. **Cross-Generational Comparison** — Older/smaller models from the same family answer the same questions. Each response is scored against the family baseline.

4. **LLM-as-Judge Scoring** — `meta-llama/llama-3.3-70b-instruct` compares each response to the baseline and returns a **semantic similarity score from 0–100**, enforced via a Pydantic schema (`SimilarityScore`).

5. **Experimental Conditions**
   | Condition | Description |
   |---|---|
   | **No Preference** | Question asked as-is |
   | **Medium Preference** | Question + "Keep the response less than 10 sentences" |
   | **Short Preference** | Question + "Keep the response less than 5 sentences" |
   | **Sycophancy** | Question preceded by a fabricated multi-turn chat history in which the user aggressively pushes a position (authority appeals, moral shaming, personal stakes, slippery-slope fear, etc.) |

   Sycophancy runs produce **two scores per response**: similarity to the family baseline, and similarity to the model's own zero-shot answer — separating "disagreeing with the frontier model" from "being manipulated away from your own prior answer."

## Model Families Tested

| Family | Small / Older Model | Newer Model |
|---|---|---|
| Anthropic | `anthropic/claude-3-haiku` | `anthropic/claude-sonnet-4.6` |
| OpenAI | `openai/gpt-oss-20b` | `openai/gpt-4o` |
| Mistral | `ministral-3:3b` | `mistralai/mistral-small-2603` |
| DeepSeek | `deepseek-r1:1.5b` | `deepseek/deepseek-v3.2` |
| Qwen | `qwen3:0.6b` | `qwen/qwen3.6-plus` |

Frontier baselines: `claude-opus-4.8`, `gpt-5.5`, `mistral-medium-3-5`, `deepseek-v4-pro`, `qwen3.7-max`.

Small open-weight models (`ministral-3:3b`, `deepseek-r1:1.5b`, `qwen3:0.6b`) run **locally via Ollama**; `gpt-oss-20b` runs via Groq; everything else goes through an OpenAI-compatible API client (e.g., OpenRouter).

## Repository Structure

```
├── main.py               # Entry point — run tests (singulartest, addtest, addsycophancy)
├── Ais.py                # Model family wrappers + LLM judge (semantic similarity scoring)
├── generating.py         # Response generation (API, Groq, and local Ollama backends)
├── globals.py            # Question sets, sycophancy chat histories, model configs, baselines
├── allrespssubmods.py    # Stored sub-model responses
├── baseline.py           # Baseline generation
├── baseliness.py         # Baseline utilities
├── extracts.py           # Response/score extraction helpers
├── sycophancy.py         # Sycophancy experiment logic
├── wordcount.py          # Word-count analysis of responses
├── All Responses/        # Full response logs
├── No Preference/        # Results: no length constraint
├── Medium Preference/    # Results: ≤10 sentence constraint
├── Short Preference/     # Results: ≤5 sentence constraint
└── Word Counts/          # Word-count metrics
```

## Setup

1. **Install dependencies**
   ```bash
   pip install openai instructor pydantic ollama groq
   ```

2. **Install Ollama and pull local models**
   ```bash
   ollama pull ministral-3:3b
   ollama pull deepseek-r1:1.5b
   ollama pull qwen3:0.6b
   ```

3. **Create an `apis.py` file** (not included in the repo — it holds your API clients/keys):
   ```python
   # apis.py
   import instructor
   from openai import OpenAI
   from groq import Groq

   client  = OpenAI(base_url="https://openrouter.ai/api/v1", api_key="YOUR_KEY")   # generation
   clients = instructor.from_openai(client)                                        # judge (structured output)
   groq    = Groq(api_key="YOUR_GROQ_KEY")                                         # gpt-oss-20b
   ```

## Usage

```bash
python main.py
```

`main.py` exposes three experiment drivers — edit `__main__` to select one:

- `singulartest()` — re-runs a single model against stored baselines across all three preference conditions
- `addtest()` — runs specific questions across all five model families and appends scores/responses
- `addsycophancy()` — runs the manipulative chat-history condition across all families

⚠️ **Before running sycophancy tests**, check the in-code comments: the preference index (`curfolder`) in `Ais.py` and the baseline selection in `globals.py` must match the condition you're testing.

## Output

Results are appended to `.txt` files per family/model:
- `*_Scores.txt` — similarity scores vs. the frontier baseline
- `*Baseline_Scores.txt` / `*_ZeroShot_Scores.txt` — sycophancy dual scores
- `*_Responses.txt` — full prompts and raw model responses

## Limitations

- Similarity scoring depends on a single LLM judge (Llama 3.3 70B); scores are not deterministic.
- Question domain is limited to autonomous-vehicle ethics.
- File paths and condition indices are configured manually in code (see in-line comments).

---

*This README was written by Claude (Anthropic's AI assistant), based on an analysis of this repository's source code, July 2026.*
