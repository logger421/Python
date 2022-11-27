## Wojciech Lotko

# Zadania

### OBOWIĄZKOWE DO PRZESŁANIA: zadanie 7.6 i jedno z 7.1-7.5.

## ZADANIE 7.1 (KLASA FRAC)

W pliku `fracs.py` zdefiniować klasę Frac wraz z potrzebnymi metodami. Wykorzystać wyjątek ValueError do obsługi błędów
w ułamkach. Dodać możliwości dodawania|odejmowania|mnożenia|dzielenia|porównywania liczb `(int, long)` do ułamków (
działania lewostronne i prawostronne). Rozważyć możliwość włączenia liczb float do działań na
ułamkach `[Wskazówka: metoda float.as_integer_ratio()]`. Napisać kod testujący moduł fracs.

## Przykład zachowania klasy Fraction.
```
<<< from fractions import Fraction
<<< Fraction(3.14159)
Fraction(3537115888337719, 1125899906842624)
<<< Fraction(3.14159).limit_denominator(1000) # default is 1000000
Fraction(355, 113)
<<< Fraction(0.4)
Fraction(3602879701896397, 9007199254740992)
<<< Fraction(0.4).limit_denominator(1000)
Fraction(2, 5)
```
```
class Frac:
"""Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        # Sprawdzamy, czy y=0.
        self.x = x
        self.y = y

    def __str__(self): pass         # zwraca "x/y" lub "x" dla y=1

    def __repr__(self): pass        # zwraca "Frac(x, y)"

    # Py2
    #def __cmp__(self, other): pass  # cmp(frac1, frac2)

    # Py2.7 i Py3
    def __eq__(self, other): pass

    def __ne__(self, other): pass

    def __lt__(self, other): pass

    def __le__(self, other): pass

    #def __gt__(self, other): pass

    #def __ge__(self, other): pass

    def __add__(self, other): pass  # frac1+frac2, frac+int

    __radd__ = __add__              # int+frac

    def __sub__(self, other): pass  # frac1-frac2, frac-int

    def __rsub__(self, other):      # int-frac
        # tutaj self jest frac, a other jest int!
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other): pass  # frac1*frac2, frac*int

    __rmul__ = __mul__              # int*frac

    def __div__(self, other): pass  # frac1/frac2, frac/int, Py2

    def __rdiv__(self, other): pass # int/frac, Py2

    def __truediv__(self, other): pass  # frac1/frac2, frac/int, Py3

    def __rtruediv__(self, other): pass  # int/frac, Py3

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self): pass         # -frac = (-1)*frac

    def __invert__(self): pass      # odwrotnosc: ~frac

    def __float__(self): pass       # float(frac)

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # w Pythonie set([2]) == set([2.0])
        # chcemy set([2]) == set([Frac(2)])
```
## Kod testujący moduł.

