import os

from Helpers import *

with open("input.txt") as f:
    lines = [x.replace("\n", "") for x in f.readlines()]

print(f"Length of input: {len(lines[0])}")
print(f"Length to first: {len_to_first(lines[0])}")
print(f"Length to first start of message: {len_to_som(lines[0])}")