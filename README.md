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

1. Install Python 3.12: open PowerShell and run `winget install Python.Python.3.12`
2. Install Git: `winget install Git.Git`
3. Install VS Code from https://code.visualstudio.com (free)
4. On GitHub, open https://github.com/darsi-org/opt-capstone and press **Use this template** to make your own copy. Then clone your copy, not darsi-org's: `git clone https://github.com/<your-username>/opt-capstone.git`
5. Open a new PowerShell, go into the folder with `cd opt-capstone`, and run these lines one at a time:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   python check.py
   ```

   If PowerShell says running scripts is disabled on this system, you don't need to change any setting: use Command Prompt and run `.venv\Scripts\activate.bat` instead, or skip activating and start every command with `.venv\Scripts\python` (for example `.venv\Scripts\python -m pip install -r requirements.txt`, then `.venv\Scripts\python check.py`).

### Mac

1. Install Homebrew from https://brew.sh if you don't have it
2. Install Python and Git: `brew install python@3.12 git`
3. Install VS Code from https://code.visualstudio.com
4. On GitHub, open https://github.com/darsi-org/opt-capstone, press **Use this template**, then clone your copy: `git clone https://github.com/<your-username>/opt-capstone.git`
5. In Terminal, go into the folder with `cd opt-capstone` and run:

   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   python check.py
   ```

### Codespaces

No computer of your own? Use GitHub Codespaces, from a borrowed laptop too: open your copy → **Code** → **Codespaces** → **Create codespace**. Python and Git are already there. In its terminal, run:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python check.py
```

A phone browser is enough to read the results.

## Start

Press **Use this template** on https://github.com/darsi-org/opt-capstone, clone your copy, then follow milestone 1.

## Milestones

### m1: The problem and a validator (3 hours)

#### Why this matters
Before solving, decide how you will know a timetable is wrong. Never trust a solver alone.

#### Tools for this milestone
- **OR-Tools later** — CP-SAT solver. Get it: pip install -r requirements.txt
- **validate.py** — lists every broken hard rule. Get it: you write it

