# Chapter 6: Discussion

## Proof, or evidence?

Nothing in this tutorial was proved. Chapter 4 ran the argument against the artifacts the system
actually has, and reported that R13 holds because a file was there and a measured number cleared an
agreed bar. That is validation: empirical evidence, gathered from the system as built, tied to the
claim it supports. Formal verification would ask instead for a proof, over a model of the system,
that the property holds for every execution.

For the requirements you work with, which could be formally verified at all, and which can only ever
be validated this way?

*Going deeper:* a learned classifier has no specification to prove against, only data it was fitted
to. Does that make formal verification inapplicable to the model itself, useful for the pipeline
around it, or neither? And if you did hold a proof about part of the system, where would it go in a
justification model, and what would it be evidence for?

## Where the interpretation lives

"Shall be fair" is not checkable. "The flip-rate is below 10%" is. In chapter 5's bricks, the strategy
node is where one becomes the other, and that step is the one thing in the model that nothing below
it establishes.

Is that operationalisation a requirement of its own, a design decision, or an assumption?

*Going deeper:* who signs it off, and what does the argument look like when two stakeholders
operationalise the same high-level requirement differently?

## When is an argument enough?

`trustworthy` stops at "the splits are disjoint and every label is valid". Nothing in the notation
says that is sufficient, and the compiler is happy either way.

For a given high-level requirement, how would you decide that the argument underneath it is complete?

*Going deeper:* is sufficiency a property of the argument, of the domain, or of the regulator, and can
it be written down before the argument is built?

## The argument as a test of the requirement

Chapter 3 asked you to write an argument from a conclusion downwards, and the shape of the argument
came out of how the requirement was worded.

If nobody can write a justification for a requirement, is that a defect in the argument or in the
requirement?

*Going deeper:* would you use "somebody can sketch the argument" as an acceptance criterion in
requirements review, and what would it catch that a review checklist does not?

## Requirements change, arguments rot

A high-level requirement can be stable for years while the system under it changes weekly. Chapter 4
put the check next to the element it belongs to so that the argument fails when the world moves.

Which part of the model should absorb that change, and how do you notice when a still-green argument
has stopped being about the current system?

*Going deeper:* what is the equivalent of a stale test here, and would you rather find a red argument
or an out-of-date one?

## Ownership across an organisation

`assemble` let three teams argue their own claim without negotiating anything except the wording of
the artifacts they share.

Does that mirror how requirements are actually owned where you work?

*Going deeper:* which high-level requirement in your project has no owner who could write its
argument, and what does that absence tell you?

## The external reader

Model cards, audits and the AI Act all ask for something a third party can read and act on.

Is a justification model an engineering artifact, a communication artifact, or a compliance artifact,
and can one notation be all three?

*Going deeper:* what would you refuse to write into a model that a regulator will read, and what does
that refusal say about the requirement it belongs to?


