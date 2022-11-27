from __future__ import annotations
from Zadania6.points import Point


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 > x2 or y1 > y2:
            raise ValueError("Chcemy, aby x1 < x2, y1 < y2.")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self) -> str:  # "[(x1, y1), (x2, y2)]"
        return "[{}, {}]".format(str(self.pt1), str(self.pt2))

    def __repr__(self) -> str:  # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({}, {}, {}, {})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other) -> bool:  # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):  # obsługa rect1 != rect2
        return not self == other

    def center(self) -> Point:  # zwraca środek prostokąta
        x1, y1 = self.pt1.x, self.pt1.y
        x2, y2 = self.pt2.x, self.pt2.y
        return Point((x1 + x2) * 0.5, (y1 + y2) * 0.5)

    def area(self) -> float:  # pole powierzchni
        x1, y1 = self.pt1.x, self.pt1.y
        x2, y2 = self.pt2.x, self.pt2.y
        return (y2 - y1) * (x2 - x1)

    def move(self, x, y):  # przesunięcie o (x, y)
        v = Point(x, y)
        self.pt1 += v
        self.pt2 += v

    def intersection(self, other) -> Rectangle:
        '''część wspólna prostokątów'''
        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)

        return Rectangle(x1, y1, x2, y2)

    def cover(self, other) -> Rectangle:
        points = [self.pt1, self.pt2, other.pt1, other.pt2]

        def find_min_xy(l: list) -> tuple:
            '''Finds minial (x, y) inside given points'''
            min_x = min([p.x for p in l])
            min_y = min([p.y for p in l])
            return min_x, min_y

        def find_max_xy(l: list) -> tuple:
            '''Finds maximal (x, y) inside given points'''
            max_x = max([p.x for p in l])
            max_y = max([p.y for p in l])
            return max_x, max_y

        return Rectangle(*find_min_xy(points), *find_max_xy(points))

    def make4(self) -> tuple:
        '''zwraca krotkę czterech mniejszych'''
        center = self.center()
        r1 = Rectangle(self.pt1.x, self.pt1.y, center.x, center.y)
        r2 = Rectangle(center.x, self.pt1.y, self.pt2.x, center.y)
        r3 = Rectangle(self.pt1.x, center.y, center.x, self.pt2.y)
        r4 = Rectangle(center.x, center.y, self.pt2.x, self.pt2.y)

        return r1, r2, r3, r4


if __name__ == '__main__':
    r1 = Rectangle(0, 0, 1, 1)
    r2 = Rectangle(0, 0, 2, 2)

    print(r1.cover(r2))