```
import unittest

class TestFrac(unittest.TestCase): pass
```
## ZADANIE 7.2 (KLASA POLY)
W pliku `polys.py` zdefiniować klasę Poly wraz z potrzebnymi metodami. Wykorzystać wyjątek ValueError do obsługi błędów w
wielomianach. Dodać możliwości dodawania liczb `(int, long, float)` do wielomianów (działania lewostronne i prawostronne).
Dodanie nowych metod kontenerowych i sprawdzenie możliwości iteracji po instancji `(for coeff in poly)`. Napisać kod
testujący moduł polys.
```
class Poly:
"""Klasa reprezentująca wielomiany."""

    # wg Sedgewicka - tworzymy wielomian c*x^n
    def __init__(self, c=0, n=0):
        self.size = n + 1    # rozmiar tablicy
        self.a = self.size * [0]
        self.a[self.size-1] = c

    def __str__(self):
        return str(self.a)

    def __add__(self, other): pass  # poly1+poly2, poly+liczba

    __radd__ = __add__              # liczba+poly

    def __sub__(self, other): pass  # poly1-poly2, poly-liczba

    def __rsub__(self, other): pass # liczba-poly

    def __mul__(self, other): pass  # poly1*poly2, poly*liczba

    __rmul__ = __mul__              # liczba*poly

    def __pos__(self):              # +poly1 = (+1)*poly1
        return self

    def __neg__(self): pass         # -poly1 = (-1)*poly1

    def is_zero(self): pass         # bool, True dla [0], [0, 0],...

    def __eq__(self, other): pass   # obsługa poly1 == poly2

    def __ne__(self, other):        # obsługa poly1 != poly2
        return not self == other

    def eval(self, x): pass         # schemat Hornera

    def combine(self, other):       # złożenie poly1(poly2(x))

    def __pow__(self, n): pass      # poly(x)**n lub pow(poly(x),n)

    def diff(self): pass            # różniczkowanie

    def integrate(self): pass       # całkowanie

    def __len__(self): pass         # len(poly), rozmiar self.a

    def __getitem__(self, i): pass            # poly[i], współczynnik przy x^i

    def __setitem__(self, i, value): pass     # poly[i] = value

    def __call__(self, x): pass     # poly(x)
    # dla isinstance(x, (int,long,float)) odpowiada eval(),
    # dla isinstance(x, Poly) odpowiada combine()
```
## Kod testujący moduł.
```
import unittest

class TestPoly(unittest.TestCase): pass
```
## ZADANIE 7.3 (KLASA RECTANGLE)
W pliku `rectangles.py` zdefiniować klasę Rectangle wraz z potrzebnymi metodami. Wykorzystać wyjątek `ValueError` do obsługi
błędów. Napisać kod testujący moduł rectangles.
```
from points import Point

class Rectangle:
"""Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
    # Chcemy, aby x1 < x2, y1 < y2.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self): pass         # "[(x1, y1), (x2, y2)]"

    def __repr__(self): pass        # "Rectangle(x1, y1, x2, y2)"

    def __eq__(self, other): pass   # obsługa rect1 == rect2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self): pass          # zwraca środek prostokąta

    def area(self): pass            # pole powierzchni

    def move(self, x, y): pass      # przesunięcie o (x, y)

    def intersection(self, other): pass # część wspólna prostokątów

    def cover(self, other): pass    # prostąkąt nakrywający oba

    def make4(self): pass           # zwraca krotkę czterech mniejszych

```
## Kod testujący moduł.
```
import unittest

class TestRectangle(unittest.TestCase): pass
```
## ZADANIE 7.4 (KLASA TRIANGLE)
W pliku `triangles.py` zdefiniować klasę Triangle wraz z potrzebnymi metodami. Wykorzystać wyjątek `ValueError` do obsługi
błędów. Napisać kod testujący moduł triangles.
```
from points import Point

class Triangle:
"""Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        # Należy zabezpieczyć przed sytuacją, gdy punkty są współliniowe.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self): pass         # "[(x1, y1), (x2, y2), (x3, y3)]"

    def __repr__(self): pass        # "Triangle(x1, y1, x2, y2, x3, y3)"

    def __eq__(self, other): pass   # obsługa tr1 == tr2

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self): pass          # zwraca środek trójkąta

    def area(self): pass            # pole powierzchni

    def move(self, x, y): pass      # przesunięcie o (x, y)

    def make4(self): pass           # zwraca krotkę czterech mniejszych
```
## Kod testujący moduł.
```
import unittest

class TestTriangle(unittest.TestCase): pass
```
## ZADANIE 7.5 (KLASA CIRCLE)
W pliku `circles.py` zdefiniować klasę Circle wraz z potrzebnymi metodami. Okrąg jest określony przez podanie środka i
promienia. Wykorzystać wyjątek `ValueError` do obsługi błędów. Napisać kod testujący moduł circles.
```
from points import Point

class Circle:
"""Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self): pass       # "Circle(x, y, radius)"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self): pass           # pole powierzchni

    def move(self, x, y): pass     # przesuniecie o (x, y)

    def cover(self, other): pass   # najmniejszy okrąg pokrywający oba
```
# Kod testujący moduł.
```
import unittest

class TestCircle(unittest.TestCase): pass
```
## ZADANIE 7.6 (ITERATORY)
Stworzyć następujące iteratory nieskończone:
```
(a) zwracający 0, 1, 0, 1, 0, 1, ...,
(b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D],
(c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia].
```