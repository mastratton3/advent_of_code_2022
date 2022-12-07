import queue
import os
import re

with open("input.txt") as f:
    lines = [x.replace("\n", "") for x in f.readlines()]

stacks = re.sub(" +", " ", lines[8]).strip().split(" ")
stack_index_locations = {x: lines[8].index(x) for x in stacks}
stack_queues = {x: queue.LifoQueue() for x in stack_index_locations}

# Begin process to create stacks
for line_num in [x for x in range(7, -1, -1)]:
    line = lines[line_num]
    for stack_num, idx in stack_index_locations.items():
        value_present = line[idx]
        if value_present != " ":
            stack_queues[stack_num].put(value_present)

p2_queues = stack_queues.copy()

def parse_instruction(s):
    split_string = s.split(" ")
    return (int(split_string[1]), split_string[3], split_string[5])

for instruction in lines[10:]:
    parsed_instruction = parse_instruction(instruction)
    for move_num in range(1, parsed_instruction[0] + 1):
        removed_item = stack_queues[parsed_instruction[1]].get()
        stack_queues[parsed_instruction[2]].put(removed_item)

result = [stack_queues[str(x)].get() for x in range(1,10)]

for instruction in lines[10:]:
    parsed_instruction = parse_instruction(instruction)
    print(f"Running {instruction}")
    temp_queue = []
    for move_num in range(1, parsed_instruction[0] + 1):
        print(f"Move Num: {move_num}")
        removed_item = p2_queues[parsed_instruction[1]].get()
        print(f"Moving item: {removed_item}")
        temp_queue.append(removed_item)
    print("Moving to While Loop")
    while len(temp_queue) > 0:
        p2_queues[parsed_instruction[2]].put(temp_queue.pop())

result2 = [p2_queues[str(x)].get() for x in range(1,10)]

# Notes:
#   Input in format of "Move {num_to_move} from {column_num} to {column_num}"
#   Boxes get pulled top first