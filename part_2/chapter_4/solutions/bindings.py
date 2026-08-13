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


@jpipe_link("shippable:model")
@jpipe(produce=["model"])
def the_trained_model_is_on_disk(produce: JpipeProduce) -> bool:
    """[evidence] The trained model is on disk."""
    artifact = MOCKS / "model.txt"
    if not artifact.is_file():
        return False
    produce("model", artifact.read_text())
    return True


@jpipe_link("shippable:metrics")
@jpipe(produce=["metrics"])
def the_measurement_report_is_on_disk(produce: JpipeProduce) -> bool:
    """[evidence] The measurement report is on disk."""
    report = MOCKS / "measurements.json"
    if not report.is_file():
        return False
    # A report that exists but cannot be read is not a report. Saying so here keeps the
    # strategy below free to assume it received something well-formed.
    try:
        measurements = json.loads(report.read_text())
    except json.JSONDecodeError:
        return False
    produce("metrics", measurements)
    return True


@jpipe_link("shippable:bar")
@jpipe(consume=["model", "metrics"])
def the_measured_accuracy_clears_the_80_bar(model, metrics) -> bool:
    """[strategy] The measured accuracy clears the 80% bar."""
    # Both leaves are consumed, and both are used. An accuracy figure means nothing on
    # its own: it is a measurement *of* something, so an empty model file sinks the check
    # just as a low number does.
    return bool(model.strip()) and metrics.get("accuracy", 0.0) >= ACCURACY_BAR
