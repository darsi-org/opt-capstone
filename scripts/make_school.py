"""A made-up school: 12 exams, 6 days x 2 slots, 5 rooms, 300 pupils. Seeded, so everyone gets the same data."""
import csv
import pathlib
import random

random.seed(2026)
pathlib.Path("data").mkdir(exist_ok=True)
SUBJECTS = ["Arabic", "English", "Maths", "Physics", "Chemistry", "Biology", "History", "Geography", "French", "German", "ICT", "Philosophy"]
HARD = {"Maths", "Physics", "Chemistry"}
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
    for p in range(1, 301):
        for s in ["Arabic", "English", "Maths"] + random.sample(SUBJECTS[3:], 3):
            w.writerow([f"P{p:03}", s])
print("data/exams.csv, data/rooms.csv, data/pupils.csv written")
