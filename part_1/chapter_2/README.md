# Chapter 2: Worked examples

The models shown on the slides, in runnable form. Nothing here is an exercise: open them, preview
them, and change them to see what the editor says. Chapter 3 is where you write your own.

| File | What it shows |
|---|---|
| [deployable.jd](deployable.jd) | one justification written whole, with the two commands that compile it in its header |
| [assemble.jd](assemble.jd) | two independent justifications, gathered by `assemble` |
| [template.jd](template.jd) | a template, a justification that implements it, and a second, partial one |

[deployable.json](deployable.json) and [deployable.py](deployable.py) are what those two commands
produce, checked in so you can see the compiler's output before running anything yourself. Chapter 4
is where the Python side stops being a listing and starts being work.

## Let the editor do the mechanical work

The jPipe IDE knows the language, so the bookkeeping that makes a `.jd` file tedious is not yours to
do by hand. Everything below is in the extension you installed in [Setup](../../README.md#setup), and
none of it needs the compiler to be running. Try each one in these files: they are worked examples, so
nothing is lost if you mangle one, and `git checkout` brings it back.

**Rename a symbol, with `F2`.** Element and model names are references, not text, and the editor
rewrites all of them. Put the cursor on `can_deploy` in [template.jd](template.jd) and rename it: the
template's declaration, the two `implements` clauses and every qualified hook that names it, nine
places in one keystroke. Renaming an element does the same to the `supports` lines that mention it.
Never rename with find-and-replace: `model` is a different element in each model that declares one,
and the editor knows that where a search does not.

**Fix what the editor flags, with the lightbulb (`⌘.` / `Ctrl+.`).** Where a problem can be repaired,
the fix is offered rather than described. Delete the `sub-conclusion can_deploy:fair` line from
`deployable` in [template.jd](template.jd) and the editor will report the `@support` that is now
unanswered and offer to write the declaration back. Mistype `assemble` in [assemble.jd](assemble.jd)
and it offers the spelling. The same applies to a conclusion nothing supports yet, a mistyped config
key, and a `load` path that does not resolve.

**Reach for the refactorings, with `⌃⇧R` / `Ctrl+Shift+R`,** or from **Refactor…** in the right-click
menu, or by name in the command palette:

- **Sort Elements** puts a model's declarations in the order its argument reads, conclusion first,
  then down through what supports it, one branch at a time. The examples here are already in that
  order, which is what it produces: you never have to maintain that shape by hand.
- **Extract Template** turns a justification into a template plus a justification that implements it.
  That is exactly the shape [template.jd](template.jd) shows, so you can produce it from a model you
  wrote whole rather than planning for it up front.
- **Convert Justification to Template** switches what a model is, and says up front how many
  `@support` elements the conversion would drop.

**Tidy the file, from Source Action…** in the right-click menu, or by name in the palette:
**jPipe: Auto-indent and Align** is where the aligned `is` columns in these files come from, so do not
space them by hand. **jPipe: Organize Loads** sorts and de-duplicates the `load` statements at the top
of a file, which matters from chapter 5 on, where models are split across files. Both run only when
you ask: reordering your own source is a decision, not something that should happen while you save.

The point is not that these save keystrokes. A model whose names, order and layout are maintained by
the editor is one you can keep changing as the system it argues about changes, which is the whole
claim of this tutorial.
