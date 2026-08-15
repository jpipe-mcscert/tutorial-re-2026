# Chapter 3: Exercises

By the end of this chapter, you can:

- write a justification from a conclusion downwards, and use the compiler's diagnostics as the
  checklist of what is still missing;
- turn an argument you have written into a template, keeping what does not vary and leaving hooks
  where it does;
- implement that template twice, and decide for each hook how much argument it needs underneath it.

Three exercises, in order: a justification, a template, and two justifications implementing that
template. Everything you need syntactically is in [chapter 2](../chapter_2/), and each exercise says
which file to crib from.

## The scenario

You argue one claim here: the classifier from the [emotion detection case
study](https://github.com/jpipe-mcscert/jpipe-tutorial-2026) **fails gracefully**. The
**severe-error rate** is the share of answers that land on the far side of the emotion wheel, as
chapter 1 set out in 1.3, and the bar is **5%**.

![Full metric dashboard for three candidate models: model A, model B and model C, each with accuracy,
macro-F1, flip-rate, mean distance and severe errors](../../images/three_models_full_dashboard.svg)

Bottom row: **model C** scores 0.030 and clears the bar, where model B scores 0.051 and does not.
Model C is the model you are arguing about.

Neither that choice of model nor the 5% bar can be read off the table, and the argument you are about
to write is where both are recorded: this model, held to this bar, on the strength of this evidence.

## How to work

Fill in the stub, then ask the compiler what is still missing. There are two ways to ask, and they
report the same thing.

**In the editor.** Open the stub, then open its preview from the preview icon in the editor title
bar, or by right-clicking and choosing **jPipe**, then *Open Diagram Preview*. The **notepad icon at
the top right of the preview panel** switches it between the diagram and the diagnostic view, where
the *Problems* tab lists what the compiler has to say. It is the last icon in the toolbar and stays
there whatever the panel is showing. The report is redrawn every time you save, which makes this the
shorter loop of the two.

**On the command line.** From this directory:

```sh
jpipe diagnostic -i exercises/01_graceful.jd
```

Either way, look before you write anything. Each stub is deliberately incomplete, and each exercise
below opens with the errors it starts on. Those errors are your checklist, and you are done when the
*Problems* tab is empty or the command reports `(none)`.

To keep a diagram rather than look at it, use the download icon in the preview toolbar and pick a
format, right-click and choose **jPipe**, then *Download as SVG*, or run:

```sh
jpipe process -f svg -i exercises/01_graceful.jd -m graceful -o graceful.svg
```

Worked answers are in [solutions/](solutions/). Read them after you have tried, not before.

## 3.1: Write a justification

**File:** [exercises/01_graceful.jd](exercises/01_graceful.jd) · **Crib from:**
[chapter_2/deployable.jd](../chapter_2/deployable.jd)

**Starts on:** `[conclusion-supported] Conclusion 'claim' in model 'graceful' has no supporting
strategy`

Argue that the classifier fails gracefully. The conclusion is written for you; build the argument
underneath it. The bar is 5%, and a bar needs a measurement to be held against, so below the
conclusion there is a sub-conclusion saying the severe-error rate has been measured, and below that,
the run that produced the number and the artifacts that run consumed.

**Done when:** the diagnostics are clean, and the diagram reads top to bottom as the conclusion, the
bar it is held to, the measurement, and the two artifacts the run needed.

## 3.2: Write a template

**File:** [exercises/02_quality_gate.jd](exercises/02_quality_gate.jd) · **Crib from:**
[chapter_2/template.jd](../chapter_2/template.jd)

**Starts on:** `[conclusion-supported]` for `holds`, and `[has-abstract-support] Template
'quality_gate' declares no abstract supports`

Before you type anything, sketch on paper the argument for **accuracy**: the accuracy has been
measured, and it clears the 80% bar. Put that sketch next to what you wrote in 3.1.

They are the same argument. Two things differ: which metric was measured, and which bar it was held
against. Write the part that does not vary into the template, and leave the two parts that do as
`@support` hooks.

**Done when:** the diagnostics are clean, and your template has exactly two hooks. A third hook
usually means something that belongs to one metric rather than to both has been pushed into the
template.

## 3.3: Implement the template, twice

**File:** [exercises/03_implements.jd](exercises/03_implements.jd) · **Crib from:**
[chapter_2/template.jd](../chapter_2/template.jd)

**Starts on:** `[sub-conclusion-supported]` for `quality_gate:measured`, and `[no-abstract-support]
Abstract support 'quality_gate:bar' in justification 'graceful' was not overridden`

The template is restated at the top of the file so it stands on its own. Write `graceful` against it
first. It is the same argument as 3.1, except that the conclusion and the confronting strategy now
come from the template instead of being written a second time. Then write `accurate` for the 80%
accuracy bar, where the template supplies the same two elements again and what you write is the two
hooks.

Two things to watch as you go:

- **Fill a hook by naming it, scoped to the template:** `quality_gate:measured`. The first one is
  already filled in the stub, to show you the shape.
- **A hook does not fix how much goes under it.** `measured` needs a whole sub-argument, because a
  number nobody produced proves nothing. `bar` is agreed elsewhere and cited here, so one piece of
  evidence is enough. Both are legal, and choosing between them is a judgement about how much of the
  argument you owe.

**Done when:** the diagnostics are clean, and the model summary lists `quality_gate` as
`used by: "graceful", "accurate"`.

**If you finish early:** chapter 2's [assemble.jd](../chapter_2/assemble.jd) shows how to combine two
justifications into one. Assemble `graceful` and `accurate` into a single claim that the model is
ready for deployment.
