import os

with open("input.txt") as f:
    lines = f.readlines()


lines = [x.replace("\n", "") for x in lines]

def parse_to_tuple(x):
    split_string = x.split(" ")
    return (split_string[0], split_string[1])

parsed_inputs = [parse_to_tuple(x) for x in lines]


results = {("A", "X"): "Draw",
            ("A", "Y"): "Win",
            ("A", "Z"): "Lose",
            ("B", "X"): "Lose",
            ("B", "Y"): "Draw",
            ("B", "Z"): "Win",
            ("C", "X"): "Win",
            ("C", "Y"): "Lose",
            ("C", "Z"): "Draw"}

selection_scores = {"X": 1,
                    "Y": 2,
                    "Z": 3}

result_scores = {"Win": 6,
                "Lose": 0,
                "Draw": 3}

def calculate_score(x):
    selection_score = selection_scores[x[1]]
    result = results[x]
    result_score = result_scores[result]
    return selection_score + result_score

all_scores = [calculate_score(x) for x in parsed_inputs]
total_score = sum(all_scores)

print(f"Total score: {total_score}")
