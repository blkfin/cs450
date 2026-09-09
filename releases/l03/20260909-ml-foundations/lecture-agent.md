# CS 450 · AI and the World — L3 — ML foundations

- Course: CS 450 · AI and the World
- Lecture: L3 / ML foundations
- Semantic source: `lecture.resolved.json`
- Semantic source SHA-256: `1ee4e9efb3b1d6172b0de67ae2df7c0a6a327f07058c409fe2c9e3906b017c6c`
- Schema: `lecture/v1`

Normalized reader semantics, projected per block type from the resolved lecture document. Layout classes, presenter chrome, SVG drawing instructions and instructor-only fields are not part of this projection — they were never built.

## A model turns inputs into predictions

- Source lineage: `lecture#sections.model`
- Citations: `ml`

### Ask for evidence that an AI works on new cases.

### Diagram explanation

A learned model maps measurements to a species prediction.

- Flower measurements leads to Learned model
- Learned model leads to Species prediction

- **Model**: The learned part of a system that maps inputs to predictions.

## Examples give it something to learn from

- Source lineage: `lecture#sections.examples`
- Citations: `supervised`, `iris`

### One actual Iris example · measurements in centimetres

| Sepal length | Sepal width | Petal length | Petal width | Known species |
| --- | --- | --- | --- | --- |
| 5.1 | 3.5 | 1.4 | 0.2 | setosa |

- **Inputs / features**: The four measurements.
- **Label**: The known species we want the model to predict.
- **Supervised learning**: Learning from examples with target answers.

## Training changes it; using it makes a prediction

- Source lineage: `lecture#sections.make_use`
- Citations: `supervised`, `iris`

### TRAIN · make

- Labeled examples → fit a model
- The model is changed.

### INFER · use

- New measurements → prediction
- The fitted model is used.

**Citations:** `supervised`

### Code state 1

Train

```python
model.fit(measurements, labels)
```

### Code state 2

Use

```python
model.predict(new_measurements)
```

## Learn the pattern, not the quirks

- Source lineage: `lecture#sections.goldilocks`
- Citations: `fit`

### Image alternative

Conceptual fitting patterns; shapes identify groups. Not measured Iris results.

CS 450 · original conceptual illustration · Original course schematic; all rights reserved

## Check cases kept out of training

- Source lineage: `lecture#sections.check`
- Citations: `holdout`, `iris`, `fit`

### TRAINING FLOWERS

- Used to fit the model
- 112 examples

### HELD-OUT FLOWERS

- Kept out while fitting
- 38 examples

**Citations:** `iris`

### Diagram explanation

The score summarizes predictions on the separate cases.

- Predict species leads to Compare with kept-back label
- Compare with kept-back label leads to Count correct / checked

- **Accuracy**: Correct predictions divided by the number of cases checked.

## Learning can also use rewards for actions

- Source lineage: `lecture#sections.rewards`
- Citations: `ml`

### SUPERVISED LEARNING

- Examples with target answers
- Iris measurements + species

### REINFORCEMENT LEARNING

- Actions produce reward feedback
- Game moves → game reward

**Citations:** `ml`

## Follow the same story in Iris

- Source lineage: `lecture#sections.handoff`
- Citations: `iris`

### Diagram explanation

Separate cases provide a check on a trained model.

- Examples leads to Train
- Train leads to Model
- Model leads to Use + check

- **Decision tree**: Questions about measurements lead to a species prediction.
- **Depth**: How many levels of questions the tree can use.

- Try depth 1, then depth 3.
- Explain the new result.

## Open the Iris notebook

- Source lineage: `lecture#sections.open_notebook`
- Citations: `iris`

Get a working notebook or join the paper/projected route.

1. Open the Iris activity from the CS 450 course page.
2. In Colab, choose Runtime → Run all.
3. Find a code cell and the output underneath it.

**Response mode:** written

- Notebook: blkfin.github.io/cs450/

## Read the inputs, prediction, and check

- Source lineage: `lecture#sections.read_first_run`
- Citations: `iris`

Explain one example and one prediction.

1. Find the four input measurements and the species label.
2. Find the 38 flowers kept out of training.
3. At depth 1, read the correct count and denominator.
4. Choose one displayed case: does its prediction match its label?

**Response mode:** written

- Depth 1: 25 of 38 correct · 65.8%

## Allow more questions, then check again

- Source lineage: `lecture#sections.change_depth`
- Citations: `iris`

Predict what could change before you rerun.

1. In Step 6, change TREE_DEPTH from 1 to 3.
2. Run that cell and every cell below it.
3. Compare the new correct count on the same held-out flowers.

**Response mode:** written

- Depth 3: 37 of 38 correct · 97.4%

## Keep the claim within the evidence

- Source lineage: `lecture#sections.close`
- Citations: `iris`, `holdout`

Complete three lines.

1. Training did __; inference did __.
2. The model got __ of __ held-out flowers right.
3. That does not establish __.

**Response mode:** written

- Ask what it learned from, how it was checked, and whether the check fits your use.
