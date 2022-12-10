import pytest

from Helpers import *

def test_pos_adjacent():
    a = Pos(1, 1)
    b = Pos(1, 1)
    c = Pos(1, 2)
    d = Pos(1, 3)
    e = Pos(3, 1)
    f = Pos(2, 3)
    g = Pos(2, 2)
    assert a.are_adjacent(b)
    assert a.are_adjacent(c)
    assert a.are_adjacent(g)
    assert not a.are_adjacent(d)
    assert not a.are_adjacent(e)
    assert not a.are_adjacent(f)

def test_add():
    a = Pos(1,1)
    assert a + (1,0) == Pos(2,1)

def test_sub():
    a = Pos(1,1)
    b = Pos(1,1)
    assert a - b == Pos(0,0)
    assert a - (0, 0) == a

def test_determine_move():
    assert determine_move(Pos(0,0)) == Pos(0,0)
    assert determine_move(Pos(1,0)) == Pos(0,0)
    assert determine_move(Pos(2,0)) == Pos(1,0)
    assert determine_move(Pos(2,2)) == Pos(1,1)
    assert determine_move(Pos(1,2)) == Pos(1,1)
    assert determine_move(Pos(-1,-1)) == Pos(0,0)
    assert determine_move(Pos(-1, -2)) == Pos(-1, -1)

def test_board_moving():
    gb = GameBoard()
    gb.move_h("U", 1)
    assert (gb.hpos == Pos(0, 1)) and (gb.tpos == Pos(0,0))
    gb.move_h("U", 1)
    assert (gb.hpos == Pos(0, 2) and gb.tpos == Pos(0, 1))
    gb.move_h("R", 2)
    assert (gb.hpos == Pos(2, 2) and gb.tpos == Pos(1, 2))
    assert gb.tail_visits == set([Pos(0, 0,), Pos(0,1), Pos(1,2)])