#### Do this
1. Set up your copy as in **Install once** (your copy, not darsi-org's). The made-up school is in data/: 12 exams, 6 days × 2 slots, 5 rooms, 140 pupils. `python scripts/make_school.py` rebuilds the same files.
2. Write PROBLEM.md: hard rules (no pupil clash, room size, each exam once) vs wishes (spread, no two hard exams a day).
3. Write validate.py and at least four tests in tests/test_validate.py (check.py counts them there): every file in tests/bad/ breaks exactly one hard rule and must fail with a message naming the exam, pupil or room; tests/good/ok.csv keeps every rule and must pass.
4. Run `pytest`, then `python check.py --milestone m1`.

#### You know you're done when
- PROBLEM.md exists
- ≥4 tests in tests/test_validate.py, all passing
- m1 passes

#### If something goes wrong
- **Validator passes a clashing timetable** → Join pupils to exams; two exams sharing a pupil cannot share a slot
- **Validator passes twice.csv** → "All 12 exams are there" isn't enough: count each exam, it must appear exactly once
- **Hard vs wish confused** → If breaking it makes the timetable impossible to sit (a pupil in two exams at once, more pupils than seats), it is a hard rule; if it only makes the timetable harder on pupils (two hard exams in one day), it is a wish

#### What you should understand
You can separate hard rules from wishes and catch every broken rule without the solver.

**Hand in:** PROBLEM.md, validate.py with tests, and darsi-check.json that passes m1.

### m2: A first CP-SAT model (4 hours)

#### Why this matters
Variables for exam×slot×room, hard rules as constraints, then validate the CSV the solver wrote.

#### Tools for this milestone
- **Google OR-Tools CP-SAT** — constraint programming solver. Get it: pip install ortools

#### Do this
1. In solve_cpsat.py create BoolVars for each exam, slot, room.
2. Add hard rules: each exam once, capacity, no pupil clash.
3. Solve with a 30s limit, write timetable.csv, run validate.py, save results/cpsat.json (status, seconds, broken_rules=0).
4. Run python check.py --milestone m2.

#### You know you're done when
- timetable.csv exists
- broken_rules is 0
- m2 passes

#### If something goes wrong
- **INFEASIBLE** → First check the data: is any exam bigger than the biggest room? Then look for a constraint that is too tight; print which hard rule you added last
- **Solver slow** → Keep 30s limit; FEASIBLE is OK if validator passes

#### What you should understand
You can model hard rules in CP-SAT and refuse any solution your validator rejects.

**Hand in:** solve_cpsat.py, timetable.csv, zero broken rules, and darsi-check.json that passes m2.

### m3: Wishes as an objective (4 hours)

#### Why this matters
Now make it kinder: minimise weighted penalties for crowded days and hard pairs.

#### Tools for this milestone
- **CP-SAT objective** — weights trade wishes. Get it: Minimize(sum of penalties)

#### Do this
1. Add penalties: two exams same day (weight 3), two hard same day (10), both slots same day (5).
2. Minimise total. Report each penalty before/after. Try two weight sets and explain.
3. Validate again. Save penalty in results/cpsat.json. Run python check.py --milestone m3.

#### You know you're done when
- results/cpsat.json has penalty
- m3 passes

#### If something goes wrong
- **Penalty unchanged** → Confirm the objective is set and you compare against a no-objective run
- **Weights feel arbitrary** → Ask a teacher which pain is worse; write their choice down

#### What you should understand
You can turn wishes into weights, minimise them, and explain the trade-off.

**Hand in:** Objective in the model, before/after table, weights note, and darsi-check.json that passes m3.

### m4: A second model with HiGHS (3 hours)

#### Why this matters
Two solvers agreeing — both passing the same validator — is strong evidence the model is right.

#### Tools for this milestone
- **HiGHS via highspy** — open-source MIP solver. Get it: pip install highspy

#### Do this
1. Write solve_highs.py as a MIP with the same data and 30s limit.
2. Validate with the same validate.py. Compare penalty, time, optimality in results/highs.json.
3. If they disagree, find the missing rule. Run python check.py --milestone m4.

#### Worked example: three exams with highspy
A MIP small enough to check by hand, written the way solve_highs.py will be. Three exams and one day with two slots. Maths shares pupils with Arabic and with Physics. One wish: hard exams in the morning, so an afternoon costs 3 for Maths or Physics and 1 for Arabic.

```python
import highspy

exams = ["Arabic", "Maths", "Physics"]
slots = [1, 2]  # one day: 1 = morning, 2 = afternoon
clashes = [("Arabic", "Maths"), ("Maths", "Physics")]  # these pairs share pupils
afternoon = {"Arabic": 1, "Maths": 3, "Physics": 3}  # the wish: hard exams in the morning

h = highspy.Highs()
h.setOptionValue("output_flag", False)  # quiet
h.setOptionValue("time_limit", 30.0)  # the same 30-second limit as CP-SAT
x = {(e, s): h.addBinary() for e in exams for s in slots}  # 1 = exam e sits in slot s

for e in exams:  # hard rule: each exam exactly once
    h.addConstr(sum(x[e, s] for s in slots) == 1)
for a, b in clashes:  # hard rule: no pupil in two exams at once
    for s in slots:
        h.addConstr(x[a, s] + x[b, s] <= 1)

h.minimize(sum(afternoon[e] * x[e, 2] for e in exams))  # the wishes: make the penalty small
print(h.modelStatusToString(h.getModelStatus()))  # Optimal, or why it stopped
for e in exams:
    print(e, "slot", next(s for s in slots if h.val(x[e, s]) > 0.5))
print("penalty", h.getInfo().objective_function_value)
```

It prints Optimal, Arabic and Physics in slot 1, Maths in slot 2, and penalty 3.0. Check it by hand: Maths can't share a slot with either of the others, so it sits alone. Maths in the afternoon costs 3; Arabic and Physics in the afternoon cost 1 + 3 = 4. In solve_highs.py the key grows to (exam, day, slot, room) and you add the room-size rule, as in your CP-SAT model. If the 30-second limit stops HiGHS first, the status says so instead of Optimal: write that in results/highs.json, and don't call the timetable optimal.

#### You know you're done when
- results/highs.json has penalty and broken_rules 0
- m4 passes

#### If something goes wrong
- **highspy install fails on Windows** → pip install highspy; if wheels fail use Codespaces
- **Different penalties both valid** → Neither proved OPTIMAL; try a longer limit and say so

#### What you should understand
You can cross-check a timetable with a second solver and the same validator.

**Hand in:** solve_highs.py, comparison table, and darsi-check.json that passes m4.

### m5: A Streamlit app and v1.0 (3 hours)

#### Why this matters
Give it to the people who make timetables — with validation before every download.

#### Tools for this milestone
- **Streamlit** — upload CSVs, sliders, download. Get it: pip install streamlit

#### Do this
1. Build app.py: upload exams/rooms/pupils, weight sliders, solve, download timetable.
2. Show validator result and penalties in plain Arabic and English. Add a what-if: close a room one day and show what changed.
3. CI runs validator tests. Tag v1.0. Run python check.py --milestone m5.

#### You know you're done when
- app.py uses streamlit
- m5 passes

#### If something goes wrong
- **Infeasible what-if crashes the app** → Catch INFEASIBLE and suggest relaxing a wish or adding a slot
- **Download without validation** → Block download until broken_rules == 0

#### What you should understand
You can wrap a solver in an app staff can use, with validation as the last safety check.

**Hand in:** app.py, green Actions, v1.0, darsi-check.json that passes m5, and your explanation.

## The check

Run `python check.py` or `python check.py --milestone m2`. It only reads files, writes `darsi-check.json`, and prints English and Arabic. It uploads nothing.

## Review on Darsi

Send your repository link and `darsi-check.json` with each milestone on Darsi. Darsi reads your latest Actions run and release from GitHub's public API, adds an advisory AI review, then your teacher or the Darsi team reviews it. **Darsi never runs your code.**

## Licence

MIT — see [LICENSE](LICENSE).
