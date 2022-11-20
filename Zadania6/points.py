from __future__ import annotations

import math


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """zwraca string "(x, y)\""""
        return "({}, {})".format(self.x, self.y)

    def __repr__(self) -> str:
        """zwraca string "Point(x, y)"""
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, other) -> bool:
        """obsługa point1 == point2"""
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __ne__(self, other) -> bool:
        """obsługa point1 != point2"""
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other) -> Point:
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other) -> Point:
        """v1 - v2"""
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other) -> int:
        """v1 * v2, iloczyn skalarny, zwraca liczbę"""
        return self.x * other.x + self.y * other.y

    def cross(self, other) -> int:  # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self) -> float:
        """długość wektora"""
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __hash__(self):
        """hash code"""
        return hash((self.x, self.y))  # bazujemy na tuple, immutable points
