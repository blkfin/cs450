# CS 450 L09 · Inside an AI agent

- Course: CS 450 · AI and the World
- Lecture: L09 / Inside an AI agent
- Semantic source: `lecture.resolved.json`
- Semantic source SHA-256: `5391fb514e84888fdf87128dd6603b64a9ae254e02ef3c4be8705acbf0a719f1`
- Schema: `lecture/v1`

Normalized reader semantics, projected per block type from the resolved lecture document. Layout classes, presenter chrome, SVG drawing instructions and instructor-only fields are not part of this projection — they were never built.

## Give the software a job, not just a prompt

- Source lineage: `cs450-fall-2026-l09-inside-agent#sections.c01`
- Citations: `approved_storyboard`

### Find two Harbor Hawks home-game tickets under $60 each including fees. Show the option first. After I confirm, add a personal calendar reminder. Never buy or reserve tickets.

| Ticket-agent workspace | Current entry |
| --- | --- |
| What can it do? | ? |
| What does it know? | ? |
| How does it know when to stop? | ? |

- Fictional team, games, prices, availability, tool responses, and event IDs.

## An agent chooses actions from feedback to pursue a goal

- Source lineage: `cs450-fall-2026-l09-inside-agent#sections.c02`
- Citations: `approved_storyboard`, `huggingface_agents`

- **Agent**: A system that perceives an environment and acts toward a goal.
- **AI agent in this course**: A system in which a model chooses the next allowed action from current state, receives an observation, and may choose again.

| Definition part | Ticket carrier |
| --- | --- |
| Goal | Two qualifying tickets and a confirmed reminder |
| Perceive | Schedules, quotes, results, user confirmation |
| Act | Request an allowed lookup or calendar write |
| Choose | Model selects the next request from evidence |

## The ticket desk shows the whole system

- Source lineage: `cs450-fall-2026-l09-inside-agent#sections.c03`
- Citations: `approved_storyboard`, `grootendorst_visual`, `huggingface_agents`

### Diagram explanation

Goal and ticket state enter the model; the request passes through the harness and tool; environmental observation updates state.

- Goal + ticket state leads to Model chooses request
- Model chooses request leads to Harness checks permission + limit: requested action
- Harness checks permission + limit leads to Allowed tool runs: permit or refuse
- Allowed tool runs leads to Schedules · prices · calendar · user
- Schedules · prices · calendar · user leads to Goal + ticket state: observation

## One loop turn changes the problem

- Source lineage: `cs450-fall-2026-l09-inside-agent#sections.c04`
- Citations: `approved_storyboard`, `huggingface_agents`

### State 0

- No games known
- Model requests schedule()

### State 1

- A: Oct 10, listed $48
- B: Oct 17, listed $52
- Next call receives both results

**Caveat:** Fictional ticket records.

## iClicker 1 · What should the agent do next?

- Source lineage: `cs450-fall-2026-l09-inside-agent#sections.c05`
- Citations: `approved_storyboard`

### A: $48 + $14 fee = $62 each, over the $60 cap. B: listed $52, all-in price unknown. No option shown to user.

Which next action best follows from the goal and evidence?

1. A · Add game A because its listed price was lower
2. B · Request quote(B, seats=2)
3. C · Ask the user to approve game B now
4. D · Report that no game meets the cap

Which next action best follows from the goal and evidence?

## The plan lives in state and can change

- Source lineage: `cs450-fall-2026-l09-inside-agent#sections.c06`
- Citations: `approved_storyboard`, `grootendorst_visual`

| Workspace slot | Current state |
| --- | --- |
| Goal | 2 seats, ≤$60 each all-in; show first; no purchase |
| Rejected | A: $62 each |
| Candidate | B: $57 each; two seats available |
| Pending | User confirmation for exact reminder |
| Budget | 3 of 6 tool calls used |

### Initial idea

- schedule → quote cheapest listing → calendar

### Actual route

- schedule → quote A → reject A → quote B → ask user

## iClicker 2 · Which ticket system earns an agent?

- Source lineage: `cs450-fall-2026-l09-inside-agent#sections.c07`
- Citations: `approved_storyboard`, `anthropic_effective_agents`

Which version most benefits from a model choosing the next step?

1. A · Every Friday, post the same ticket-page link
2. B · Check A, then B, then email the cheaper result in that order
3. C · Search changing inventory and fees; choose checks from results; ask before a write
4. D · Add a calendar event from a completed form

Which version most benefits from a model choosing the next step?

## Use an agent only when adaptation pays for uncertainty

- Source lineage: `cs450-fall-2026-l09-inside-agent#sections.c08`
- Citations: `approved_storyboard`, `anthropic_effective_agents`

### Agent becomes more useful

- Route is expensive to specify
- Observations should change the next move
- Action space can be bounded
- Success can be checked

### Prefer a workflow

- Steps and branches are known
- Same sequence should run every time
- Mistakes are hard to reverse
- Done is unverifiable

**Caveat:** Fit depends on the task, checks, and cost of error.

## Put probabilistic judgment inside a deterministic shell

- Source lineage: `cs450-fall-2026-l09-inside-agent#sections.c09`
- Citations: `approved_storyboard`

### Fixed workflow

- Code fixes the branch for each condition
- Same state follows the same coded route
- Inspect which rule fired

### Model-directed agent

- Model predicts a next request from probabilities
- Same state may yield another valid request
- Inspect requests, observations, and state

- Deterministic shell: allowed tools · price cap · approval before write · step limit · exact tool execution · receipt required for done

## Autonomy is a dial, not an on/off switch

- Source lineage: `cs450-fall-2026-l09-inside-agent#sections.c10`
- Citations: `approved_storyboard`

| Level | What it may do | Ticket carrier |
| --- | --- | --- |
| 1 · Advise | Show games | allowed |
| 2 · Prepare | Draft reminder | allowed |
| 3 · Approve | Write after confirmation | this system |
| 4 · Delegate | Write within standing rules | not granted |
| 5 · Unbounded | Choose and buy | forbidden |

## iClicker 3 · Is the task done?

- Source lineage: `cs450-fall-2026-l09-inside-agent#sections.c11`
- Citations: `approved_storyboard`

### B: $57 each, two seats. User: Yes, add Oct 17 reminder. No purchase. Request: calendar.create(...). Observation: calendar not connected; no event created.

What should the system record and do?

1. A · Success, because the user approved
2. B · Success, because the model emitted the request
3. C · Blocked; report no event and what must change
4. D · Keep retrying until the event appears

What should the system record and do?

## Done is a claim about evidence

- Source lineage: `cs450-fall-2026-l09-inside-agent#sections.c12`
- Citations: `approved_storyboard`

### Assistant A

- Done. I added the reminder.
- Tool result: none

### Assistant B

- Added reminder E42 for Oct 17. No tickets purchased.
- Tool result: created; event_id=E42; correct time; no invitees

## An agent is a feedback-controlled system around a model

- Source lineage: `cs450-fall-2026-l09-inside-agent#sections.c13`
- Citations: `approved_storyboard`, `anthropic_effective_agents`, `huggingface_agents`

- **AI agent**: A goal-directed system where a model selects allowed actions, observations update external state, and the loop repeats until a stop condition.

| Closing question | Retrieval answer |
| --- | --- |
| What makes it an agent? | Model-selected next action from feedback |
| When should we use one? | Uncertain route with checkable success |
| What keeps it honest? | Bounds, state, stop conditions, and receipts |
