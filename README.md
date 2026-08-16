# Validating Requirements of Machine Learning Pipelines with Justification Models (IEEE RE 2026)

## Authors

- **Sébastien Mosser**, Associate Professor, McMaster Centre for Software Certification
- **Kalvin Thuan-Phong Khuu**, PhD Student, McMaster Centre for Software Certification

## Overview

This repository holds the material for a hands-on [jPipe](https://www.jpipe.org) tutorial: how to
write a justification model, how to keep it honest as the system it describes evolves, and how to run
it against the artifacts it claims exist.

The tutorial runs in **two parts of three chapters each**, and a chapter ships whichever of these it
needs:

- **examples**, the `.jd` models shown in the slides, in runnable form;
- **exercises**, what participants write themselves;
- **solutions**, one worked answer per exercise.

The running example throughout is the **emotion detection case study**
([jpipe-tutorial-2026](https://github.com/jpipe-mcscert/jpipe-tutorial-2026)): a classifier that is
accurate, fair, and gracefully failing to different degrees across three versions. Its deployability is
the claim the justification models argue about, which is why the examples talk about flip-rate,
accuracy, and test datasets.

## Slides

What is presented on the day, one deck per part:

- **[Part 1](slides/jPipe_RE_I.pdf)**, chapters 1 to 3: the decision a justification records, the
  language it is written in, and writing models yourself.
- **[Part 2](slides/jPipe_RE_II.pdf)**, chapters 4 to 6: running a model against the artifacts it
  names, composing models across files and owners, and the closing discussion.

## The tool suite

jPipe is three tools that hand work to each other:

![The jPipe tool suite. On your computer, a developer works in the jPipe IDE; the jPipe compiler turns
the model into a .json file, which the jPipe runner consumes. The same .json crosses to a CI/CD server,
where a second jPipe runner checks it against the code base that other developers also push
to](images/jpipe_toolsuite_final.svg)

- the **jPipe IDE**, a VS Code extension, is where `.jd` models are written and previewed;
- the **jPipe compiler** turns a model into a diagram to show people, or into a `.json` description of
  the argument for other tools to consume;
- the **jPipe runner** takes that `.json` and confronts the argument with the artifacts it claims
  exist, so a model that has drifted away from the system fails instead of quietly lying.

Read the figure left to right. On your own machine the loop is short: write, render, check. The same
`.json` then crosses to the CI server, where the runner re-checks the argument against the code base
every time anyone pushes, which is what stops an assurance case from rotting the moment it is written.

## Setup

The quickest way in is a Codespace, where the compiler, Java, Graphviz, Python and the runner are all
preinstalled and the repository is already cloned:

**https://codespaces.new/jpipe-mcscert/tutorial-re-2026**

A real Codespace is required: pressing `.` for github.dev does not work, as the jPipe extension has no
web build.

### Plan B: install the tools yourself

Clone this repository, then install the three tools from the jPipe site, in this order. Each install
page covers Homebrew, APT and Scoop, so pick the one line that matches your machine:

1. Clone this repository, and work from inside it:

   ```sh
   $ git clone https://github.com/jpipe-mcscert/tutorial-re-2026.git
   $ cd tutorial-re-2026
   tutorial-re-2026 $
   ```

2. **[Install the Compiler](https://www.jpipe.org/tutorials/install/compiler/)**, one package-manager
   command, which brings Java and Graphviz along with it. Start here: the other two build on it.
3. **[Install the IDE](https://www.jpipe.org/tutorials/install/ide/)**, the VS Code extension, which
   picks up the compiler you just installed with no configuration.
4. For the **runner**, first needed in chapter 4 where models stop being only drawn and start being
   executed, this repository pins its own copy rather than relying on a system-wide install, so that
   everyone in the room is on the same version:

   ```sh
   tutorial-re-2026 $ pipenv sync --dev   # installs jpipe-runner exactly as pinned in Pipfile.lock
   ```

   That needs **Python 3.13 or newer** and [pipenv](https://pipenv.pypa.io/). Anything from 3.13 up
   works, so if your machine is already on a later version there is nothing to downgrade.

## Working with the models

Check a model for errors:

```sh
tutorial-re-2026 $ jpipe diagnostic -i part_1/chapter_2/deployable.jd
```

Export one model from a file, as a diagram or as something executable:

```sh
tutorial-re-2026 $ jpipe process -f svg    -i part_1/chapter_2/deployable.jd -m deployable -o deployable.svg
tutorial-re-2026 $ jpipe process -f python -i part_1/chapter_2/deployable.jd -m deployable -o deployable.py
```

`-m` names the model to export, since one `.jd` file can hold several.

## References

The tools, the people, and the work this tutorial is built on.

- **[jPipe](https://www.jpipe.org)**, the language, the compiler, the IDE and the runner.
- **[McMaster Centre for Software Certification (McSCert)](https://www.eng.mcmaster.ca/mcscert/)**,
  where jPipe is developed.
- **[Sébastien Mosser](https://mosser.github.io/)** and
  **[Kalvin Thuan-Phong Khuu](https://kalvinkhuu.github.io/)**, the authors of this tutorial.

Publications behind the material:

- S. Mosser, S. Ravichandran, K. T.-P. Khuu, B. Detlor, D. Y. Geiskkovitch, A.-M. Pinna-Déry and
  P. J. White. *Capturing and Organizing Reusable Interaction Practices Using Justification and
  Feature Models*. Journal of Object Technology, 25(3):183-196, 2026.
  [10.5381/jot.2026.25.3.a14](https://www.jot.fm/contents/issue_2026_03/a14.html)
- K. T.-P. Khuu, N. Lacroix, M. Blay-Fornarino and S. Mosser. *Safety First! Modelling Requirements
  from GPT-5 System Card using Lightweight Safety Models*. MoDRE 2026, the 16th Model-Driven
  Requirements Engineering Workshop, co-located with IEEE RE 2026.
  [hal-05681913](https://hal.science/hal-05681913)
- K. T.-P. Khuu, N. Lacroix, B. Lacroix, R. Paige, M. Blay-Fornarino and S. Mosser. *Model Cards for
  Responsible AI: Stop Carding, Start Modelling*. ICSE-SEET 2026, the IEEE/ACM 48th International
  Conference on Software Engineering.
  [hal-05679580](https://hal.science/hal-05679580v1)

## License

MIT. See [LICENSE](./LICENSE).
