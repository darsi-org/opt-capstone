# Capstone: an exam timetable that really works


> **Darsi briefs are short on purpose.** The in-app lesson shows tight numbered clicks. This README keeps the full commands, error fixes, and background for each milestone — open the matching **Milestone N** section when you need detail.

Build an exam timetable for a made-up school: independent validator first, OR-Tools CP-SAT model, kinder timetable via weighted wishes, a second model with HiGHS, and a Streamlit app staff can use with a what-if.

[العربية](README.ar.md)

## What you will be able to do

- Run real free tools from a laptop or Codespaces
- Finish five milestones, each with checks you can self-verify
- Leave with a portfolio piece: a report, demo or tool tagged v1.0
- **Darsi never runs your code** — it reads your link and check file, then an advisory review

## Install once

### Windows

1. Install Python 3.12: open PowerShell and run winget install Python.Python.3.12
2. Install Git: winget install Git.Git
3. Install VS Code from https://code.visualstudio.com (free)
4. On GitHub, open https://github.com/darsi-org/opt-capstone and press Use this template, then Clone your copy
5. In the project folder run:
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   python check.py

### Mac

1. Install Homebrew from https://brew.sh if you don't have it
2. brew install python@3.12 git
3. Install VS Code from https://code.visualstudio.com
4. On GitHub open https://github.com/darsi-org/opt-capstone → Use this template → clone your copy
5. In the project folder run:
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   python check.py

### Codespaces / Colab

No computer of your own? Use GitHub Codespaces: open your copy → Code → Codespaces → Create codespace. Everything installs there. Or open a notebook in Google Colab, run the first cell that clones your repo, then run python check.py. Both work from a borrowed laptop; a phone browser is enough to read results.

## Start

Press **Use this template** on https://github.com/darsi-org/opt-capstone, clone your copy, then follow milestone 1.

## Milestones

### m1: The problem and a validator (3 hours)

## Why this matters
Before solving, decide how you will know a timetable is wrong. Never trust a solver alone.

## Tools for this milestone
- **OR-Tools later** — CP-SAT solver. Get it: pip install -r requirements.txt
- **validate.py** — lists every broken hard rule. Get it: you write it

## Do this
1. Clone https://github.com/darsi-org/opt-capstone. Run: python scripts/make_school.py
2. Write PROBLEM.md: hard rules (no pupil clash, room size, each exam once) vs wishes (spread, no two hard exams a day).
3. Write validate.py; test it on every file in tests/bad/. Run python check.py --milestone m1.

## You know you're done when
- PROBLEM.md exists
- ≥4 validator tests
- m1 passes

## If something goes wrong
- **Validator passes a clashing timetable** → Join pupils to exams; two exams sharing a pupil cannot share a slot
- **Hard vs wish confused** → If breaking it makes the timetable impossible, it was a wish

## What you should understand
You can separate hard rules from wishes and catch every broken rule without the solver.

**Hand in:** PROBLEM.md, validate.py with tests, and darsi-check.json that passes m1.

### m2: A first CP-SAT model (4 hours)

## Why this matters
Variables for exam×slot×room, hard rules as constraints, then validate the CSV the solver wrote.

## Tools for this milestone
- **Google OR-Tools CP-SAT** — constraint programming solver. Get it: pip install ortools

## Do this
1. In solve_cpsat.py create BoolVars for each exam, slot, room.
2. Add hard rules: each exam once, capacity, no pupil clash.
3. Solve with a 30s limit, write timetable.csv, run validate.py, save results/cpsat.json (status, seconds, broken_rules=0).
4. Run python check.py --milestone m2.

## You know you're done when
- timetable.csv exists
- broken_rules is 0
- m2 passes

## If something goes wrong
- **INFEASIBLE** → Check a constraint that is too tight; print which hard rule you added last
- **Solver slow** → Keep 30s limit; FEASIBLE is OK if validator passes

## What you should understand
You can model hard rules in CP-SAT and refuse any solution your validator rejects.

**Hand in:** solve_cpsat.py, timetable.csv, zero broken rules, and darsi-check.json that passes m2.

### m3: Wishes as an objective (4 hours)

## Why this matters
Now make it kinder: minimise weighted penalties for crowded days and hard pairs.

## Tools for this milestone
- **CP-SAT objective** — weights trade wishes. Get it: Minimize(sum of penalties)

## Do this
1. Add penalties: two exams same day (weight 3), two hard same day (10), both slots same day (5).
2. Minimise total. Report each penalty before/after. Try two weight sets and explain.
3. Validate again. Save penalty in results/cpsat.json. Run python check.py --milestone m3.

## You know you're done when
- results/cpsat.json has penalty
- m3 passes

## If something goes wrong
- **Penalty unchanged** → Confirm the objective is set and you compare against a no-objective run
- **Weights feel arbitrary** → Ask a teacher which pain is worse; write their choice down

## What you should understand
You can turn wishes into weights, minimise them, and explain the trade-off.

**Hand in:** Objective in the model, before/after table, weights note, and darsi-check.json that passes m3.

### m4: A second model with HiGHS (3 hours)

## Why this matters
Two solvers agreeing — both passing the same validator — is strong evidence the model is right.

## Tools for this milestone
- **HiGHS via highspy** — open-source MIP solver. Get it: pip install highspy

## Do this
1. Write solve_highs.py as a MIP with the same data and 30s limit.
2. Validate with the same validate.py. Compare penalty, time, optimality in results/highs.json.
3. If they disagree, find the missing rule. Run python check.py --milestone m4.

## You know you're done when
- results/highs.json has penalty and broken_rules 0
- m4 passes

## If something goes wrong
- **highspy install fails on Windows** → pip install highspy; if wheels fail use Codespaces
- **Different penalties both valid** → Neither proved OPTIMAL; try a longer limit and say so

## What you should understand
You can cross-check a timetable with a second solver and the same validator.

**Hand in:** solve_highs.py, comparison table, and darsi-check.json that passes m4.

### m5: A Streamlit app and v1.0 (3 hours)

## Why this matters
Give it to the people who make timetables — with validation before every download.

## Tools for this milestone
- **Streamlit** — upload CSVs, sliders, download. Get it: pip install streamlit

## Do this
1. Build app.py: upload exams/rooms/pupils, weight sliders, solve, download timetable.
2. Show validator result and penalties in plain Arabic and English. Add a what-if: close a room one day and show what changed.
3. CI runs validator tests. Tag v1.0. Run python check.py --milestone m5.

## You know you're done when
- app.py uses streamlit
- m5 passes

## If something goes wrong
- **Infeasible what-if crashes the app** → Catch INFEASIBLE and suggest relaxing a wish or adding a slot
- **Download without validation** → Block download until broken_rules == 0

## What you should understand
You can wrap a solver in an app staff can use, with validation as the last safety check.

**Hand in:** app.py, green Actions, v1.0, darsi-check.json that passes m5, and your explanation.

## The check

Run `python check.py` or `python check.py --milestone m2`. It only reads files, writes `darsi-check.json`, and prints English and Arabic. It uploads nothing.

## Review on Darsi

Send your repository link and `darsi-check.json` with each milestone on Darsi. Darsi reads your latest Actions run and release from GitHub's public API, adds an advisory AI review, then your teacher or the Darsi team reviews it. **Darsi never runs your code.**

## Licence

MIT — see [LICENSE](LICENSE).
