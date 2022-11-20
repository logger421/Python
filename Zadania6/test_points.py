import math
import unittest
from points import Point


class TestPoint(unittest.TestCase):
    def test_return_str(self):
        print("Testing __str__")
        self.assertEqual(str(Point(0, 0)), "(0, 0)")
        self.assertEqual(str(Point(1, 0)), "(1, 0)")
        self.assertEqual(str(Point(0, 1)), "(0, 1)")

    def test_return_repr(self):
        print("Testing __repr__")
        self.assertEqual(repr(Point(0, 0)), "Point(0, 0)")
        self.assertEqual(repr(Point(1, 0)), "Point(1, 0)")
        self.assertEqual(repr(Point(0, 1)), "Point(0, 1)")

    def test_equal(self):
        print("Testing __eq__")
        self.assertEqual(Point(1, 1), Point(1, 1))
        self.assertEqual(Point(1, 2), Point(1, 2))
        self.assertTrue(Point(0, 0) == Point(0, 0))
        self.assertTrue(Point(1, 1) == Point(1, 1))
        self.assertFalse(Point(0, 0) == Point(1, 1))
        self.assertFalse(Point(0, 0) == Point(2, 2))

    def test_negation(self):
        print("Testing __ne__")
        self.assertNotEqual(Point(1, 1), Point(2, 1))
        self.assertNotEqual(Point(4, 1), Point(4, 4))
        self.assertTrue(Point(0, 0) != Point(1, 0))
        self.assertTrue(Point(1, 1) != Point(1, 2))
        self.assertFalse(Point(0, 0) != Point(0, 0))
        self.assertFalse(Point(1, 0) != Point(1, 0))

    def test_add(self):
        print("Testing __add__")
        self.assertEqual(Point(0, 0) + Point(1, 1), Point(1, 1))
        self.assertEqual(Point(1, 3) + Point(1, 1), Point(2, 4))

    def test_sub(self):
        print("Testing __sub__")
        self.assertEqual(Point(0, 0) - Point(1, 1), Point(-1, -1))
        self.assertEqual(Point(1, 3) - Point(1, 1), Point(0, 2))

    def test_mul(self):
        print("Testing __mul__")
        self.assertEqual(Point(0, 0) * Point(1, 1), 0)
        self.assertEqual(Point(1, 1) * Point(1, 1), 2)
        self.assertEqual(Point(3, 1) * Point(1, 2), 5)
        self.assertEqual(Point(2, 2) * Point(1, 1), 4)

    def test_cross(self):
        print("Testing __cross__")
        self.assertEqual(Point(1, 1).cross(Point(1, 1)), 0)
        self.assertEqual(Point(3, 1).cross(Point(1, 2)), 5)
        self.assertEqual(Point(2, 2).cross(Point(1, 1)), 0)
        self.assertEqual(Point(0, 0).cross(Point(0, 0)), 0)

    def test_length(self):
        print("Testing length")
        self.assertEqual(Point(1, 1).length(), math.sqrt(2))
        self.assertEqual(Point(2, 1).length(), math.sqrt(5))
        self.assertEqual(Point(2, 2).length(), math.sqrt(8))

    def test_hash(self):
        print("Testing __hash__")
        p1 = Point(0, 0)
        p2 = Point(0, 0)
        self.assertEqual(p1.__hash__(), p2.__hash__())
        p2 = Point(1, 0)
        self.assertNotEqual(p1.__hash__(), p2.__hash__())
        del p1, p2


if __name__ == '__main__':
    unittest.main()
