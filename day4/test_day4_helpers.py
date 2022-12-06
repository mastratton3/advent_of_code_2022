import pytest

from Helpers import *

def test_parse_to_range():
	assert parse_to_range("1-5") == set(range(1,6))

def test_parse_to_sets():
	assert parse_to_sets("2-4,6-8") == (set([2,3,4]), set([6,7,8]))

def test_fully_contained():
	assert check_fully_contained((set([2,3,4]), set([3,4])))
	assert not check_fully_contained((set([2,3,4]), set([5,6,7])))
	assert not check_fully_contained((set([2,3,4]), set([3,4,5])))

def test_any_overlap():
	assert check_any_overlap((set([2,3,4]), set([4,5,6])))
	assert not check_any_overlap((set([2,3,4]), set([5,6,7])))