# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A personal PyCharm/IntelliJ Python project (`TintinPython`) used by a student (3rd standard) to practice Python fundamentals from class/homework. There is no application, package, or library being built — each file in `src/` is a standalone practice script.

## Structure

- `src/` is the IntelliJ source root (declared in `TintinPython.iml` / `.idea/TintinPy.iml`), and is also where this repo's git work happens day to day.
- Practice scripts are named by date and sequence: `YYYYMMDDNNN.py` (e.g. `20260619001.py` is the 1st script from 2026-06-19, `20260619002.py` the 2nd). New exercises should follow this same naming convention, using the actual current date.
- Each script is independent and self-contained — there's no shared module structure, no imports between scripts, and no package layout to preserve.
- Scripts commonly start with a comment naming the topic/section being practiced (e.g. `# Section A: TRUE FALSE Practice`, `# HW 1`) — keep this convention when adding new exercises.
- `.venv/` is a local virtualenv (not used for dependency management beyond the standard library — these scripts only use builtins).

## Running scripts

There is no build, lint, or test tooling in this project. Run any script directly:

```bash
python3 src/20260619001.py
```

Scripts frequently use `input()` for interactive prompts, so running them requires a terminal (or providing input via stdin/redirection) — they are not meant to run unattended.

## Working conventions

- Don't merge separate exercises into one file or refactor across files — each numbered script is a distinct, graded/reviewed homework or classwork submission and should stay self-contained.
- When adding a new exercise, create a new `YYYYMMDDNNN.py` file rather than appending to an existing one, unless explicitly asked to extend that day's file.
- Keep code at a beginner level consistent with the existing style (plain `print`/`input`, basic `if`/`elif`/`else`, `for`/`while` loops, simple functions) — avoid introducing advanced idioms, type hints, or external libraries unless asked.
