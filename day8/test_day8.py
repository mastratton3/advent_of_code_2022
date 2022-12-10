import pytest

from Helpers import *

def test_find_visible():
    assert find_visible([1,2,3,4,5]) == [True, True, True, True, True]
    assert find_visible([5,4,3,2,1]) == [True, False, False, False, False]
    assert find_visible([2,2,3,2,1]) == [True, False, True, False, False]

def test_consolidate_two_booleans():
    assert consolidate_two_booleans([True, True, True], [False, False, False]) == [True, True, True]
    assert consolidate_two_booleans([True, False, False], [False, True, True]) == [True, True, True]
    assert consolidate_two_booleans([True, False, False], [False, False, True]) == [True, False, True]

def test_reverse_list():
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]


def test_forest():
    a = Forest()
    a.add_row([1,2,3])
    a.add_row([4,5,6])
    a.add_row([7,8,9])
    assert a.calc_num_columns() == 3
    assert a.pull_column(0) == [1, 4, 7]


def test_forest_visibility():
    a = Forest()
    a.add_row([3,0,3,7,3])
    a.add_row([2,5,5,1,2])
    a.add_row([6,5,3,3,2])
    a.add_row([3,3,5,4,9])
    a.add_row([3,5,3,9,0])
    assert a.check_visibility(1,1)
    assert not a.check_visibility(2,2)
    assert a.visibility_count() == 21