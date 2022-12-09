import os

from Helpers import *

with open("input.txt") as f:
    lines = [x.replace("\n", "") for x in f.readlines()]


current_directory = Dir("/")

for line in lines[1:]:
    in_or_out = input_or_output(line)
    if in_or_out == "input":
        ins = parse_user_input(line)
        if ins == ("cd", ".."):
            current_directory = current_directory.parent
        elif ins[0] == "cd":
            current_directory = current_directory.child(ins[1])
    elif in_or_out == "output":
        out = parse_output(line)
        if out[0][0] == "dir":
            current_directory.add_child(out[0][1])
        elif out[0][0] == "file":
            current_directory.add_file(out[0][1], out[1])
    else:
        raise Exception("Found line that wasn't input or output.")

root = current_directory.goto_root()

a = root.walk_full_tree()
less_than_100k = sum([v for (k,v) in a if v < 100000])
ttl = sum([v for (k, v) in a])

total_space_avail = 70000000
total_space_required = 30000000

currently_used_space = root.calc_dir_total_size()
currently_free = total_space_avail - currently_used_space
required = total_space_required - currently_free

min([v for (k,v) in a if v > required])