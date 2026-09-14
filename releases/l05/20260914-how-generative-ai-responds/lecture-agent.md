# CS 450 L5 · How generative AI responds

- Course: CS 450 · AI and the World
- Lecture: L5 / How generative AI responds
- Semantic source: `lecture.resolved.json`
- Semantic source SHA-256: `8ca592bff81a9ea0ff70264a6138b0123c256168cd81b773cccf5f842ac92a33`
- Schema: `lecture/v1`

Normalized reader semantics, projected per block type from the resolved lecture document. Layout classes, presenter chrome, SVG drawing instructions and instructor-only fields are not part of this projection — they were never built.

## How does generative AI produce a response?

- Source lineage: `cs450-l05-how-generative-ai-responds#sections.cover`
- Citations: none

CS 450 · AI and the World · September 14, 2026

- You can say what happens between your question and the reply, and why a fluent, confident answer can still be wrong.

## It can pass the bar exam and still miscount the letters in strawberry

- Source lineage: `cs450-l05-how-generative-ai-responds#sections.scenario`
- Citations: `openai_gpt4`

### Image alternative

A bar exam result marked at the ninetieth percentile sits beside a chat reply that counts the letter r in strawberry as two.

- The same model scores in the top tenth on bar exam questions.
- You type a ten-letter word and ask it to count one letter.
- The reply appears left to right, a piece at a time, confident and complete.
- The count is wrong.

## A classifier picks a label; a generator writes the next piece

- Source lineage: `cs450-l05-how-generative-ai-responds#sections.classifier_vs_generator`
- Citations: `anthropic_transcript`, `kb_next_token`

### Diagram explanation

A classifier turns measurements into a species label and stops, while a generator turns the text so far into a next piece that is added back to the text.

- Flower measurements leads to Model
- Model leads to Species
- Text so far leads to Model
- Model leads to Next piece
- Next piece leads to Text so far: added back

- Two weeks ago the model turned inputs into one prediction: a label.

- **Generative AI**: A model whose prediction is new content, not a category.
- **Language model**: A model trained to predict the next piece of text.

- Its output goes back in as input, so it keeps going.

## The model never sees letters; it sees tokens

- Source lineage: `cs450-l05-how-generative-ai-responds#sections.tokens`
- Citations: `kb_tokens`

- **Token**: A chunk of text from a fixed list, the unit the model works in.

### Image alternative

One short sentence shown as seven coloured chunks, with thirty-six characters counted against seven tokens.

- Common words are one token; rarer words split into pieces.
- The model receives the pieces. It never counts the letters inside one.
- Limits and prices are quoted in tokens for the same reason.

## Generation is one prediction, repeated

- Source lineage: `cs450-l05-how-generative-ai-responds#sections.one_prediction_repeated`
- Citations: `kb_next_token`, `anthropic_transcript`

- **Next-token prediction**: Score every possible next piece, pick one, add it.

### Image alternative

Candidate next pieces for an unfinished sentence are ranked by score, and the top-scoring one is added to the sentence.

- Then run again on the longer text.
- A whole reply is that step a few hundred times.
- Nothing plans the sentence; each piece only follows the ones before it.

## A student asks a chat app what year Einstein published special relativity. It answers 1905, correctly. What happened?

- Source lineage: `cs450-l05-how-generative-ai-responds#sections.poll_lookup`
- Citations: none

A student asks a chat app what year Einstein published special relativity. It answers 1905, correctly. What happened?

- A. It found 1905 in a table of facts stored inside the model
- B. It predicted 1905 as the likely next piece
- C. It worked the year out from what it knows about Einstein
- D. It copied 1905 from a document it had read during training

This anonymous poll does not count toward your grade.

### Image alternative

Two ways a question could be answered, one by finding a stored fact and one by calculating a probable next piece.

## Nothing in the loop looks anything up

- Source lineage: `cs450-l05-how-generative-ai-responds#sections.nothing_looks_up`
- Citations: `anthropic_transcript`, `kb_next_token`

