import os

with open("input.txt") as f:
    lines = f.readlines()


lines = [x.replace("\n", "") for x in lines]

def parse_to_tuple(x):
    split_string = x.split(" ")
    return (split_string[0], split_string[1])

parsed_inputs = [parse_to_tuple(x) for x in lines]

to_pick_opts = {("A", "X"): "C",
            ("A", "Y"): "A",
            ("A", "Z"): "B",
            ("B", "X"): "A",
            ("B", "Y"): "B",
            ("B", "Z"): "C",
            ("C", "X"): "B",
            ("C", "Y"): "C",
            ("C", "Z"): "A"}

selection_scores = {"A": 1,
                    "B": 2,
                    "C": 3}

result_scores = {"Z": 6,
                "X": 0,
                "Y": 3}

def calculate_score(x):
    to_pick = to_pick_opts[x]
    selection_score = selection_scores[to_pick]
    result_score = result_scores[x[1]]
    return selection_score + result_score

all_scores = [calculate_score(x) for x in parsed_inputs]
total_score = sum(all_scores)

print(f"Total score: {total_score}")
