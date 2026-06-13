import csv
import random
import os
import sys

NUM_ROWS = 52


COLUMNS = ["процент радужности единорога", "коэффицент сияния единорога", "процент уникальности единорога", "класс успешности еддинорога"]

def generate_row():

    return {
        "процент радужности единорога": random.randint(0, 100),
        "коэффицент сияния единорога": round(random.uniform(1.5, 9.9), 2),
        "процент уникальности единорога": random.randint(0, 100),
        "класс успешности еддинорога": random.choice(["A", "B", "C"]),
    }

OUTPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else "/data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "data.csv")

os.makedirs(OUTPUT_DIR, exist_ok=True)

rows = [generate_row() for _ in range(NUM_ROWS)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS)
    writer.writeheader()
    writer.writerows(rows)

