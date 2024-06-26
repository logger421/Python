## Wojciech Lotko
Zadania
OBOWIĄZKOWE DO PRZESŁANIA: 5.2 lub 5.3

## ZADANIE 5.1
Stworzyć plik rekurencja.py i zapisać w nim funkcje z zadań 4.3 (factorial), 4.4 (fibonacci). Sprawdzić operacje importu i przeładowania modułu.
```
import rekurencja
# import rekurencja as rek
# from rekurencja import *
# from rekurencja import factorial
# from rekurencja import fibonacci as fib

print ( rekurencja.factorial(6) )
print ( rekurencja.fibonacci(5) )
```
## ZADANIE 5.2
Stworzyć plik fracs.py i zapisać w nim funkcje do działań na ułamkach. Ułamek będzie reprezentowany przez listę dwóch liczb całkowitych [licznik, mianownik]. Napisać kod testujący moduł fracs. Nie należy korzystać z klasy Fraction z modułu fractions. Można wykorzystać funkcję fractions.gcd() implementującą algorytm Euklidesa.
```
def add_frac(frac1, frac2): pass        # frac1 + frac2
def sub_frac(frac1, frac2): pass        # frac1 - frac2
def mul_frac(frac1, frac2): pass        # frac1 * frac2
def div_frac(frac1, frac2): pass        # frac1 / frac2
def is_positive(frac): pass             # bool, czy dodatni
def is_zero(frac): pass                 # bool, typu [0, x]
def cmp_frac(frac1, frac2): pass        # -1 | 0 | +1
def frac2float(frac): pass              # konwersja do float

# f1 = [-1, 2]      # -1/2
# f2 = [1, -2]      # -1/2 (niejednoznaczność)
# f3 = [0, 1]       # zero
# f4 = [0, 2]       # zero (niejednoznaczność)
# f5 = [3, 1]       # 3
# f6 = [6, 2]       # 3 (niejednoznaczność)



import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self): pass

    def test_mul_frac(self): pass

    def test_div_frac(self): pass

    def test_is_positive(self): pass

    def test_is_zero(self): pass

    def test_cmp_frac(self): pass

    def test_frac2float(self): pass

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
```
## ZADANIE 5.3
Stworzyć plik polys.py i zapisać w nim funkcje do działań na wielomianach. Wielomian będzie reprezentowany przez listę swoich współczynników, np. [a0, a1, a2] dla a0 + a1*x + a2*x*x. Napisać kod testujący moduł polys.

```
def add_poly(poly1, poly2): pass        # poly1(x) + poly2(x)

def sub_poly(poly1, poly2): pass        # poly1(x) - poly2(x)

def mul_poly(poly1, poly2): pass        # poly1(x) * poly2(x)

def is_zero(poly): pass                 # bool, [0], [0,0], itp.

def eq_poly(poly1, poly2): pass        # bool, porównywanie poly1(x) == poly2(x)

def eval_poly(poly, x0): pass           # poly(x0), algorytm Hornera

def combine_poly(poly1, poly2): pass    # poly1(poly2(x)), trudne!

def pow_poly(poly, n): pass             # poly(x) ** n

def diff_poly(poly): pass               # pochodna wielomianu

# p1 = [2, 1]                   # W(x) = 2 + x
# p2 = [2, 1, 0]                # jw  (niejednoznaczność)
# p3 = [-3, 0, 1]               # W(x) = -3 + x^2
# p4 = [3]                      # W(x) = 3, wielomian zerowego stopnia
# p5 = [0]                      # zero
# p6 = [0, 0, 0]                # zero (niejednoznaczność)

import unittest

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]      # W(x) = x
        self.p2 = [0, 0, 1]   # W(x) = x^2

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])

    def test_sub_poly(self): pass

    def test_mul_poly(self): pass

    def test_is_zero(self): pass

    def test_eq_poly(self): pass

    def test_eval_poly(self): pass

    def test_combine_poly(self): pass

    def test_pow_poly(self): pass

    def test_diff_poly(self): pass

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
```
## ZADANIE 5.4
Stworzyć plik sparsepolys.py i zapisać w nim funkcje do działań na wielomianach o wysokim rzędzie, ale małej liczbie wyrazów. Wielomian będzie reprezentowany przez słownik, `{0: a0, 1: a1, 2: a2}` dla `a0 + a1*x + a2*x*x`. Napisać kod testujący moduł sparsepolys.
```
p1 = {10: 1, 0: 2}            # W(x) = x**10 + 2
p2 = {100: 4, 5: 3}           # W(x) = 4 * x**100 + 3 * x**5
p3 = {0: 3}                   # W(x) = 3, wielomian zerowego stopnia
p4 = {0: 0}                   # zero
p5 = {5: 0}                   # zero (niejednoznaczność)
```
## ZADANIE 5.5
Stworzyć plik sparsematrices.py i zapisać w nim funkcje do działań na macierzach rzadkich, czyli macierzach o małej liczbie niezerowych współczynników. Macierz będzie reprezentowana przez słownik, `{(1,2): 3, (10, 20): 30}` dla macierzy o niezerowych współczynnikach `M[1, 2] = 3, M[10, 20] = 30`. Zakładamy, że macierze są kwadratowe, a ich wymiar jest odpowiednio duży. Napisać kod testujący moduł sparsematrices.

```
def add_sparse(sparse1, sparse2): pass        # sparse1 + sparse2

def sub_sparse(sparse1, sparse2): pass        # sparse1 - sparse2

def mul_sparse(sparse1, sparse2): pass        # sparse1 * sparse2

def is_diagonal(sparse): pass                 # bool, czy diagonalna

def is_empty(sparse): pass                    # bool, czy zerowa

s1 = {}                                       # macierz zerowa
s2 = {(2, 2): 3, (5, 5): 9}                   # macierz diagonalna
```