# Chapter 5: Assemble and refine

Every model so far has been written whole, by one person, in one file. Real assurance cases are not
built that way. Different people own different claims, and an argument that looked finished last month
turns out to rest on a leaf nobody ever justified.

jPipe has one operator for each of those situations, and this chapter is about both:

- **assemble** adds *breadth*. Several independent justifications, none aware of the others, are
  gathered under one new strategy and one new conclusion. Nothing is rewritten.
- **refine** adds *depth*. One element of an argument, asserted until now, is replaced by a whole
  justification. Only that branch changes.

Reference pages: [assemble](https://www.jpipe.org/tutorials/assemble/) and
[refine](https://www.jpipe.org/tutorials/refine/).

Nothing is executed here. Chapter 4 covered running a model; this chapter is about structure, so your
tool throughout is `jpipe diagnostic` and the model summary it prints.

## The bricks

The three quality lenses of the emotion detection case study, one file each in [bricks/](bricks/), and
each one small enough to read in a glance:

| Brick | Claims | Rests on |
|---|---|---|
| [fair](bricks/fair.jd) | The classifier is fair | the flip-rate is below 10% |
| [performant](bricks/performant.jd) | The classifier is performant | the accuracy clears the 80% bar |
| [graceful](bricks/graceful.jd) | The classifier fails gracefully | the severe-error rate is below 5% |

Those are the three columns of the dashboard you looked at in chapter 3. A fourth file,
[trustworthy](bricks/trustworthy.jd), is the detail argument 5.2 needs.

**Read the evidence labels before you start.** `performant` and `graceful` both say "The test dataset
is trustworthy", worded identically, and that is not an accident. A label is the contract between
bricks: jPipe unifies nodes that say the same thing, and it unifies on the **label**, not the id. Two
bricks that word the same artifact differently will not meet, however carefully they were named.

## 5.1: Assemble

**File:** [exercises/01_assemble.jd](exercises/01_assemble.jd) · **Crib from:**
[chapter_2/assemble.jd](../../part_1/chapter_2/assemble.jd)

![The assemble operator. Two authors each own an independent justification; both feed into an assemble
step, and the result keeps both arguments intact as sub-conclusions under a new strategy and a new
conclusion](../../images/jpipe_assemble_abstract.svg)

That is the whole contract. Each brick keeps its shape, its conclusion becomes a sub-conclusion, and
the new strategy and conclusion are the only things added. `assemble` will not invent those two labels
for you, which is the honest choice: what three lenses together entitle you to claim is a judgement,
not a derivation.

New here is `load`, one line per file you need. Paths are relative to the file doing the loading, and
globs work, so `load "../bricks/*.jd"` would pull all four at once.

**Done when:** the diagnostic is clean and `deployable` appears in the summary as:

```
conclusion(1), sub-conclusion(3), strategy(4), evidence(3)
```

Then account for that evidence count. The three bricks declare six pieces of evidence between them,
and three came out. Which ones merged, and what would have happened if `graceful` had said "the test
set is reliable" instead?

## 5.2: Refine

**File:** [exercises/02_refine.jd](exercises/02_refine.jd)

![The refine operator. A base justification has one evidence node ringed and marked as the hook; a
separate detail justification feeds in; in the result the base is unchanged except that the hooked node
has become a sub-conclusion with the detail's whole argument beneath it](../../images/jpipe_refine_operator.svg)

`graceful` claims the test dataset is trustworthy and stops there. It is a leaf, which in an assurance
case means "take my word for it". [trustworthy.jd](bricks/trustworthy.jd) is somebody actually arguing
it: the splits are disjoint, and every label is one of the eight Plutchik emotions.

Two things the compiler enforces, and one it does not.

**It does enforce that the hook lives in the base.** The hook is an element id from the *first*
argument. Get it wrong, either by naming nothing or by naming something in the detail, and you get the
same clear refusal:

```
[execution-error] hook element 'nope' not found in base model 'graceful'
```

**It does enforce a fresh name.** A refinement cannot be called what its base is called.

**It does not enforce that the refinement means the same thing.** The detail's conclusion label
replaces the hooked node's label, silently. If `trustworthy` concluded something else, the argument
would quietly start claiming that instead, in a position where a reader still sees a supported node.
Keeping the two labels identical is your job, not the tool's.

**Done when:** the diagnostic is clean, and comparing `graceful` with `graceful_deep` shows one node
that changed kind:

```
graceful        conclusion(1),                    strategy(1), evidence(2)
graceful_deep   conclusion(1), sub-conclusion(1), strategy(2), evidence(3)
```

## 5.3: Compose them

**File:** [exercises/03_composed.jd](exercises/03_composed.jd)

Refine first, then assemble: put the deepened brick into the assembly in place of the shallow one, and
let `fair` and `performant` join it untouched.

One rule of thumb, which the exercise makes you meet head on: **deepest brick first**. Where two bricks
meet on a shared label, whichever arrives first decides what kind of node it is, and a sub-conclusion
can carry an argument beneath it where a piece of evidence cannot. Assemble them the other way round
and you get:

```
[invalid-support] 'graceful_deep:trustworthy:checks' cannot support 'unified_1'
```

**Done when:** the diagnostic is clean, and you can see what happened to one particular node. In 5.1,
the assembled model contained this:

```
evidence        The test dataset is trustworthy
```

Here it contains this instead:

```
sub-conclusion  The test dataset is trustworthy
  strategy      The split is disjoint and every label is valid
    evidence    No test row appears in the training split
    evidence    Every label is one of the eight Plutchik emotions
```

`performant` cited that leaf and still does. Its file was never opened. It got a properly argued test
dataset because it happened to word its evidence the same way `graceful` did, and somebody else did
the work.

That is what these two operators are for. Assemble lets people argue their own claims without
negotiating. Refine lets one of them go deeper without disturbing anyone. Labels are what let the
results meet.

Worked answers are in [solutions/](solutions/). Read them after you have tried, not before.
