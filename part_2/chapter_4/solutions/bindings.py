"""Solution to chapter 4: the execution layer for the `shippable` model.

One function per element of shippable.jd, tied to it by @jpipe_link("shippable:<id>").
The runner walks the model bottom-up and calls them in order, so each function answers
exactly one question, and answers it about the world rather than about itself.

The division of labour is the same one every jPipe binding uses:

  * an **evidence** leaf reports whether an artifact is there, and hands it onward. It
    renders no judgement: "the file exists" is a fact, not an opinion.
  * a **strategy** consumes what the leaves produced and judges it. This is the only
    place a threshold is allowed to appear.
  * a **conclusion** is never executed at all. The runner passes it as soon as
    everything under it passes, which is what makes the conclusion a consequence of the
    argument rather than another thing to assert.

Only the standard library is used, on purpose: this chapter adds no dependency.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Callable

from jpipe_runner.framework.decorators.jpipe_decorator import jpipe
from jpipe_runner.framework.decorators.link_decorator import jpipe_link

JpipeProduce = Callable[[str, Any], None]

#: Resolved from this file rather than the working directory, so the run behaves the same
#: wherever it is launched from.
MOCKS = Path(__file__).resolve().parent.parent / "mocks"

#: The bar the strategy holds the measurement against. It lives here, next to the check
#: that applies it, and nowhere else.
ACCURACY_BAR = 0.80

#: 4.4 breaks this argument by hand: edit a mock, rename a file. A CI run cannot do
#: either, so four variables may stand in for the world when they are set. Unset, which is
#: how you will run this on your machine, everything below reads mocks/ and nothing here
#: changes what you saw in 4.3.
#:
#:   SHIPPABLE_MODEL      "no" takes the trained model away, as renaming the file does
#:   SHIPPABLE_METRICS    "no" takes the measurement report away
#:   SHIPPABLE_ACCURACY   the accuracy the report is read as holding
#:   SHIPPABLE_BAR        the bar the strategy applies, in place of ACCURACY_BAR
TRUE_VALUES = {"1", "true", "yes", "on"}


def taken_away(variable: str) -> bool:
    """Whether the environment says this artifact is not there for this run."""
    return os.environ.get(variable, "yes").strip().lower() not in TRUE_VALUES


def number(variable: str, default: float) -> float:
    """A figure read from the environment, or the default when it is unset."""
    raw = os.environ.get(variable)
    return default if raw is None else float(raw)


@jpipe_link("shippable:model")
@jpipe(produce=["model"])
def the_trained_model_is_on_disk(produce: JpipeProduce) -> bool:
    """[evidence] The trained model is on disk."""
    artifact = MOCKS / "model.txt"
    if taken_away("SHIPPABLE_MODEL") or not artifact.is_file():
        return False
    produce("model", artifact.read_text())
    return True


@jpipe_link("shippable:metrics")
@jpipe(produce=["metrics"])
def the_measurement_report_is_on_disk(produce: JpipeProduce) -> bool:
    """[evidence] The measurement report is on disk."""
    report = MOCKS / "measurements.json"
    if taken_away("SHIPPABLE_METRICS") or not report.is_file():
        return False
    # A report that exists but cannot be read is not a report. Saying so here keeps the
    # strategy below free to assume it received something well-formed.
    try:
        measurements = json.loads(report.read_text())
    except json.JSONDecodeError:
        return False
    # The one number the strategy reads may come from the environment instead, so a CI run
    # can vary the measurement without a second mock file to keep in step with this one.
    measurements["accuracy"] = number("SHIPPABLE_ACCURACY",
                                      measurements.get("accuracy", 0.0))
    produce("metrics", measurements)
    return True


@jpipe_link("shippable:bar")
@jpipe(consume=["model", "metrics"])
def the_measured_accuracy_clears_the_80_bar(model, metrics) -> bool:
    """[strategy] The measured accuracy clears the 80% bar."""
    # Both leaves are consumed, and both are used. An accuracy figure means nothing on
    # its own: it is a measurement *of* something, so an empty model file sinks the check
    # just as a low number does.
    #
    # Moving the bar from the environment is a demonstration hook, not a pattern to copy.
    # Once it moves, the element's label still says 80% while the check applies something
    # else, and a label that no longer describes its check is the drift this tutorial is
    # about. In your own project, leave the bar where ACCURACY_BAR is.
    bar = number("SHIPPABLE_BAR", ACCURACY_BAR)
    return bool(model.strip()) and metrics.get("accuracy", 0.0) >= bar
