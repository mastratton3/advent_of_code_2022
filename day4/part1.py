import os

from Helpers import *

with open("input.txt") as f:
    lines = f.readlines()

lines = [x.replace("\n", "") for x in lines]

is_fully_contained = [check_fully_contained(parse_to_sets(x)) for x in lines]
one_if_fully_contained = [1 for x in is_fully_contained if x]

contains_intersection = [check_any_overlap(parse_to_sets(x)) for x in lines]
one_if_intersection = [1 for x in contains_intersection if x]

print(f"Total lines: {len(lines)}")
print(f"Total fully contained: {len(one_if_fully_contained)}")
print(f"Total with intersection: {len(one_if_intersection)}")