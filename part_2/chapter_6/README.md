# Chapter 6: Discussion

Twenty minutes, no exercises, nothing to install. The prompts below are starting points for talking
about what justification models do for the validation of high-level requirements, which is a question
none of the previous five chapters answers on its own.

There are more prompts here than the time allows. Three or four is a full session, and the room
chooses which. Each one names where in the tutorial it comes from, so the discussion has something
concrete to argue against, and each carries a second question for when it runs dry.

## Verification, or validation?

Chapter 4 confirmed that R13 holds: the artifacts exist and the measurement clears the bar. That is
verification. What in a justification model speaks to validation, to whether R1, "the classifier shall
be fair", was the right requirement in the first place?

*If it stalls:* if nothing in the model does, what would have to be added, and would the result still
be a justification model or a different artifact altogether?

## Where the interpretation lives

"Shall be fair" is not checkable. "The flip-rate is below 10%" is. In chapter 5's bricks, the strategy
node is where one becomes the other, and that step is a claim nobody verified.

Is that operationalisation a requirement of its own, a design decision, or an assumption?

*If it stalls:* who signs it off, and what does the argument look like when two stakeholders
operationalise the same high-level requirement differently?

## When is an argument enough?

`trustworthy` stops at "the splits are disjoint and every label is valid". Nothing in the notation
says that is sufficient, and the compiler is happy either way.

For a given high-level requirement, how would you decide that the argument underneath it is complete?

*If it stalls:* is sufficiency a property of the argument, of the domain, or of the regulator, and can
it be written down before the argument is built?

## The argument as a test of the requirement

Chapter 3 asked you to write an argument from a conclusion downwards, and the shape of the argument
came out of how the requirement was worded.

If nobody can write a justification for a requirement, is that a defect in the argument or in the
requirement?

*If it stalls:* would you use "somebody can sketch the argument" as an acceptance criterion in
requirements review, and what would it catch that a review checklist does not?

## Requirements change, arguments rot

A high-level requirement can be stable for years while the system under it changes weekly. Chapter 4
put the check next to the element it belongs to so that the argument fails when the world moves.

Which part of the model should absorb that change, and how do you notice when a still-green argument
has stopped being about the current system?

*If it stalls:* what is the equivalent of a stale test here, and would you rather find a red argument
or an out-of-date one?

## Ownership across an organisation

`assemble` let three teams argue their own claim without negotiating anything except the wording of
the artifacts they share.

Does that mirror how requirements are actually owned where you work?

*If it stalls:* which high-level requirement in your project has no owner who could write its
argument, and what does that absence tell you?

## The external reader

Model cards, audits and the AI Act all ask for something a third party can read and act on.

Is a justification model an engineering artifact, a communication artifact, or a compliance artifact,
and can one notation be all three?

*If it stalls:* what would you refuse to write into a model that a regulator will read, and what does
that refusal say about the requirement it belongs to?

## Closing round

Two minutes, going round the room, no discussion. Name one high-level requirement from your own work,
and say whether you could write its argument today, could not, or would rather not.

## Warming up

Chapter 3's [If you finish early](../../part_1/chapter_3/README.md#if-you-finish-early) asks what else
training this model carries and how each of those would be justified. Some participants will have
argued about it already, which makes it a way into the first prompt above rather than a cold start.
