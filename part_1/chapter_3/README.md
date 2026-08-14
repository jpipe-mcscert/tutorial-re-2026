# Chapter 3: Exercises

Your turn to write. Three exercises, in order: a justification, a template, and a
justification implementing that template.

Everything you need syntactically is in [chapter 2](../chapter_2/), so keep those three files open
beside you. Each exercise below says which one to crib from.

## The scenario

The classifier from the [emotion detection case
study](https://github.com/jpipe-mcscert/jpipe-tutorial-2026) is measured three ways. Chapter 2 argued
about two of them: it is **fair** (its predictions do not change when only a person's identity does)
and it is **performant** (it gets enough answers right).

The third is the one you will argue about here: the classifier **fails gracefully**. Eight emotions
sit on a wheel, so a wrong answer can be a near-miss or the exact opposite. A model that mistakes
*joy* for *trust* is wrong in a way you can live with; one that mistakes *joy* for *sadness* is not.
The **severe-error rate** counts how often it is wrong in the second way, and the bar is **5%**.

Here is what the case study actually measured, for the three candidate models it built:

![Full metric dashboard for three candidate models: model A, model B and model C, each with accuracy,
macro-F1, flip-rate, mean distance and severe errors](../../images/three_models_full_dashboard.svg)

Read the bottom row. **Model C** scores 0.030 on severe errors and clears the 5% bar; **model B**
scores 0.051 and does not. Model C is the one you will be arguing about.

Spend a minute on the dashboard, because every decision in this chapter comes out of it. Shipping
model C rather than A or B is a decision. Setting the severe-error bar at 5% rather than 3% or 10% is
another. Neither is forced by the numbers: model A wins the top two rows outright and is still the
one you would not ship, because its flip-rate of 0.613 means it changes its prediction for six people
in ten when nothing changes but their identity.

Because these are decisions and not readings, they carry an obligation to explain themselves: this
model, held to this bar, on the strength of this evidence. Writing that explanation down in a form
somebody else can check is what you are about to do.

## How to work

Fill in the stub, then ask the compiler what is still missing. There are two ways to ask, and they
report the same thing.

**In the editor.** Open the stub and open its preview, from the preview icon in the editor title bar
or by right-clicking and choosing **jPipe**, then *Open Diagram Preview*. The **notepad icon at the
top right of the preview panel** switches it between the diagram and the diagnostic view, where the
*Problems* tab lists what the compiler has to say. It is the last icon in the toolbar and stays there
whatever the panel is showing, so it is always in the same place. The report is redrawn every time
you save, which makes this the shorter loop of the two.

**On the command line.** From this directory:

```sh
jpipe diagnostic -i exercises/01_graceful.jd
```

Either way, look *before* you write anything. Each stub is deliberately incomplete, and the
diagnostics name what is missing. They are your checklist, and you are done when the Problems tab is
empty or the command reports `(none)`.

To keep a diagram rather than just look at it, export from the preview's download menu, or run:

```sh
jpipe process -f svg -i exercises/01_graceful.jd -m graceful -o graceful.svg
```

Worked answers are in [solutions/](solutions/). Read them after you have tried, not before.

## 3.1: Write a justification

**File:** [exercises/01_graceful.jd](exercises/01_graceful.jd) · **Crib from:**
[chapter_2/deployable.jd](../chapter_2/deployable.jd)

Argue that the classifier fails gracefully. The conclusion is given; build the argument underneath
it. The bar is 5%, and a bar is worth nothing without a measurement to hold against it, so somewhere
below the conclusion there is a sub-conclusion saying the severe-error rate *has been measured*, and
below that, the run that produced the number and the artifacts that run consumed.

**Done when:** the diagnostics are clean, and the diagram reads top to bottom as an argument you
would be willing to defend.

## 3.2: Write a template

**File:** [exercises/02_quality_gate.jd](exercises/02_quality_gate.jd) · **Crib from:**
[chapter_2/template.jd](../chapter_2/template.jd)

Before you type anything, sketch on paper the argument for **accuracy**: the accuracy has been
measured, and it clears the 80% bar. Put that sketch next to what you wrote in 3.1.

They are the same argument. Only two things differ: *which* metric was measured, and *which* bar it
was held against. Capture the part that does not vary as a template, and leave the two parts that do
as `@support` hooks.

**Done when:** the diagnostics are clean, and your template has exactly two hooks. If you find
yourself wanting a third, you have probably pushed something into the template that belongs to one
metric rather than to both.

## 3.3: Implement the template, twice

**File:** [exercises/03_implements.jd](exercises/03_implements.jd) · **Crib from:**
[chapter_2/template.jd](../chapter_2/template.jd)

The template is restated at the top of the file so it stands on its own. Write `graceful` against it
first. It is the same argument as 3.1, except the conclusion and the confronting strategy now come
from the template instead of being written a second time. Then write `accurate` for the 80% accuracy
bar.

The second one is the point. Writing it should feel like almost no work, and that is the template
paying for itself.

Two things to watch as you go:

- **Fill a hook by naming it, scoped to the template:** `quality_gate:measured`. The first one is
  already filled in the stub, to show you the shape.
- **A hook is a slot, not a fixed size.** `measured` needs a whole sub-argument under it, because a
  number nobody produced proves nothing. `bar` is agreed elsewhere and merely cited here, so one
  piece of evidence is enough. Both are legal, and choosing between them is a judgement about how
  much of the argument you actually owe.

**Done when:** the diagnostics are clean, and the model summary shows `quality_gate` as
`used by: "graceful", "accurate"`.

**If you finish early:** chapter 2's [assemble.jd](../chapter_2/assemble.jd) shows how to combine two
justifications into one. Assemble `graceful` and `accurate` into a single claim that the model is
ready for deployment.
