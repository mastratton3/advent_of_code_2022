import os


def parse_to_range(s):
	split_string = [int(x) for x in s.split("-")]
	return set(range(split_string[0], split_string[1] + 1))

def parse_to_sets(s):
	split_string = s.split(",")
	return (parse_to_range(split_string[0]), parse_to_range(split_string[1]))

def check_fully_contained(sets):
	s1 = sets[0]
	s2 = sets[1]
	min_length = min([len(s1), len(s2)])
	intersection = s1.intersection(s2)
	return len(intersection) == min_length

def check_any_overlap(sets):
	s1 = sets[0]
	s2 = sets[1]
	intersection = s1.intersection(s2)
	return len(intersection) > 0