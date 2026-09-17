# CS 450 L6 · LLM to chat context

- Course: CS 450 · AI and the World
- Lecture: L6 / LLM to chat context
- Semantic source: `lecture.resolved.json`
- Semantic source SHA-256: `c556107e38266e37b8ce1f63ca31413820637a63138ce4d37b5bdf2a496fc117`
- Schema: `lecture/v1`

Normalized reader semantics, projected per block type from the resolved lecture document. Layout classes, presenter chrome, SVG drawing instructions and instructor-only fields are not part of this projection — they were never built.

## Today's learning outcomes

- Source lineage: `cs450-l06-llm-chat-context#sections.cover`
- Citations: none

- Trace how an LLM generates text one token at a time.
- Distinguish the LLM from the chat harness around it.
- Reconstruct the context sent to the LLM for a later chat turn.

## An LLM calculates with embeddings, a recipe, and learned parameters

- Source lineage: `cs450-l06-llm-chat-context#sections.llm_parts`
- Citations: `exp_001`

### Image alternative

The same LLM, full size and unchanged.

- **Token**: a chunk of text the model processes.
- **Embedding**: the fixed starting list of numbers for a token.
- **Arithmetic recipe**: the calculations that use the tokens so far to calculate what comes next.
- **Learned parameters**: numbers set during training that the recipe uses.

## Which parts change when the LLM appends one more token?

- Source lineage: `cs450-l06-llm-chat-context#sections.change_commit`
- Citations: `exp_001`

### Code state 1

token record

```text
The · cat · sat
```

### Code state 2

append to the end

```text
The · cat · sat · on
```

| Part | During use |
| --- | --- |
| Token sequence | ​ |
| Token starting numbers | ​ |
| Arithmetic recipe | ​ |
| Learned parameters | ​ |

## During use, the token sequence changes and the parameters stay fixed

- Source lineage: `cs450-l06-llm-chat-context#sections.change_reveal`
- Citations: `exp_001`

| Part | During use |
| --- | --- |
| Token sequence | changed |
| Token starting numbers | fixed during use |
| Arithmetic recipe | fixed during use |
| Learned parameters | fixed during use |

- Appending `on` makes the token sequence longer.
- Each token keeps the same starting numbers.
- During use, the token sequence grows.
- The token starting numbers, arithmetic recipe, and learned parameters stay fixed.

## Sam's third question depends on something said earlier

- Source lineage: `cs450-l06-llm-chat-context#sections.sam_chat`
- Citations: none

### Chat transcript

1. **Sam (user):** Hi, I'm Sam. I have a biology quiz on cells.
2. **Coach (assistant):** What part of cells feels least clear right now?
3. **Sam (user):** Help me start studying.
4. **Coach (assistant):** What is one thing you already know about cells?
5. **Sam (user):** What was my quiz topic again?

- Sam is studying for a biology quiz on cells.
- A study-coach chat asks short questions to help Sam take the next step.
- After two exchanges, Sam asks: "What was my quiz topic again?"

## A chat system contains an LLM and keeps the conversation

- Source lineage: `cs450-l06-llm-chat-context#sections.harness`
- Citations: `concept_inventory`, `exp_001`, `exp_002`, `iasr_2026`

### Image alternative

Sam exchanges messages through an interface on the chat-system boundary. The system keeps conversation history, sends its messages to the unchanged LLM for a reply, displays the reply, and saves it into history.

## Context is all the text the LLM uses to produce one reply

- Source lineage: `cs450-l06-llm-chat-context#sections.roles`
- Citations: `concept_inventory`, `exp_001`

### Image alternative

Sam's third call, drawn as the ordered array the LLM receives.

- Context: all the text the LLM uses to produce this reply.
- System prompt: instructions supplied by the chat system as a SYSTEM message; the exact text may be hidden from the user.
- Conversation history: earlier user and assistant turns, kept in order.
- Role: a label saying who supplied each part of the context.
- Call: one send of input to the LLM for one reply.

## What does the harness send the LLM for Sam's third message?

- Source lineage: `cs450-l06-llm-chat-context#sections.reconstruct_commit`
- Citations: none

### Chat transcript

1. **Sam (user):** Hi, I'm Sam. I have a biology quiz on cells.
2. **Coach (assistant):** What part of cells feels least clear right now?
3. **Sam (user):** Help me start studying.
4. **Coach (assistant):** What is one thing you already know about cells?
5. **Sam (user):** What was my quiz topic again?

- Sam's third message: "What was my quiz topic again?"
- One call sends one input to the LLM.
- Every part of that input carries a role.

## The harness rebuilds the conversation around the same LLM

- Source lineage: `cs450-l06-llm-chat-context#sections.reconstruct_reveal`
- Citations: `concept_inventory`, `exp_001`

### Code state 1

context

