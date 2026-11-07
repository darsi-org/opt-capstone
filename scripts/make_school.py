"""A made-up school: 12 exams, 6 days x 2 slots, 5 rooms, 140 pupils. Seeded, so everyone gets the same data.

Every pupil sits Arabic, English and Maths, one language (French or German) and two more subjects.
The biggest exam (140 pupils) fits the Hall (150 seats), so a timetable that keeps every rule exists.
French and German share no pupil, so those two may sit in the same slot, in two rooms that are big enough.
"""
import csv
import pathlib
import random

random.seed(2026)
pathlib.Path("data").mkdir(exist_ok=True)
SUBJECTS = ["Arabic", "English", "Maths", "French", "German", "Physics", "Chemistry", "Biology", "History", "Geography", "ICT", "Philosophy"]
HARD = {"Maths", "Physics", "Chemistry"}
CHOICES = SUBJECTS[5:]  # each pupil picks two of these seven
with open("data/exams.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["exam", "hard"])
    for s in SUBJECTS:
        w.writerow([s, int(s in HARD)])
with open("data/rooms.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["room", "seats"])
    for r, n in [("Hall", 150), ("R1", 40), ("R2", 40), ("R3", 30), ("Lab", 25)]:
        w.writerow([r, n])
with open("data/pupils.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["pupil", "exam"])
    for p in range(1, 141):
        language = "German" if p % 4 == 0 else "French"  # 35 take German, 105 French
        for s in ["Arabic", "English", "Maths", language] + random.sample(CHOICES, 2):
            w.writerow([f"P{p:03}", s])
print("data/exams.csv, data/rooms.csv, data/pupils.csv written")
