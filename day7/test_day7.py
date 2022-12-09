import pytest

from Helpers import *

def test_input_or_output():
    assert input_or_output("$ cd /") == "input"
    assert input_or_output("$ ls") == "input"
    assert input_or_output("dir dscbfp") == "output"
    assert input_or_output("283653 fsdfddfv") == "output"

def test_parse_user_input():
    assert parse_user_input("$ cd /") == ("cd", "/")
    assert parse_user_input("$ ls") == ("ls", None)
    assert parse_user_input("$ cd ..") == ("cd", "..")

def test_parse_output():
    assert parse_output("dir dscbfp") == (("dir", "dscbfp"), None)
    assert parse_output("283653 fsdfddfv") == (("file", "fsdfddfv"), "283653")

def test_dir_structure():
    root = Dir("/")
    root.add_child("a")
    a = root.child("a")
    a.add_child("b")
    a.add_child("c")
    b = a.child("b")
    c = a.child("c")
    a.add_file("test.txt", 5)
    b.add_file("test2.txt", 10)
    c.add_file("test3.txt", 15)
    assert b.calc_dir_file_size() == 10
    assert b.calc_dir_total_size() == 10
    assert a.calc_dir_file_size() == 5
    assert a.calc_dir_total_size() == 30
    assert root.calc_dir_file_size() == 0
    assert root.calc_dir_total_size() == 30
    assert root.is_root()
    assert not a.is_root()
    assert b.dir_full_path() == "/a/b"
    assert root.walk_full_tree() == [('', 30), ('/a', 30), ('/a/b', 10), ('/a/c', 15)]