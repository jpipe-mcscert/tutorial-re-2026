# This file is what `jpipe process -f python -i shippable.jd -m shippable` produced,
# with the TODOs added. Regenerate it yourself in 4.1 if you want to see that for
# yourself; the only thing added by hand is the MOCKS path below, so that you spend the
# chapter on the argument rather than on relative paths.
#
# Every function is linked to one element of the model by @jpipe_link("shippable:<id>").
# The runner walks the model bottom-up and calls them in that order.
#
# Use only the standard library: `json` and `pathlib` are all you need, and this chapter
# adds no dependency.
#
# Run it with:   pipenv run jpipe-runner -l exercises/bindings.py shippable.json

from pathlib import Path
from typing import Any, Callable

from jpipe_runner.framework.decorators.jpipe_decorator import jpipe
from jpipe_runner.framework.decorators.link_decorator import jpipe_link

JpipeProduce = Callable[[str, Any], None]

# Resolved from this file, not from the working directory, so the run behaves the same
# wherever you launch it from.
MOCKS = Path(__file__).resolve().parent.parent / "mocks"


# The conclusion. Left exactly as generated, and left alone: the runner never calls this
# function. A conclusion passes when everything under it passes, which is the whole point
# of writing the argument down. Nothing for you to do here.

@jpipe_link("shippable:claim")
@jpipe(consume=[])
def the_classifier_is_fit_to_ship() -> bool:
    """[conclusion] The classifier is fit to ship"""
    pass


@jpipe_link("shippable:bar")
@jpipe(produce=[], consume=[])
def the_measured_accuracy_clears_the_80_bar(produce: JpipeProduce) -> bool:
    """[strategy] The measured accuracy clears the 80% bar"""
    # TODO (4.3) the only place in this file where a judgement belongs.
    #
    #   1. declare what it needs:  @jpipe(consume=["model", "metrics"])
    #   2. take those names as parameters, in that order, and drop the `produce`
    #      parameter: this function produces nothing.
    #   3. return whether the accuracy in `metrics` clears 0.80.
    #
    # Every name you list in consume=[] must actually be used in the body. The decorator
    # checks, and says so if you forget.
    pass


@jpipe_link("shippable:model")
@jpipe(produce=[])
def the_trained_model_is_on_disk(produce: JpipeProduce) -> bool:
    """[evidence] The trained model is on disk"""
    # TODO (4.2) report whether MOCKS / "model.txt" is there, and hand its contents on.
    #
    #   1. declare what it offers:  @jpipe(produce=["model"])
    #   2. call produce("model", <the file's text>) when it exists
    #   3. return True if it exists, False if it does not
    #
    # Return False rather than raising when the file is missing. "It is not there" is a
    # verdict this argument is allowed to reach, and the runner knows what to do with it.
    pass


@jpipe_link("shippable:metrics")
@jpipe(produce=[])
def the_measurement_report_is_on_disk(produce: JpipeProduce) -> bool:
    """[evidence] The measurement report is on disk"""
    # TODO (4.2) the same shape as above, for MOCKS / "measurements.json", produced under
    # the name "metrics". Parse it with json.loads so the strategy receives a dict rather
    # than a string.
    #
    # A file that exists but does not parse is not a measurement report. Decide what this
    # function should return in that case, and say so in the code.
    pass
