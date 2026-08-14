# Chapter 2: Worked examples

By the end of this chapter, you can:

- open the diagram preview of a `.jd` file, and read the source and the diagram against each other;
- edit a model with completion, renaming, formatting and quick fixes, rather than by hand;
- read the compiler's report inside the editor, and go from an element in it to its declaration.

## How to work

Every task below happens in [deployable.jd](deployable.jd), so open that file and leave it open. It
holds two justifications: `deployable`, and `deployable_v1`, the same argument in a rougher state.
Both compile, and `jpipe diagnostic -i deployable.jd` reports `(none)` before you start.

The tasks build on each other, and each one changes the file. When you are done, or whenever you want
to start over:

```sh
git checkout part_1/chapter_2/deployable.jd
```

You do not need to run the compiler yourself. The extension you installed in
[Setup](../../README.md#setup) calls it for you.

## 2.1: Open the preview

Open the preview from the icon in the editor title bar, or by right-clicking and choosing **jPipe**,
then *Open Diagram Preview*. The panel opens beside the file.

If it is blank and asks you to move the cursor into a diagram block, that is the rule it works by: the
preview shows the model your cursor is in. Click inside `deployable`, then inside `deployable_v1`, and
the diagram switches. One `.jd` file can hold several models, and the preview picks between them from
the cursor position rather than from a menu.

The preview draws the file as saved, not as typed. Change a label and a banner appears to say you are
looking at the last saved version. Save (`⌘S` / `Ctrl+S`) and the diagram is redrawn. While that
banner is up, moving the cursor into the other justification does not switch the diagram either, so
save before you navigate.

**Done when:** you have switched the preview between the two justifications using only the cursor, and
you have seen the unsaved-changes banner appear and go away.

## 2.2: Follow the argument with the cursor

In the preview toolbar, the eye icon (*Highlight on cursor*) is a toggle. Turn it on.

Put the cursor on `claim` in `deployable` and move down the declarations one line at a time. The
element named on the current line stays lit, the rest of the diagram dims, and if that node is off
screen the preview scrolls it into view. The `supports` lines behave the same way, so you can also
move down the relations and see which part of the diagram each one draws.

Then put the cursor on `model` in `deployable`, and on `model` in `deployable_v1`. The preview switches
models: these are two different elements that share a name.

**Done when:** you can move from the conclusion down to the evidence and see each element highlighted
in turn.

## 2.3: Let the editor finish the line

`deployable` has an `agreed` evidence that `deployable_v1` does not. Add one to `deployable_v1`, typing
as little of it as you can.

In the declarations, type `evi`, accept `evidence`, name it `agreed`, and write a label. Then, in the
relations below, type `agreed sup`, accept `supports`, and press `⌃Space` / `Ctrl+Space`.

The list you get holds the elements this model declares, each with its label beside it, and only the
ones that may legally appear in that position: `agreed` is evidence, evidence supports strategies, so
the list is `threshold` and `execution`. Take `threshold`, then save and check the new node in the
preview.

**Done when:** `deployable_v1` has an `agreed` evidence supporting `threshold`, and you have seen that
the completion list omits the elements that could not be there.

## 2.4: Rename, and then re-align

`deployable_v1` calls its dataset `training_ds`. Put the cursor on it, press `F2`, or right-click and
choose **Rename Symbol**, and type `test_ds`. The declaration and the `supports` line both change,
because an id is a reference rather than a piece of text.

Note what does not change. `deployable`, higher up the file, keeps its own `test_ds`, and each
justification's `model` remains its own element. Ids are scoped to the model that declares them, so a
find-and-replace across the file would rename elements that only happen to share a name.

The rename leaves the `is` column ragged. Run **Format Document**, from the right-click menu, from
`⇧⌥F` / `Shift+Alt+F`, or as *jPipe: Auto-indent and Align* in the command palette. The columns line
up again. That is where the layout of the files in this repository comes from, so you do not need to
space them by hand.
Formatting rewrites lines and never moves them past each other: comments stay beside what they
describe, and blank lines stay where you put them, which is how a body is divided into sub-arguments.

**Done when:** `deployable_v1` names `test_ds` in both places and its columns are aligned again.

## 2.5: Delete something, and let the editor put it back

In `deployable_v1`, delete the two `evidence` declarations under `execution`, and the two `supports`
lines that mention them.

The strategy `execution` is now unsupported, and the editor reports it: *Strategy 'execution' is not
supported by any evidence, sub-conclusion, or @support*. Put the cursor on the underlined id and open
the quick fixes, from the lightbulb that appears in the gutter or with `⌘.` / `Ctrl+.`. Two are
offered:

- *Add some evidence e supporting 'execution'*
- *Add a sub-conclusion sc supporting 'execution'*

Both are valid at that position, which is why the editor offers a choice instead of applying one. Take
the first. It writes the declaration and the `supports` line that ties it in, and leaves the label
empty, which it then reports as a warning in turn. Fill the label in: the quick fix restores the
structure of the argument, and the sentence is yours to write.

**Done when:** the error is gone and the new element has a label.

## 2.6: Read the file as the compiler sees it

The last icon in the preview toolbar, the notepad, switches the panel to the **diagnostic view**. It
is the last icon whatever the panel is showing, so it stays in the same place. It shows the output of
`jpipe diagnostic -i deployable.jd`, run for you, in four tabs, each carrying a count:

- **Problems**, what would stop the file compiling, and empty by now;
- **Models**, the two justifications with a census of what each is made of;
- **Symbols**, every element of every model, and where it is declared;
- **Actions**, the commands the compiler executed to build the two models.

Open **Symbols** and click a row: the editor jumps to the line that declares that element. Every row
that carries a location works this way, in Problems as much as in Symbols. Leave the tab open and move
around the source, and the row for the element you are on is marked as the current one.

The filter box narrows whichever tab you are in, and *Copy* puts the report on the clipboard. The same
notepad icon returns to the diagram.

**Done when:** you have gone from a symbol in the report to its declaration in the source in one
click, and Problems is empty.

## Put it back

```sh
git checkout part_1/chapter_2/deployable.jd
```
