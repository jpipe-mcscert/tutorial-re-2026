# Chapter 4: Executing a model

Everything you wrote in part 1 was drawn, not run. A drawn argument will happily claim that a model is
fit to ship on a machine where no model exists, because nothing ever went and looked. This chapter is
where that stops.

The model is given to you complete in [shippable.jd](shippable.jd). Your work is the layer underneath
it: a Python function per element, each one answering its element's question about the world.

```
claim      The classifier is fit to ship        <- concluded, never executed
bar        The measured accuracy clears 80%     <- the only judgement in the argument
model      The trained model is on disk         <- a fact
metrics    The measurement report is on disk    <- a fact
```

## What is being mocked, and why

A real classifier would drag a whole toolchain behind it, and this chapter is not about classifiers.
So the artifacts are stand-ins, in [mocks/](mocks/):

- [mocks/model.txt](mocks/model.txt), a text file where a trained model would be;
- [mocks/measurements.json](mocks/measurements.json), the numbers a real evaluation run would emit.

The numbers are **model C's column from the dashboard** in chapter 3, so the accuracy your argument
is about to check is one you have already looked at. Nothing else changes: a binding that reads a
mock and a binding that reads the real thing differ only in what is behind the file name.

This chapter adds **no dependency**. `json` and `pathlib` from the standard library are all you need,
and the runner is already pinned in `Pipfile.lock`.

## Setting up

Once, from the repository root, if you have not already:

```sh
pipenv sync --dev
```

Then work from this directory.

## 4.1: Compile the model, and generate the skeleton

The runner takes two inputs and gives back one report:

![The jPipe runner takes two files: a .json holding the justification, and a .py holding the checks.
It produces a report listing each check as passed or failed](../../images/jpipe_runner_landscape.svg)

The runner does not read `.jd`. It reads the compiled form, and it needs a Python file binding
functions to elements. jPipe produces both:

```sh
jpipe process -f json   -i shippable.jd -m shippable -o shippable.json
jpipe process -f python -i shippable.jd -m shippable -o skeleton.py
```

Those two commands are the two cards on the left of the figure. Note that the report on the right has
a failing check in it: a report where everything always passes would be telling you nothing, which is
what 4.4 is about.

Open `skeleton.py`. There is one function per element, each tied to its element by
`@jpipe_link("shippable:<id>")`, and every body is `pass`. That skeleton is the starting point of
[exercises/bindings.py](exercises/bindings.py), which is the same file with the work marked out and a
`MOCKS` path added so you do not spend the chapter on relative paths. Work in that one.

Now run it:

```sh
pipenv run jpipe-runner -l exercises/bindings.py shippable.json
```

It refuses, and it tells you why:

```
[EvidenceDependencyValidator] evidence node does not produce any variables.
  • Element: shippable:model ("The trained model is on disk") [evidence]
  • Fix: Ensure the function bound to shippable:model calls produce(...) at least once.
```

**Let the tool lead for the rest of this chapter.** The runner checks the wiring before it runs
anything, and each complaint names the next thing to do. You will meet three in order: leaves that
produce nothing, then leaves whose output nobody consumes, then functions that forget to return a
verdict. Fix the one in front of you and run again.

**Done when:** you have `shippable.json`, and you have read the error above rather than skipped past it.

## 4.2: Make the facts real

**Elements:** `shippable:model`, `shippable:metrics`

An evidence leaf reports whether an artifact is there, and hands it onward. It renders no judgement:
"the file exists" is a fact, and facts are what the argument is built out of.

Each leaf needs three things:

1. `@jpipe(produce=["model"])`, declaring the name it offers to the rest of the argument;
2. a call to `produce("model", <value>)` with what it found;
3. `return True` when the artifact is there, **`return False` when it is not**.

That last one matters. Returning `False` is not an error, it is a verdict, and it is one this argument
is allowed to reach. Raising an exception instead throws away the runner's ability to tell you *which*
part of the argument stopped holding.

**Done when:** the `EvidenceDependencyValidator` error changes. It will not disappear, it will become
a different complaint, because the leaves now produce something that nothing consumes yet. That is 4.3.

## 4.3: Make the check real

**Element:** `shippable:bar`

The strategy is the one place in this file where a judgement belongs, and so the only place a
threshold may appear. It declares what it needs, takes those values as parameters, and returns whether
the bar is cleared:

```python
@jpipe(consume=["model", "metrics"])
def the_measured_accuracy_clears_the_80_bar(model, metrics) -> bool:
```

Note that `produce` is gone from both the decorator and the signature: this function produces nothing.
Note also that every name in `consume=[]` must actually be used in the body. The decorator checks, and
says so if you forget, which is a fair question to be asked: why declare a dependency you do not use?

**Done when:** the run is green, four passed and nothing failed.

```
evidence<shippable:model>   :: The trained model is on disk           | PASS |
evidence<shippable:metrics> :: The measurement report is on disk      | PASS |
strategy<shippable:bar>     :: The measured accuracy clears the 80%.. | PASS |
conclusion<shippable:claim> :: The classifier is fit to ship          | PASS |
```

The conclusion passes without you ever having written its body. The runner never calls it: a
conclusion holds when everything under it holds, which is the entire reason for writing the argument
down instead of just asserting it.

## 4.4: Break it, twice

A green run proves nothing on its own. An argument that cannot fail is not an argument, so make it
fail, in two different ways, and watch the difference.

**Lower the bar past what the model can meet.** Edit `accuracy` in
[mocks/measurements.json](mocks/measurements.json) to `0.72` and run again:

```
strategy<shippable:bar>     :: ...clears the 80% bar    | FAIL |
conclusion<shippable:claim> :: The classifier is fit... | SKIP |
```

The facts still hold: the model is there, the report is there. What failed is the *judgement*, and the
conclusion is no longer claimed.

**Now take an artifact away.** Restore `0.818`, rename `mocks/model.txt`, and run again:

```
evidence<shippable:model>   :: The trained model is on disk | FAIL |
strategy<shippable:bar>     :: ...clears the 80% bar        | SKIP |
conclusion<shippable:claim> :: The classifier is fit...     | SKIP |
```

Different shape. The check was never even attempted, because a node whose support has failed is
skipped rather than run. The runner will not let a judgement be made about a thing that is not there.

Put `model.txt` back when you are done.

**Done when:** you can say which of the two failures you would rather find in your CI log, and why.

## Where this goes

The argument is now attached to the world, and moves when the world moves. That is the whole idea, and
the rest of part 2 is what follows from it: the same `.json` handed to a runner on a CI server, which
re-checks it every time anybody pushes.

Worked answers are in [solutions/bindings.py](solutions/bindings.py). Read them after you have tried.
