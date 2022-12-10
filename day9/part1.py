import os

from Helpers import *

with open("input.txt") as f:
    lines = [x.replace("\n", "") for x in f.readlines()]

gb = GameBoard()

for line in lines:
    parsed_line = line.split(" ")
    gb.move_h(parsed_line[0], int(parsed_line[1]))

print(gb)
print(f"Num positions tail visited: {len(gb.tail_visits)}")

