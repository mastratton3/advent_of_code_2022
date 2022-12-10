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

gb2 = GameBoard(9)
for line in lines:
    parsed_line = line.split(" ")
    gb2.move_h(parsed_line[0], int(parsed_line[1]))

print(gb2)
print(f"Num Positions Tail Visited(10): {len(gb2.tail_visits)}")