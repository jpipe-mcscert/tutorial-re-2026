# Justifying Software with jPipe: Tutorial (RE 2026)

## Authors

- **Sébastien Mosser**, Associate Professor, McMaster Centre for Software Certification
- **Kalvin Thuan-Phong Khuu**, PhD Student, McMaster Centre for Software Certification

## Overview

This repository holds the material for a hands-on [jPipe](https://www.jpipe.org) tutorial: how to
write a justification model, how to keep it honest as the system it describes evolves, and how to run
it against the artifacts it claims exist.

The tutorial runs in **two parts of three chapters each**, and a chapter ships whichever of these it
needs:

- **slides**, what is presented at that point in the tutorial;
- **examples**, the `.jd` models shown on those slides, in runnable form;
- **exercises**, what participants write themselves;
- **solutions**, one worked answer per exercise.

Chapters alternate rather than each carrying all four: chapter 2 is worked examples, chapter 3 is the
exercises that build on them. A chapter with exercises states them in its own `README.md`.

The running example throughout is the **emotion detection case study**
([jpipe-tutorial-2026](https://github.com/jpipe-mcscert/jpipe-tutorial-2026)): a classifier that is
accurate, fair, and gracefully failing to different degrees across three versions. Its deployability is
the claim the justification models argue about, which is why the examples talk about flip-rate,
accuracy, and test datasets.

## The tool suite

jPipe is three tools that hand work to each other:

![The jPipe tool suite. On your computer, a developer works in the jPipe IDE; the jPipe compiler turns
the model into a .json file, which the jPipe runner consumes. The same .json crosses to a CI/CD server,
where a second jPipe runner checks it against the code base that other developers also push
to](images/jpipe_toolsuite_final_v3.svg)

- the **jPipe IDE**, a VS Code extension, is where `.jd` models are written and previewed;
- the **jPipe compiler** turns a model into a diagram to show people, or into a `.json` description of
  the argument for other tools to consume;
- the **jPipe runner** takes that `.json` and confronts the argument with the artifacts it claims
  exist, so a model that has drifted away from the system fails instead of quietly lying.

Read the figure left to right. On your own machine the loop is short: write, render, check. The same
`.json` then crosses to the CI server, where the runner re-checks the argument against the code base
every time anyone pushes, which is what stops an assurance case from rotting the moment it is written.

## Setup

Install the three tools from the jPipe site, in this order. Each page covers Homebrew, APT and Scoop,
so pick the one line that matches your machine:

1. **[Install the Compiler](https://www.jpipe.org/tutorials/install/compiler/)**, one package-manager
   command, which brings Java and Graphviz along with it. Start here: the other two build on it.
2. **[Install the IDE](https://www.jpipe.org/tutorials/install/ide/)**, the VS Code extension, which
   picks up the compiler you just installed with no configuration.
3. For the **runner**, first needed in chapter 4 where models stop being only drawn and start being
   executed, this repository pins its own copy rather than relying on a system-wide install, so that
   everyone in the room is on the same version:

   ```sh
   pipenv sync --dev     # installs jpipe-runner exactly as pinned in Pipfile.lock
   ```

   That needs **Python 3.13** and [pipenv](https://pipenv.pypa.io/).

### Plan B: a Codespace

If the local install fights back on the day, open the repository in a GitHub Codespace, where the
compiler, Java, Graphviz, Python and the runner are all preinstalled:

**https://codespaces.new/jpipe-mcscert/tutorial-re-2026**

A real Codespace is required: pressing `.` for github.dev does not work, as the jPipe extension has no
web build.

## Working with the models

Check a model for errors:

```sh
jpipe diagnostic -i part_1/chapter_2/deployable.jd
```

Export one model from a file, as a diagram or as something executable:

```sh
jpipe process -f svg    -i part_1/chapter_2/deployable.jd -m deployable -o deployable.svg
jpipe process -f python -i part_1/chapter_2/deployable.jd -m deployable -o deployable.py
```

`-m` names the model to export, since one `.jd` file can hold several.

## License

MIT. See [LICENSE](./LICENSE).
