# You took a test. Now test your AI.

- Course: CS 450 - AI and the World
- Lecture: 12 / Lecture 12
- Semantic source: `lecture.resolved.json`
- Semantic source SHA-256: `0141f5fd1bd51247b393b12e44e560457b3da52d11a92cc9fd1c477d53cd09e0`
- Schema: `lecture/v1`

Normalized reader semantics, projected per block type from the resolved lecture document. Layout classes, presenter chrome, SVG drawing instructions and instructor-only fields are not part of this projection — they were never built.

## What does one result actually tell you?

- Source lineage: `lecture#sections.cover`
- Citations: none

You were tested. Now you can test your AI.

By the end, you can check a rule, name what you tested, and support a trust boundary.

## Your test found an edge that one score hides.

- Source lineage: `lecture#sections.test_edge`
- Citations: none

A benchmark is fixed tasks with known answers.

| Your October 13 test | Correct |
| --- | --- |
| Define a learned rule | 94% |
| Apply it to a case | 61% |

## Who set the rule in each thermostat?

- Source lineage: `lecture#sections.rule_predict`
- Citations: none

The application gap asks who supplied the rule.

| Thermostat | Where the rule came from |
| --- | --- |
| A | Owner types 20°C; heat switches below 20°C. |
| B | Past adjustments and owner responses form a schedule. |

## A person supplies one rule; examples form the other.

- Source lineage: `lecture#sections.rule_answer`
- Citations: none

Who sets the rule separates these two cases.

| Thermostat | Rule | Why |
| --- | --- | --- |
| A | Supplied | A person set the threshold. |
| B | Learned | Examples with outcomes formed the schedule. |

## Which layer does a writing app belong to?

- Source lineage: `lecture#sections.product_predict`
- Citations: none

A result means little until you name what was tested.

| Layer | What it names |
| --- | --- |
| Lab | Organization building models |
| Model | Trained system generating outputs |
| Host | Service running the model |
| Product | App people use |
| Agent (tool loop) | Model acting through tools under permissions |

## You tested the app, not the model inside it.

- Source lineage: `lecture#sections.product_answer`
- Citations: none

Product: the app, with its settings and model. It is not the Agent layer: this app takes no actions through tools.

Writing-app test

```text
Task: rewrite a paragraph
Product: writing app
Prompt: make this shorter
Result: this app’s output on this task and prompt
```

## Does acting require learning, and does one prompt imply one cycle?

- Source lineage: `lecture#sections.agent_predict`
- Citations: none

Agent has more than one meaning; which fits each case?

Textbook agent and tool-loop cases

```text
Textbook agent: thermostat A senses temperature and switches heat.

Tool-loop agent, one request: find the weather and suggest clothing.
Read request → call weather tool → receive weather
Read weather → call wardrobe tool → receive options
Reply to user
```

## Acting needs no learning; one turn can hold several cycles.

- Source lineage: `lecture#sections.agent_answer`
- Citations: none

Textbook agent: anything that acts in an environment. Turns and cycles count a tool loop.

| Meaning | What the case shows |
| --- | --- |
| Agent (textbook): acts in an environment | Thermostat A acts without learning. |
| Turn (tool loop): prompt to next stop | One request, one final reply: 1 turn. |
| Cycle (tool loop): request tools, receive results, update state | Weather then wardrobe: 2 cycles. |

## An AI test needs a criterion first and more than one run.

- Source lineage: `lecture#sections.ai_test`
- Citations: none

A test has fixed tasks and a key; its score describes what was tested. The same AI prompt can give a different answer each run, so one answer is not the result.

| AI test | Why it is needed |
| --- | --- |
| Pass criterion: a checkable condition | Decide success before seeing an answer. |
| Fresh chat: a new conversation | Keep earlier attempts out of the conversation. |
| Same prompt, three runs | Compare outcomes under identical conditions. |

## Will the tool satisfy both checks?

- Source lineage: `lecture#sections.demo_predict`
- Citations: none

The criterion turns an impressive sentence into a test.

Prompt and criterion

```text
Write one sentence of exactly 12 words that never uses the letter e.

PASS only if:
1. Exactly 12 space-separated words
2. No e or E anywhere
```

## Three fresh runs produce a tally we can check.

- Source lineage: `lecture#sections.demo_tally`
- Citations: none

A prediction needs observed answers checked against the same criterion.

| Fresh chat | Word count | No e or E? | Pass? |
| --- | --- | --- | --- |
| 1 | [blank] | [blank] | [blank] |
| 2 | [blank] | [blank] | [blank] |
| 3 | [blank] | [blank] | [blank] |

## Changing one condition shows which condition mattered.

- Source lineage: `lecture#sections.change_one`
- Citations: none

The tally describes this prompt. If it failed, ease one condition; if it passed, its edge is still unknown.

| Test | Prompt conditions |
| --- | --- |
| Original | 12 words, no e or E |
| If it failed: ease length only | 6 words, no e or E |

## Your own task needs the same evidence.

- Source lineage: `lecture#sections.pair_test`
- Citations: none

The demo's result says nothing about your task; test it yourselves.

In pairs, test your AI tool on a task from your major or job.

1. Write a criterion you can check yourselves.
2. Predict, then repeat the same prompt in three fresh chats.
3. Change one thing; run three more until it fails.
4. Record product, prompt, checks, counts and the changed result.

**Response mode:** written

## A failure needs evidence before it supports a conclusion.

- Source lineage: `lecture#sections.earned_conclusion`
- Citations: none

You have a tally and a variant; a funny failure alone explains little. Evidence is a record another pair could check. Which pair earned its conclusion?

| Pair’s evidence | Can we check it? |
| --- | --- |
| Product, task and exact prompt | [blank] |
| Criterion and three checked outputs | [blank] |
| One changed condition and its outputs | [blank] |
| Trust boundary matching those trials | [blank] |

## A result supports a claim only within its tested conditions.

- Source lineage: `lecture#sections.close`
- Citations: none

The strongest evidence keeps trust inside the cases it checked.

Evidence sentence

```text
We tested ___.
It passed __/3 times.
Changing ___ produced ___.
We would trust it for ___, but check ___.
```
