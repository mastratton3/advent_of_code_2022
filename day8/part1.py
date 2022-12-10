import os

from Helpers import *

with open("input.txt") as f:
    lines = [x.replace("\n", "") for x in f.readlines()]

forest = Forest()
for line in lines:
    row = [int(x) for x in line]
    forest.add_row(row)

num_visible = forest.visibility_count()

print(f"Num Rows: {len(lines)}")
print(f"Num Cols: {forest.calc_num_columns()}")
print(f"Num Trees: {len(lines) * forest.calc_num_columns()}")
print(f"Num Trees Visible: {num_visible}")

# A couple ways to approach the problem.
# One way to attack is to write a function that goes over rows from right and left, returns T/F if visible. Just needs to track previously seen max
# Needs to do for each direction. 