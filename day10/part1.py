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