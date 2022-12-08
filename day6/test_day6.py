import pytest

from Helpers import *

def test_four_chars_dif():
    assert four_chars_are_diff("abcd")
    assert not four_chars_are_diff("aacd")
    assert not four_chars_are_diff("abcc")

def test_slice_iterate():
    assert [x for x in slice_iterate([1,2,3,4,5,6], 3)] == [[1,2,3], [2,3,4], [3, 4, 5], [4, 5, 6]]

def test_slice_and_check_diff():
    assert slice_and_check_diff("aabcd") == [False, True]

def test_case1():
    assert len_to_first("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert len_to_first("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert len_to_first("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert len_to_first("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11

def test_som():
    assert len_to_som("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert len_to_som("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert len_to_som("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert len_to_som("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert len_to_som("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26