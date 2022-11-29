import unittest
from rectangles import Rectangle
from Zadania6.points import Point


class TestPoint(unittest.TestCase):
    def setUp(self) -> None:
        self.r1 = Rectangle(0, 0, 1, 1)

    def tearDown(self) -> None:
        del self.r1

    def test_str(self):
        self.assertEqual(str(self.r1), "[(0, 0), (1, 1)]")

    def test_repr(self):
        self.assertEqual(repr(self.r1), "Rectangle(0, 0, 1, 1)")

    def test_eq(self):
        r2 = Rectangle(0, 0, 1, 1)
        self.assertTrue(self.r1 == r2)
        r2 = Rectangle(0, 0, 2, 2)
        self.assertFalse(self.r1 == r2)

    def test_neq(self):
        r2 = Rectangle(0, 0, 2, 2)
        self.assertTrue(self.r1 != r2)

    def test_center(self):
        self.assertEqual(self.r1.center(), Point(0.5, 0.5))

    def test_area(self):
        self.assertEqual(self.r1.area(), 1)

    def test_move(self):
        self.r1.move(1, 1)
        self.assertTrue(self.r1 == Rectangle(1, 1, 2, 2))

    def test_make4(self):
        self.assertTupleEqual(Rectangle.make4(Rectangle(0,0,2,2)),
                              (Rectangle(0, 0, 1, 1), Rectangle(1, 0, 2, 1),
                               Rectangle(0, 1, 1, 2), Rectangle(1, 1, 2, 2)))

    def test_cover(self):
        self.assertEqual(Rectangle(0, 0, 1, 1).cover(Rectangle(0, 0, 2, 2)), Rectangle(0, 0, 2, 2))
        self.assertEqual(Rectangle(0, 0, 1, 1).cover(Rectangle(0, 0, 2, 2)), Rectangle(0, 0, 2, 2))

    def test_intersection(self):
        self.assertEqual(Rectangle(0, 0, 2, 2).intersection(Rectangle(1, 1, 2, 2)), Rectangle(1, 1, 2, 2))


if __name__ == '__main__':
    unittest.main()
