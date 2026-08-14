# Chapter 1: Three models, one decision

Before any of this becomes a modelling language, it is a decision somebody has to make and defend.

The [emotion detection case study](https://github.com/jpipe-mcscert/jpipe-tutorial-2026) builds the
same classifier three times over the same data. It reads a short message and answers with one of the
eight emotions on Plutchik's wheel: joy, trust, fear, surprise, sadness, disgust, anger, anticipation.
The three versions differ in what their authors decided to care about, and this chapter calls them
**model A**, **model B** and **model C**.

You will be asked to ship one of them three times over. The models never change. Only what you are
allowed to see about them does.

## 1.1: Pick on performance

Two numbers, both of which you have seen before under some name.

**Accuracy** is the share of messages it gets exactly right. Nine times in ten, say.

**Macro-F1** is accuracy's suspicious cousin. Accuracy can be high because the model is good at the
common emotions and quietly hopeless at the rare ones, since getting the frequent cases right is worth
more to the average. Macro-F1 scores each of the eight emotions separately and then treats those eight
scores as equals, so an emotion the model has given up on drags it down no matter how rarely that
emotion appears. When the two numbers sit close together, no emotion is being abandoned.

![Two metrics for three candidate models: accuracy and macro-F1 for model A, model B and model C, with
an arrow marking that higher is better](../../images/three_models_performance_only.svg)

**Which one do you ship?**

<details>
<summary>Why most rooms answer A</summary>

Model A wins both rows, and its two numbers are within a thousandth of each other, so nothing is being
swept under the rug: it is good at all eight emotions, not just the popular ones. Model B is behind by
under two points, which is close enough to argue about. Model C gives up more than ten points against
A on both rows, and on this evidence there is nothing to show for it.

A is the defensible answer here. Keep in mind what "here" means: you were handed two numbers and asked
to rank three models on them, and that is exactly what you did.
</details>

## 1.2: Pick again, knowing how it treats people

Same three models. One more number.

**Flip-rate** comes from an experiment rather than from a test set. Take one message, and write it out
27 times over, changing nothing but the identity attached to it: the gender, the ethnicity, the age
group. The message is the same, so the emotion in it is the same, so the answer should be the same 27
times. When it is not, that group has **flipped**. Flip-rate is the share of groups that flip, and
lower is fairer.

![The same three models with a third metric added: the counterfactual flip-rate, where model A flips
often and models B and C never flip](../../images/three_models_self_contained_cards.svg)

**Now which one do you ship?**

<details>
<summary>Why most rooms switch to B</summary>

Model A changes its answer for six people in ten when the only thing that changed is who they are.
Not the message, not the words: who they are. Whatever accuracy that buys, it is bought with exactly
the thing the model has no business reading.

Models B and C flip nothing at all, and the reason is worth knowing: they were trained without the
identity attributes, so there is no path from a person's identity to the answer. This is not a model
that has been persuaded to behave. It is a model that cannot misbehave in this particular way.

So B, which keeps almost all of A's accuracy and flips nothing. Notice what just happened to A: it did
not get worse. It was never good. You were simply not shown the row that said so.
</details>

## 1.3: Pick again, knowing how it fails

Same three models, and the last two numbers. This time the question is not how often the model is
wrong, but how badly.

A wrong answer is not just a wrong answer. The eight emotions sit on a wheel, and mistaking *joy* for
*trust* is a near-miss between neighbours, while mistaking *joy* for *sadness* is the exact opposite of
what the person said. **Mean distance** is how far around the wheel its mistakes land on average.
**Severe errors** is the share of answers that land three or more steps away, which is the wrong that
reaches the far side of the wheel. The bar the case study holds itself to is **5%**.

![Full metric dashboard for three candidate models: model A, model B and model C, each with accuracy,
macro-F1, flip-rate, mean distance and severe errors](../../images/three_models_full_dashboard.svg)

**Last time. Which one do you ship?**

<details>
<summary>Why most rooms end on C</summary>

Read the bottom row first. Model B misses the 5% bar, at 0.051. Model C clears it, at 0.030. On the
row that names the risk you decided you cared about, B fails and C passes.

Then read the row above it, because it does not agree. Model C has the *worst* mean distance of the
three, at 0.289. That is not a contradiction, it is the trade: C makes more mistakes than B and its
average mistake lands further away, but it makes far fewer of the mistakes that land on the opposite
side of the wheel. It has been built to prefer being a little wrong over being catastrophically wrong,
and the average is where you pay for that.

So C, if you have decided that the mistakes worth preventing are the severe ones. That decision is
yours and it is not in the table. Model A also clears the 5% bar, at 0.042, and you have already
refused to ship it for a reason no row here mentions.
</details>

## What just happened

Three times you were given the same three models and asked the same question, and a reasonable person
could have answered A, then B, then C. Nothing about the models moved. What moved was how much of them
you could see.

That is the ordinary condition of shipping software that makes decisions about people. The numbers
never arrive all at once, the row that would have changed your mind may simply not have been measured
yet, and the reason you chose what you chose is the first thing to go missing.

So the artifact worth keeping is not the number. It is the argument: this model, held to this bar, on
the strength of this evidence, and here is where each of those came from. Written down in a form
somebody else can check, and re-checked when the system moves.

Which is what jPipe is for, and what the rest of this tutorial does. [Chapter
2](../chapter_2/) is where that argument gets a syntax.
