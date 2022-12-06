from Zadania8.rectangles import Rectangle
from Zadania6.points import Point
import pytest


def test_constructor_error():
    with pytest.raises(ValueError):
        Rectangle(4, 3, 2, 1)


def test_eq():
    assert Rectangle(0, 0, 1, 1) == Rectangle(0, 0, 1, 1)


def test_neq():
    assert Rectangle(0, 0, 2, 2) != Rectangle(0, 0, 1, 1)


def test_center():
    assert Rectangle(0, 0, 1, 1).center() == Point(0.5, 0.5)


def test_area():
    assert Rectangle(0, 0, 1, 1).area() == 1


def test_move():
    r = Rectangle(0, 0, 1, 1)
    r.move(1, 1)
    assert r == Rectangle(1, 1, 2, 2)
    del r


def test_make4():
    t = Rectangle.make4(Rectangle(0, 0, 2, 2))
    assert t == (Rectangle(0, 0, 1, 1), Rectangle(1, 0, 2, 1),
                 Rectangle(0, 1, 1, 2), Rectangle(1, 1, 2, 2))


def test_cover():
    assert Rectangle(0, 0, 1, 1).cover(Rectangle(0, 0, 2, 2)) == Rectangle(0, 0, 2, 2)


def test_intersection():
    assert Rectangle(0, 0, 2, 2).intersection(Rectangle(1, 1, 2, 2)) == Rectangle(1, 1, 2, 2)


def test_from_points():
    assert Rectangle.from_points((Point(0, 0), Point(1, 1))) == Rectangle(0, 0, 1, 1)


def setup():
    return Rectangle(0, 0, 1, 1)


def teardown(r):
    del r


def test_top_point():
    r = setup()
    assert r.top == 1
    teardown(r)


def test_bottom_point():
    r = setup()
    assert r.bottom == 0
    teardown(r)


def test_right_point():
    r = setup()
    assert r.right == 1
    teardown(r)


def test_left_point():
    r = setup()
    assert r.left == 0
    teardown(r)


def test_width_point():
    r = setup()
    assert r.width == 1
    teardown(r)


def test_height_point():
    r = setup()
    assert r.height == 1
    teardown(r)


def test_bottom_left():
    r = setup()
    assert r.bottomleft == Point(0, 0)
    teardown(r)


def test_bottom_right():
    r = setup()
    assert r.bottomright == Point(1, 0)
    teardown(r)


def test_top_left():
    r = setup()
    assert r.topleft == Point(0, 1)
    teardown(r)


def test_top_right():
    r = setup()
    assert r.topright == Point(1, 1)
    teardown(r)


if __name__ == "__main__":
    pytest.main()
