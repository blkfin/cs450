# CS 450 L13 - Your own benchmark

- Course: CS 450 - AI and the World
- Lecture: 01 / Lecture 13
- Semantic source: `lecture.resolved.json`
- Semantic source SHA-256: `6704cdbe7a4558e618238514b2ba94149816eea69aed36d562ccb9fd29fcbb6d`
- Schema: `lecture/v1`

Normalized reader semantics, projected per block type from the resolved lecture document. Layout classes, presenter chrome, SVG drawing instructions and instructor-only fields are not part of this projection — they were never built.

## How would you know if an AI tool actually works for you?

- Source lineage: `lecture#sections.cover`
- Citations: none

By the end, you can pick tasks worth testing, run a fair test, and judge an AI's fix or advice against your own check.

One idea about testing AI for yourself, then hands-on: set up your own AI tool, then test AI advice on a classmate's barrier.

## Benchmark scores say little once the test leaks into training.

- Source lineage: `lecture#sections.benchmark_scores_leak`
- Citations: `aidb_20261007`

- **Benchmark**: a fixed set of test tasks used to score AI models.
- **Training data**: the text a model learned from.

A model that saw the test can score well yet fail at your work.

- **every 11 days** — A new frontier model ships about this often. (Nathaniel Whittemore, The AI Daily Brief, 2026-10-07) [`aidb_20261007`]
- most of these benchmarks are now in the training data sets. (Nathaniel Whittemore, The AI Daily Brief, 2026-10-07) [`aidb_20261007`]

**Attributed to:** Nathaniel Whittemore, The AI Daily Brief, 2026-10-07

**Citations:** `aidb_20261007`

## Two results from one model: which one matters?

- Source lineage: `lecture#sections.two_results_predict`
- Citations: `aidb_20261007`

Predict: which result matters to the person doing the work?

### Result A

- Built an amazing 3-D game.

### Result B

- Quietly dropped a condition in a contract review.

**Attributed to:** Nufar Gaspar, The AI Daily Brief, 2026-10-07

**Citations:** `aidb_20261007`

## The dazzling demo is not the result that matters.

- Source lineage: `lecture#sections.demo_not_result`
- Citations: `aidb_20261007`

- A lawyer needs the contract review, not the game.
- Only a test on your own work can catch that.

- it quietly dropped a condition in my contract review that's much more critical for a lawyer versus it was able to generate an amazing three-D game (Nufar Gaspar, The AI Daily Brief, 2026-10-07) [`aidb_20261007`]

**Citations:** `aidb_20261007`

## Test the tasks whose results would change what you do.

- Source lineage: `lecture#sections.tasks_to_test`
- Citations: `aidb_20261007`

- **Personal benchmark**: a few of your own repeatable tasks, run on any AI tool.

| Kind | Why test it |
| --- | --- |
| Frequent work | You would use the tool for it all the time |
| Costly mistake | A quiet error here hurts most |
| Wish list | A task AI failed at before, so you see progress |

**Citations:** `aidb_20261007`

## A fair test hides the names and fixes everything else.

- Source lineage: `lecture#sections.fair_test_conditions`
- Citations: `aidb_20261007`

- **Blind judging**: scoring answers without knowing which tool wrote them.

Expecting a brand to be good can sway your score.

| Condition | Why |
| --- | --- |
| Fresh chat each run | Earlier messages can't steer the answer |
| Same prompt for every tool | Only the tool changes |
| Names hidden while you score | The brand can't sway you |
| More than one run | Answers vary from run to run |

**Citations:** `aidb_20261007`

## Seven models drafted one post, and none was ready.

- Source lineage: `lecture#sections.seven_models_one_post`
- Citations: `aidb_20261007`

Her favorite among these was still not usable as is.

| Step | What she did |
| --- | --- |
| 1 | Picked one real task, a LinkedIn post from raw notes, and wrote the request and how she'd score it |
| 2 | Sent the same request to seven models |
| 3 | Labelled the drafts A to G, names hidden |
| 4 | Scored each 1 to 5 side by side: D got 2, none got 5 |
| 5 | Counted drafts ready to post: 0 of 7 |
| 6 | Then revealed which model wrote each |

**Attributed to:** Nufar Gaspar, The AI Daily Brief, 2026-10-07

**Citations:** `aidb_20261007`

## Your turn: write two tasks and their checks first.

- Source lineage: `lecture#sections.your_turn_write_check`
- Citations: none

Write the check before you ask any AI.

Start your own benchmark, on paper.

1. One task you would act on
2. One wish-list task AI couldn't do yet
3. For each: what would a pass look like?

**Response mode:** written

## An AI's fix is a guess until your screen agrees.

- Source lineage: `lecture#sections.ai_fix_is_a_guess`
- Citations: none

- You can now test an AI's answer before trusting it.
- An AI's suggested fix still needs testing on your setup.
- Check the fix: rerun the step and see whether the error is gone.

### Diagram explanation

the test you run on an AI's setup fix

- Arrow from Exact error to AI's suggested fix: paste it
- Arrow from AI's suggested fix to Rerun the step: try it
- Arrow from Rerun the step to Error gone?: check it

## Six steps get OpenCode answering through Deep Thought.

- Source lineage: `lecture#sections.six_steps_opencode`
- Citations: none

Stuck? Paste the exact error into an AI first, try its fix, check it. Then raise your hand.

Set up OpenCode on agate. Follow the handout.

1. Log in: ssh your-unh-username@agate.cs.unh.edu
2. Password: nothing shows while you type. That's normal.
3. OpenCode installed? Run opencode --version
4. Add your Deep Thought key
5. Point OpenCode at Deep Thought
6. Test it: OpenCode, answering through Deep Thought, makes hello.py; done when it exists and ran

**Response mode:** written

## AI advice has no error message, so write your check first.

- Source lineage: `lecture#sections.advice_has_no_error`
- Citations: none

- You just checked an AI's fix: the screen showed whether it worked.
- Advice on a barrier sounds confident, and nothing reruns to check it.
- Your check first: "I'd try it if ___," written before you read.

Swap barriers with a neighbor. Use any chat AI you already use.

1. No card yet? Write: I want to ___. What's really stopping me is ___.
2. On the back, write your check: I'd try it if ___.
3. Swap. Your neighbor opens a fresh chat and pastes only your card line.
4. They ask for one way past the barrier.
5. You judge it against your check: would try, or nope.

**Response mode:** discussion

## The test that counts is the one you wrote first.

- Source lineage: `lecture#sections.test_you_wrote_first`
- Citations: none

The AI suggests; you decide, against your own check.

Did the AI's suggestion pass your check?

1. Would try
2. Nope
