import os

with open("input.txt") as f:
    lines = f.readlines()

elf_total = {}
current_elve = 1

for line in [x.replace("\n", "") for x in lines]:
    if line == "":
        current_elve += 1
    else:
        cal_int = int(line)
        if current_elve in elf_total.keys():
            elf_total[current_elve] += cal_int
        else:
            elf_total[current_elve] = cal_int

print(f"Max calories: {max(elf_total.values())}")

totals = set(elf_total.values())

current_total = 0
num_to_count = 3

for x in range(1, num_to_count+1):
    current_max = max(totals)
    print(f"Current Max: {current_max}")
    current_total += current_max
    totals.remove(current_max)

print(f"Total of top {num_to_count}: {current_total}")
