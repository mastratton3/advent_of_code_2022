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

def split_list_in_half(l):
    l_break = int(len(l)/2)
    return (l[:l_break], l[l_break:])

t1 = "vJrwpWtwJgWrhcsFMMfFFhFp"
l1, l2 = split_list_in_half(t1)

def find_overlapping_items(l1, l2):
    return set(l1).intersection(set(l2))

def score_items(s1):
    return [letter_to_score[x] for x in s1]

def score_and_sum_items(s1):
    return sum(score_items(s1))

def split_overlap_and_score(l):
    l1, l2 = split_list_in_half(l)
    return score_and_sum_items(find_overlapping_items(l1, l2))

scores = [split_overlap_and_score(x) for x in lines]

print(f"Final Score: {sum(scores)}")