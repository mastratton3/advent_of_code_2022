import os

with open("input.txt") as f:
    lines = f.readlines()


def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

lines = [x.replace("\n", "") for x in lines]

letter_to_score = {x: y for (x, y) in zip([x for x in char_range('a', 'z')], range(1,27))}
letter_to_score.update({x: y for (x, y) in zip([x for x in char_range('A', 'Z')], range(27,53))})

def common_in_three(l1, l2, l3):
    return set(l1).intersection(set(l2)).intersection(set(l3))

def score_items(s1):
    return [letter_to_score[x] for x in s1]

def score_and_sum_items(s1):
    return sum(score_items(s1))

def split_overlap_and_score(l):
    l1, l2 = split_list_in_half(l)
    return score_and_sum_items(find_overlapping_items(l1, l2))

chunks = [lines[x:x+3] for x in range(0, len(lines), 3)]
common_across = [common_in_three(x[0], x[1], x[2]) for x in chunks]
scores = [score_and_sum_items(x) for x in common_across]

sum(scores)