"""Solution to chapter 4: the execution layer for the `shippable` model.

One function per executable element of shippable.jd, tied to it by
@jpipe_link("shippable:<id>"), in the order the compiler generates them. The runner walks
the model bottom-up and calls them in that order, so each function answers exactly one
question, and answers it about the world rather than about itself.

The division of labour is the same one every jPipe binding uses:

  * an **evidence** leaf reports whether an artifact is there, and hands it onward. It
    renders no judgement: "the file exists" is a fact, not an opinion.
  * a **strategy** consumes what the leaves produced and judges it. This is the only
    place a threshold is allowed to appear.
  * a **conclusion** has no function here at all: the compiler generates none, and the
    runner passes it as soon as everything under it passes, which is what makes the
    conclusion a consequence of the argument rather than another thing to assert.

The names in produce=[] and consume=[] are not element ids. `shippable:model` hands its
contents on as `trained_model`, and `shippable:bar` asks for that name. They are kept
apart on purpose: an id names a place in the argument, a produced name names a value
travelling between two of them, and reusing one string for both hides which is meant.

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


###         ###
## shippable ##
###         ###

@jpipe_link("shippable:model")
@jpipe(produce=["trained_model"])
def the_trained_model_is_on_disk(produce: JpipeProduce) -> bool:
    """[evidence] The trained model is on disk."""
    artifact = MOCKS / MODEL_FILE
    if not artifact.is_file():
        return False
    produce("trained_model", artifact.read_text())
    return True


@jpipe_link("shippable:metrics")
@jpipe(produce=["measurements"])
def the_measurement_report_is_on_disk(produce: JpipeProduce) -> bool:
    """[evidence] The measurement report is on disk."""
    report = MOCKS / METRICS_FILE
    if not report.is_file():
        return False
    try:
        measurements = json.loads(report.read_text())
    except json.JSONDecodeError:
        return False
    produce("measurements", measurements)
    return True


@jpipe_link("shippable:bar")
@jpipe(consume=["trained_model", "measurements"])
def the_measured_accuracy_clears_the_80_bar(trained_model, measurements) -> bool:
    """[strategy] The measured accuracy clears the 80% bar."""
    return bool(trained_model.strip()) and measurements.get("accuracy", 0.0) >= ACCURACY_BAR

###                                ###
## Mocked element for demo purposes ##
###                                ###


MOCKS = Path(__file__).resolve().parent.parent / "mocks"

ACCURACY_BAR = float(os.environ.get("SHIPPABLE_BAR", "0.80"))
MODEL_FILE = os.environ.get("SHIPPABLE_MODEL", "model.txt")
METRICS_FILE = os.environ.get("SHIPPABLE_METRICS", "measurements.json")
