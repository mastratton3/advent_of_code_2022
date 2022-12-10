import os

from Helpers import *

with open("input.txt") as f:
    lines = [x.replace("\n", "") for x in f.readlines()]

a = CRDT()

for ins in lines:
    a.parse_instruction(ins)

signal_strengths = a.calc_signal_strength()
relevant_signal_strengths = signal_strengths[19] + signal_strengths[59] + signal_strengths[99] + signal_strengths[139] + signal_strengths[179] + signal_strengths[219]
print(f"Parsed {len(lines)} instructions")
print(a)
print(f"Signal Strength Vector: {signal_strengths}")
print(f"Result: {relevant_signal_strengths}")

row1 = a.cycle_history[:40]
row2 = a.cycle_history[40:80]
row3 = a.cycle_history[80:120]
row4 = a.cycle_history[120:160]
row5 = a.cycle_history[160:200]
row6 = a.cycle_history[200:240]

rows = [row1, row2, row3, row4, row5, row6]
rows_rendered = [render_row(x) for x in rows]
for row in rows_rendered:
    print(row)