### Image alternative

A question about Einstein is answered by scoring candidate years and returning the highest-scoring one, with the database route crossed out.

- A search engine finds a document that already exists.
- A language model produces text that statistically follows your prompt.

- **Parameters**: Billions of numbers left behind by training, holding which pieces follow which.

- Right answers come out of the same loop: The capital of France is → Paris.

## Training played the same next-piece game on the internet

- Source lineage: `cs450-l05-how-generative-ai-responds#sections.training_same_game`
- Citations: `anthropic_transcript`

- **Pre-training**: Show the model text, ask it to predict what comes next, correct it.

### Image alternative

Fluent text, correct answers and apparent reasoning sit above the waterline; statistical patterns, token co-occurrences and training-data regularities sit below it.

- Repeat over billions of examples of human writing.
- Make: training adjusts the numbers. Use: your prompt runs the finished loop.
- Using the model does not change it.

## The next piece is drawn, not chosen

- Source lineage: `cs450-l05-how-generative-ai-responds#sections.drawn_not_chosen`
- Citations: `kb_sampling`, `anthropic_transcript`

- **Sampling**: The next piece is drawn from the ranked scores, not always the top one.
- **Temperature**: A setting that sharpens the draw toward the top or spreads it out.

### Image alternative

The same candidate scores are shown at three temperature settings, sharpening to one tall bar at the lowest and spreading almost flat at the highest.

- Low temperature: nearly the same reply each time. High: more variety.
- It changes how the model picks, not what it knows. It cannot fix the count.

## The same question got three different replies

- Source lineage: `cs450-l05-how-generative-ai-responds#sections.two_replies`
- Citations: `kb_sampling`

### Image alternative

One question asked three times returns three replies that differ in wording and in how sure they sound.

- Same prompt, same model, three runs.
- Different wording, and the count can differ too.
- None of them is the answer; each is one draw.
- One screenshot cannot show what a model can or cannot do.

## You want story ideas for a creative writing class, and separately you want the exact dates pulled out of a contract. Which temperature for which?

- Source lineage: `cs450-l05-how-generative-ai-responds#sections.poll_temperature`
- Citations: `kb_sampling`

You want story ideas for a creative writing class, and separately you want the exact dates pulled out of a contract. Which temperature for which?

- A. High for both
- B. Low for both
- C. High for stories, low for dates
- D. Low for stories, high for dates

This anonymous poll does not count toward your grade.

### Image alternative

Two tasks, creative story ideas and extracting dates from documents, each with an empty temperature box above a scale from predictable to creative.

## The scores measure plausible, not true

- Source lineage: `cs450-l05-how-generative-ai-responds#sections.plausible_not_true`
- Citations: `anthropic_transcript`, `kb_tokens`

- **Hallucination**: Fluent text that is false, produced by the same loop.

### Image alternative

Two sentences about the Eiffel Tower read equally smoothly, and one of them is false.

- The scores rank what usually follows, not what is true.
- 2 scored well because that sentence shape is common.
- The letters that would have fixed it were never visible.

## The least trustworthy parts are names, numbers, and citations

- Source lineage: `cs450-l05-how-generative-ai-responds#sections.least_trustworthy`
- Citations: `anthropic_transcript`

### Image alternative

An example reply lists three academic references, and each invented title, journal and venue is flagged on the picture.

- Where a plausible sentence and a true one look alike, the loop cannot tell them apart.
- Names, numbers, dates, quotations and citations are exactly those places.
- The rest of the sentence around them can be perfectly good.
- Check those parts before you use them.

## A language model writes the next piece; it does not look anything up

- Source lineage: `cs450-l05-how-generative-ai-responds#sections.anchor`
- Citations: `kb_next_token`

### Image alternative

Candidate next pieces for an unfinished sentence are ranked by score, and the top-scoring one is added to the sentence.

- Pieces, not letters.
- One prediction, repeated.
- Drawn from scores, not looked up.
- So a confident answer is a plausible continuation, not a checked fact.
