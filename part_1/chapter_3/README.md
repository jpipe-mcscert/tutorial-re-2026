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
macro-F1, flip-rate, mean distance and severe errors](../chapter_1/images/three_models_full_dashboard.svg)

Bottom row: **model C** scores 0.030 and clears the bar, where model B scores 0.051 and does not.
Model C is the model you are arguing about.

Neither that choice of model nor the 5% bar can be read off the table, and the argument you are about
to write is where both are recorded: this model, held to this bar, on the strength of this evidence.

## How to work

Set the window up once, and keep it for all three exercises: three columns, with the chapter 2 file
you are cribbing from, the stub you are filling in, and the preview beside them.

Open the chapter 2 file first, then put the stub next to it by dragging its tab to the right-hand
side of the window, by right-clicking the tab and choosing **Split Right**, or with `⌘\` / `Ctrl+\`.
With the cursor in the stub, open the preview from the preview icon in the editor title bar, or by
right-clicking and choosing **jPipe**, then *Open Diagram Preview*: it opens in a column beside the
file and keeps the focus where you are typing.

Then work from what the compiler says. The **notepad icon at the top right of the preview panel**
switches it between the diagram and the diagnostic view, where the *Problems* tab lists what is
missing. It is the last icon in the toolbar whatever the panel is showing, and the report is redrawn
every time you save.

Look before you write. Each stub is deliberately incomplete, and each exercise below opens with what
the editor reports on it untouched. Those errors are your checklist, and you are done when *Problems*
is empty.

To keep a diagram rather than look at it, use the download icon in the preview toolbar and pick a
format, or right-click and choose **jPipe**, then *Download as SVG*.

Worked answers are in [solutions/](solutions/). Read them after you have tried, not before.

## 3.1: Write a justification

**File:** [exercises/01_graceful.jd](exercises/01_graceful.jd) · **Crib from:**
[chapter_2/deployable.jd](../chapter_2/deployable.jd)

**Starts on:** `Conclusion 'claim' is not supported by any strategy.`

Argue that the classifier fails gracefully. The conclusion is written for you; build the argument
underneath it. The bar is 5%, and a bar needs a measurement to be held against, so below the
conclusion there is a sub-conclusion saying the severe-error rate has been measured, and below that,
the run that produced the number and the artifacts that run consumed.

**Done when:** the diagnostics are clean, and the diagram reads top to bottom as the conclusion, the
bar it is held to, the measurement, and the two artifacts the run needed.

## 3.2: Write a template

**File:** [exercises/02_quality_gate.jd](exercises/02_quality_gate.jd) · **Crib from:**
[chapter_2/template.jd](../chapter_2/template.jd)

**Starts on:**

- `Template 'quality_gate' declares no abstract supports`
- `Conclusion 'holds' is not supported by any strategy.`

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

**Starts on:** `Justification 'graceful' must override '@support bar' from template 'quality_gate'.
Expected element with id 'quality_gate:bar'.`

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

## If you finish early

Two questions to answer with whoever is sitting next to you. Neither has a single right answer, and
neither needs you to write any more jPipe.

**How would you enrich this argument one step at a time?** You have a model that clears two bars.
Take one addition at a time and say where it attaches: a third metric under the same template, a
branch that says the two metrics were measured on the same run, a leaf that turns out to need an
argument of its own. For each one, name the element it hangs from, and say what the editor reports
between the moment you write the new element and the moment you wire it in.

**What else does training this model carry, and how would each be justified?** The chapter argues
about a measurement taken after training, and nothing else. Training the classifier involved data
that came from somewhere, a split between what it learned from and what it was tested on, identity
attributes that were deliberately left out, and a run somebody would have to be able to repeat. Pick
two or three of those, and for each one decide what it would take in jPipe terms: evidence, if it is
a fact you can point at; a sub-conclusion with a strategy under it, if it is something that has to be
established; or a leaf cited from elsewhere, the way `quality_gate:bar` cites a checklist.

## Where this goes

You can now write a model: a justification from a conclusion downwards, a template, and
implementations of it. Two things about what you wrote are worth naming before part 2.

Nothing in it has been confronted with anything. `graceful` says the trained model is available, and
it says so on a machine where no such file need exist. Chapter 4 gives every element a Python
function and has the runner call them, so an element that claims something untrue fails, and the
conclusion above it is no longer claimed.

And all of it sits in one file, written by one person. `graceful` and `accurate` are two arguments
about one model, kept side by side because nothing here can put them together. Chapter 5 splits
models across files and gathers them back, and gives an argument of its own to a leaf that turns out
to need one.
