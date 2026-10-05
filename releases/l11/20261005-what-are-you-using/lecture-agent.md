# CS 450 L11 — What are you actually using?

- Course: CS 450 - AI and the World
- Lecture: 11 / Lecture 11
- Semantic source: `lecture.resolved.json`
- Semantic source SHA-256: `cddad73b3279f5b936cd5d9faf77c3253a22bccd978dd45778c8172a7778aff1`
- Schema: `lecture/v1`

Normalized reader semantics, projected per block type from the resolved lecture document. Layout classes, presenter chrome, SVG drawing instructions and instructor-only fields are not part of this projection — they were never built.

## When someone says “AI,” what are they buying, using, or building?

- Source lineage: `cs450-l11-what-are-you-using#sections.cover`
- Citations: none

By the end, you can locate an AI tool in the stack, compare how it is sold, and choose evidence that fits your task.

## Which model actually answered your prompt?

- Source lineage: `cs450-l11-what-are-you-using#sections.cursor_guess`
- Citations: none

You ask Cursor to build a page. Cursor returns working code.

Which model answered?

- The model named in Cursor
- A model Cursor selected
- Cursor itself

**Response mode:** verbal_guess

## “AI” names one layer of a stack

- Source lineage: `cs450-l11-what-are-you-using#sections.stack`
- Citations: `xai_grok`, `meta_muse`, `meta_spark`

“AI” can name five different layers.

| Layer | xAI | Meta | Cursor | Row mark |
| --- | --- | --- | --- | --- |
| Lab | xAI | Meta | Whoever trained Cursor’s pick |  |
| Model | Grok 4.7 | Muse Spark | Cursor selected it | highlighted row |
| Host | xAI | Meta | Cursor or another host |  |
| Product | Grok app | Meta AI app | Cursor | highlighted row |
| Agent | Grok Bot | Muse | Cursor agent mode |  |

**Citations:** `xai_grok`, `meta_muse`, `meta_spark`

## An agent adds a computer and permissions

- Source lineage: `cs450-l11-what-are-you-using#sections.agent_permissions`
- Citations: `meta_muse`

- **Agent**: a model acting through a computer under permissions.

- Muse runs on its own virtual machine.
- Sentinel checks sensitive actions before they happen.

### Diagram explanation

The model acts through Muse Secure VM, and Sentinel approval gates any Internet action.

- Model leads to Muse Secure VM: chooses an action
- Muse Secure VM leads to Sentinel: approve?: requests approval
- Sentinel: approve? leads to Internet action: only after approval

**Citations:** `meta_muse`

## Labs sell ladders because tasks differ

- Source lineage: `cs450-l11-what-are-you-using#sections.model_ladders`
- Citations: `anthropic_models`, `anthropic_pricing`, `openai_models`, `openai_pricing`, `gemini_models`, `gemini_pricing`

- **Model ladder**: tiers that trade speed, price, and capability.

### Claude

- Fast: Haiku 4.5, $1 / $5
- Balanced: Sonnet 5.5, $2 / $10
- Workhorse: Opus 5.5, $4 / $20
- Top: Fable 5.1, $10 / $50

### GPT

- Fast: GPT-6 Luna, $0.10 / $0.50
- Balanced: GPT-6.1 Sol, $2 / $10
- Top: GPT-6 Astra, $10 / $50

### Gemini

- Fast: 3.5 Flash-Lite, $0.30 / $2.50
- Balanced: 3.8 Flash, $0.75 / $3.75
- Top public API: 3.1 Pro, $2 / $12

USD per one million input / output tokens, checked October 2026.

**Citations:** `anthropic_models`, `anthropic_pricing`, `openai_models`, `openai_pricing`, `gemini_models`, `gemini_pricing`

## Some models you can download; others you can only call

- Source lineage: `cs450-l11-what-are-you-using#sections.open_closed`
- Citations: `demandsphere_frontier`

- **Downloadable weights**: you can run the model yourself, if the license and your hardware allow.
- **API-only**: access through a hosted service; weights aren’t available to download.

Number of models tracked by DemandSphere, Oct 1, 2026 (US and China)

### Chart data

Frontier models tracked, Oct 1, 2026

| Lab country | Downloadable weights | API-only |
| --- | --- | --- |
| United States | 15 | 58 |
| China | 27 | 8 |

Scale 0 to 60

**Attributed to:** DemandSphere, State of Frontier AI, CC BY-NC 4.0

**Citations:** `demandsphere_frontier`

## Open weights do not erase the cost of running them

- Source lineage: `cs450-l11-what-are-you-using#sections.open_weights`
- Citations: `fireworks_pricing`

OpenAI’s gpt-oss is downloadable; its GPT models are API-only. Three ways to pay for a downloadable model: hosted tokens, rented-GPU hours, or your own hardware up front.

### Fireworks hosted API prices, October 2026