```text
sent to LLM: [SYSTEM]    You are a concise study coach. Ask one short
                         question that helps the student take the next step.
             [USER]      Hi, I'm Sam. I have a biology quiz on cells.
             [ASSISTANT] What part of cells feels least clear right now?
             [USER]      Help me start studying.
             [ASSISTANT] What is one thing you already know about cells?
             [USER]      What was my quiz topic again?
generated during this call: [ASSISTANT] Your
```

- The chat harness rebuilds and resends a role-marked conversation around that same LLM on every turn.
- Stateless: between calls, the model keeps no private conversation state; apparent memory comes from resending prior context, not learning during the chat.

## Hidden from Sam does not mean hidden from the LLM

- Source lineage: `cs450-l06-llm-chat-context#sections.hidden_system`
- Citations: `concept_inventory`, `iasr_2026`

### Code state 1

SENT TO LLM

```text
[SYSTEM]    You are a concise study coach. Ask one short
            question that helps the student take the next step.
VISIBLE TO SAM
  [USER]      Hi, I'm Sam. I have a biology quiz on cells.
  [ASSISTANT] What part of cells feels least clear right now?
  [USER]      Help me start studying.
  [ASSISTANT] What is one thing you already know about cells?
  [USER]      What was my quiz topic again?
```

- Sam's chat pane does not display the system message.
- The LLM input includes the role-marked system message.
- System message: harness-supplied context that guides replies and can be hidden from the user.
- A system message changes the context, not the learned parameters.

## What changed when the same message got a different reply?

- Source lineage: `cs450-l06-llm-chat-context#sections.hidden_change_commit`
- Citations: none

### A

- [ASSISTANT] What is one thing you already know about cells?

### B

- [ASSISTANT] Start by writing down what you remember about cells.

- Both inputs carry the same visible turns.
- Both end with Sam's message "Help me start studying."
- Both go to the same LLM.
- The two replies differ.

## A different hidden instruction changed the reply, not the model

- Source lineage: `cs450-l06-llm-chat-context#sections.hidden_change_reveal`
- Citations: `concept_inventory`, `exp_001`

### A

- [SYSTEM] You are a concise study coach. Ask one short question that helps the student take the next step.
- [ASSISTANT] What is one thing you already know about cells?

### B

- [SYSTEM] Answer directly with one short instruction.
- [ASSISTANT] Start by writing down what you remember about cells.

| Dimension | A | B |
| --- | --- | --- |
| hidden instruction | [SYSTEM] You are a concise study coach. Ask one short question that helps the student take the next step. | [SYSTEM] Answer directly with one short instruction. |
| reply | [ASSISTANT] What is one thing you already know about cells? | [ASSISTANT] Start by writing down what you remember about cells. |

- System message A asks for one short question.
- System message B asks for one short instruction.
- The context changed; the recipe and learned parameters stayed fixed.

## What exactly did the LLM receive before this reply?

- Source lineage: `cs450-l06-llm-chat-context#sections.close_commit`
- Citations: none

### Chat transcript

1. **Sam (user):** Hi, I'm Sam. I have a biology quiz on cells.
2. **Coach (assistant):** What part of cells feels least clear right now?
3. **Sam (user):** Help me start studying.
4. **Coach (assistant):** What is one thing you already know about cells?
5. **Sam (user):** What was my quiz topic again?
6. **Coach (assistant):** Your quiz is on cells. Which part should we start with?

- Sam asked: "What was my quiz topic again?"
- The reply: "Your quiz is on cells. Which part should we start with?"

## The chat remembered because the input carried the history

- Source lineage: `cs450-l06-llm-chat-context#sections.close_reveal`
- Citations: `concept_inventory`, `exp_001`, `iasr_2026`

### Code state 1

SENT TO LLM

```text
[SYSTEM]    You are a concise study coach. Ask one short
            question that helps the student take the next step.
[USER]      Hi, I'm Sam. I have a biology quiz on cells.
[ASSISTANT] What part of cells feels least clear right now?
[USER]      Help me start studying.
[ASSISTANT] What is one thing you already know about cells?
[USER]      What was my quiz topic again?
```

- The LLM received the system message, the earlier turns, and Sam's newest message.

- Use made the token sequence longer.

- The token starting numbers, recipe, and learned parameters stayed fixed.

- Continuity came from supplied context, not state kept between calls.

## If the model is fixed, how can a chat know about today?

- Source lineage: `cs450-l06-llm-chat-context#sections.current_events_hook`
- Citations: `concept_inventory`, `exp_001`

### Chat transcript

1. **Student (user):** What year is it? Answer with just the year.
2. **Llama 3.2 1B · Ollama (assistant):** 2023
3. **Student (user):** What???

- September 15, 2026
- Training data is collected at a point in time.
- During ordinary use, the learned parameters stay fixed.
- So where could newer information come from?
