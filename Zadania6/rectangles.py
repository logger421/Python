from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self) -> str:  # "[(x1, y1), (x2, y2)]"
        return "[{}, {}]".format(str(self.pt1), str(self.pt2))

    def __repr__(self) -> str:  # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({}, {}, {}, {})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other) -> bool:  # obsługa rect1 == rect2
        return self.area() == other.area()

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

