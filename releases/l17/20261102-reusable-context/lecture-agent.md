# Reusable context for AI assistants

- Course: CS 450 - AI and the World
- Lecture: 10 / November 2: giving an assistant reusable context
- Semantic source: `lecture.resolved.json`
- Semantic source SHA-256: `fb68593baaa99f12a8526f728ed2fcd18c898d98dce3049d942788e930c248bc`
- Schema: `lecture/v1`

Normalized reader semantics, projected per block type from the resolved lecture document. Layout classes, presenter chrome, SVG drawing instructions and instructor-only fields are not part of this projection — they were never built.

## How can an AI assistant remember what matters?

- Source lineage: `lecture#sections.card_1`
- Citations: none

- You help a student club plan an event.
- The assistant needs your club’s rules.
- You should not have to type them every time.

Takeaway: By the end, you can write reusable notes, choose their scope, and check an answer.

## Our club needs the same rules each time

- Source lineage: `lecture#sections.card_2`
- Citations: none

Club facts

```text
Book club
Budget: $40
Invitations: under 60 words
Ask before naming a venue
```

Takeaway: Context is the information supplied to the model for an answer.

## What would a fresh conversation know?

- Source lineage: `lecture#sections.card_3`
- Citations: `src_cc_memory`, `src_chatgpt_personalize`

### Chat transcript

1. **You (user):** Write an invitation to our book club event.

Takeaway: Predict before adding our club notes.

## The app must supply the context it wants used

- Source lineage: `lecture#sections.card_4`
- Citations: `src_cc_memory`, `src_chatgpt_personalize`

| Without our notes | With our notes |
| --- | --- |
| The request names a book club. | The request includes the club rules. |
| Our budget is missing. | The $40 budget is available. |
| The model may guess a venue. | The venue rule says to ask. |

Takeaway: The model itself does not remember our earlier chats. The app saves and supplies that context.

## An API lets a program make the request

- Source lineage: `lecture#sections.card_5`
- Citations: `src_unh_dt_opencode`, `src_unh_dt_pi`, `src_oai_chat_completions`

| Part | Meaning in our club example |
| --- | --- |
| Request | Instructions plus the invitation task |
| Endpoint | The DeepThought service address |
| Key | Private authorization to use the service |
| Model | The available model to answer |
| Response | The answer returned to the program |

Takeaway: We know context must be supplied. An API is a way for a program to send it directly.

## The request contains both guidance and a task

- Source lineage: `lecture#sections.card_6`
- Citations: `src_oai_chat_completions`, `src_unh_dt_opencode`

DeepThought request body

```json
{
  "model": "AVAILABLE_MODEL_ID",
  "messages": [
    {
      "role": "system",
      "content": "Book club. Budget $40. Ask before naming a venue."
    },
    {
      "role": "user",
      "content": "Write an invitation under 60 words."
    }
  ]
}
```

Takeaway: A system message supplies instructions; a user message supplies the current request.

## A returned answer still needs our judgment

- Source lineage: `lecture#sections.card_7`
- Citations: `src_cc_best_practices`

### Chat transcript

1. **Example answer (assistant):** Join our book club on Friday! We’ll meet at River Café. Bring a favorite book.

Takeaway: A successful request does not prove that the answer followed the rules.

## Reusable notes save us from retyping the rules

- Source lineage: `lecture#sections.card_8`
- Citations: `src_agentsmd`, `src_chatgpt_projects`

| Keep the notes | Supply them again |
| --- | --- |
| A text file | A supporting tool reads it |
| Project instructions | The app adds project guidance |
| Overall preferences | The app adds guidance across projects |

Takeaway: Back to our club: typing its rules for every invitation is tedious. Reusable notes keep them ready.

## Markdown adds simple structure to plain text

- Source lineage: `lecture#sections.card_9`
- Citations: `src_agentsmd`

A tiny Markdown note

```text
# Book club

## Our rules
- Keep invitations under 60 words.
- **Ask** before naming a venue.
- Keep the budget at $40.
```

Takeaway: Markdown is plain text with marks for headings, lists, and emphasis.

## AGENTS.md gives a coding tool reusable project guidance

- Source lineage: `lecture#sections.card_10`
- Citations: `src_agentsmd`, `src_opencode_rules`, `src_cc_memory`

Inside a project folder

```text
AGENTS.md
# Working rules
- Explain changes in plain language.
- Ask before deleting a file.
```

Takeaway: A coding tool is an AI assistant that works on files in a folder. It can load project instructions.

## The same idea works at different scopes

- Source lineage: `lecture#sections.card_11`
- Citations: `src_cc_memory`, `src_chatgpt_personalize`, `src_oai_help_projects`, `src_claude_help_personalize`, `src_claude_help_projects`

| Scope | ChatGPT | Claude | Coding tool |
| --- | --- | --- | --- |
| Overall | Custom instructions | Profile instructions | A personal instruction file |
| Project | Project instructions | Project instructions and knowledge | AGENTS.md or CLAUDE.md in the folder |
| Today’s task | Your message | Your message | Your request to the assistant |

Takeaway: All three supply reusable context. Scope means where a note applies. (As of Nov 2026.)

## ChatGPT separates instructions from remembered information

- Source lineage: `lecture#sections.card_12`
- Citations: `src_oai_help_memory`, `src_chatgpt_personalize`

| Mechanism | What it supplies |
| --- | --- |
| Custom instructions | Guidance you enter across chats |
| Saved memories | Details retained for future conversations |
| Reference chat history | Relevant information from past chats |

Takeaway: Instructions tell it how to respond; memory features can supply information from earlier use. (As of Nov 2026.)

## A ChatGPT project keeps related work together

- Source lineage: `lecture#sections.card_13`
- Citations: `src_oai_help_projects`

| Our note or request | Where it belongs |
| --- | --- |
| Explain unfamiliar terms. | Overall instructions |
| Ask before naming a club venue. | Project instructions |
| The club budget is $40. | Project reference notes |
| Draft Friday’s invitation. | Today’s task |

Takeaway: Project instructions apply within that project and override global custom instructions there. (As of Nov 2026.)

## Claude also separates personal and project context

- Source lineage: `lecture#sections.card_14`
- Citations: `src_claude_help_projects`, `src_claude_help_memory`, `src_claude_help_personalize`

| Mechanism | Club use |
| --- | --- |
| Profile preferences | Explain unfamiliar terms across conversations |
| Project instructions | Ask before naming a club venue |
| Project knowledge | Club facts and reference documents |
| Memory | Project memory plus relevant outside-project context |

Takeaway: Profile preferences, project instructions, project knowledge, and memory serve different jobs. (As of Nov 2026.)

## Write notes for a different club and test them

- Source lineage: `lecture#sections.card_15`
- Citations: none

Create reusable guidance for the outdoor club.

1. Separate an overall preference, club rules, and today’s task.
2. Write short Markdown guidance with a heading and a list.
3. Supply it in plain chat, then ask for the announcement.
4. Compare the answer with two specific rules.
5. Revise one rule and retry in a fresh chat with the notes.

**Response mode:** written

Takeaway: Use the outdoor club facts on your sheet. No programming or API key is needed.

## Memory works when useful context reaches the model

- Source lineage: `lecture#sections.card_16`
- Citations: `src_cc_best_practices`

| Keep | Supply | Check |
| --- | --- | --- |
| Clear reusable notes | Current task plus relevant notes | Actual answer versus two rules |

Takeaway: The model has no memory of our chats. The app keeps and supplies useful notes; we check the answer.