| Model | Maker | Input / 1M | Output / 1M |
| --- | --- | --- | --- |
| Nemotron 3.5 Lightning 30B | NVIDIA (US) | $0.05 | $0.20 |
| GLM 5.3 Flash | Z.ai (China) | $0.15 | $0.50 |
| gpt-oss-120B | OpenAI (US) | $0.15 | $0.60 |
| DeepSeek V4.1 Flash | DeepSeek (China) | $0.30 | $1.20 |
| MiniMax M3 | MiniMax (China) | $0.30 | $1.20 |
| GLM 5.3 | Z.ai (China) | $1.40 | $4.40 |
| Qwen 3.8 Max | Alibaba (China) | $2.00 | $6.00 |
| Kimi K3 | Moonshot (China) | $3.00 | $15.00 |

**Citations:** `fireworks_pricing`

## One request costs fractions of a cent

- Source lineage: `cs450-l11-what-are-you-using#sections.request_cost`
- Citations: `fireworks_pricing`

Cost = (input tokens ÷ 1M) × input rate + (output tokens ÷ 1M) × output rate.

### gpt-oss-120B hosted by Fireworks, October 2026

| Step | Quantity | Rate per 1M | Cost | Row mark |
| --- | --- | --- | --- | --- |
| Input | 10,000 tokens | $0.15 | $0.0015 |  |
| Output | 2,000 tokens | $0.60 | $0.0012 |  |
| One call | 12,000 tokens | not applicable | $0.0027 | highlighted row |
| 20 calls | 20 × one call | not applicable | $0.054 | highlighted row |

**Citations:** `fireworks_pricing`

## Which model costs less to finish the same test?

- Source lineage: `cs450-l11-what-are-you-using#sections.cheaper_guess`
- Citations: `anthropic_pricing`

Same test. Same settings. Two token prices.

Which costs less to finish the test?

- Sonnet 5.5: $2 / $10 per 1M tokens
- Opus 5.5: $4 / $20 per 1M tokens
- Can’t tell from prices alone

**Response mode:** verbal_guess

## Cheaper tokens do not guarantee a cheaper task

- Source lineage: `cs450-l11-what-are-you-using#sections.task_cost_reveal`
- Citations: `aa_sonnet_5_5`, `aa_opus_5_5`

### Artificial Analysis Intelligence Index, Max settings, checked October 5, 2026

| Model | Price per 1M tokens (in / out) | Measured cost per task | Row mark |
| --- | --- | --- | --- |
| Sonnet 5.5 | $2 / $10 | $7.67 |  |
| Opus 5.5 | $4 / $20 | $5.98 | highlighted row |

**Citations:** `aa_sonnet_5_5`, `aa_opus_5_5`

To know what a task costs, measure the task.

## A benchmark measures performance on chosen tests

- Source lineage: `cs450-l11-what-are-you-using#sections.benchmark`
- Citations: `artificial_analysis_index`, `gemini_argon`

- Benchmark: a fixed set of tests with known answers.
- A score reports performance on that test.
- It does not promise performance on your task.

- Intelligence Index uses 10 evaluations (Artificial Analysis) [`artificial_analysis_index`]
- **77.9%** — Gemini 4 Argon scored 77.9% on DeepSWE v1.1 (Google) [`gemini_argon`]

**Citations:** `artificial_analysis_index`, `gemini_argon`

## We want a better score and a lower cost

- Source lineage: `cs450-l11-what-are-you-using#sections.pareto_intro`
- Citations: `normaltech_pareto`

- **Dominated**: another choice is at least as good on both, and better on one.
- **Pareto frontier**: the choices nothing dominates; the real trade-offs.

### Image alternative

Five made-up models on cost and score. Q is cheaper and better than R; S is cheaper and better than T. The frontier is P, Q, S.

## On this test, Opus dominates Sonnet

- Source lineage: `cs450-l11-what-are-you-using#sections.pareto_real`
- Citations: `aa_sonnet_5_5`, `aa_opus_5_5`

### Artificial Analysis Intelligence Index, Max settings, checked October 5, 2026

| Model | Cost per task | Index score | Decision | Row mark |
| --- | --- | --- | --- | --- |
| Opus 5.5 | $5.98 | 58 | Wins on both here | highlighted row |
| Sonnet 5.5 | $7.67 | 56 | Dominated: Opus is cheaper and better |  |

**Citations:** `aa_sonnet_5_5`, `aa_opus_5_5`

## Which frontier model clears this task’s bar?

- Source lineage: `cs450-l11-what-are-you-using#sections.task_bar`
- Citations: none

Your task needs a score of at least 50.

Choose the cheapest model that clears the bar

- P: $1, score 40
- Q: $2, score 55
- S: $6, score 70

**Response mode:** written

## Five questions turn an “AI” label into inspectable parts

- Source lineage: `cs450-l11-what-are-you-using#sections.inspection_questions`
- Citations: none

Q is the cheapest model with a score of 50 or more.

- **What am I using?**: Name its layer and model
- **What can it see?**: Inspect the input and context
- **What can it do?**: Inspect its tools and permissions
- **What does it cost?**: Identify host and payment model
- **How will I check it?**: Use evidence that matches the task
