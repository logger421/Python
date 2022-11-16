def add_frac(frac1, frac2):
    if frac1[1] != frac2[1]:
        m = nww(frac1[1], frac2[1])
        if frac1[1] != m and frac2[1] == m:
            return [frac1[0] * (m / frac1[1]) + frac2[0], m]
        elif frac1[1] == m and frac2[1] != m:
            return [frac1[0] + frac2[0] * (m / frac2[1]), m]
        else:
            return [frac1[0] * (m / frac1[1]) + frac2[0] * (m / frac2[1]), m]
    else:
        return [frac1[0] + frac2[0], frac1[1]]


def sub_frac(frac1, frac2):
    if frac1[1] != frac2[1]:
        m = nww(frac1[1], frac2[1])
        if frac1[1] != m and frac2[1] == m:
            return [frac1[0] * (m / frac1[1]) - frac2[0], m]
        elif frac1[1] == m and frac2[1] != m:
            return [frac1[0] - frac2[0] * (m / frac2[1]), m]
        else:
            return [frac1[0] * (m / frac1[1]) - frac2[0] * (m / frac2[1]), m]
    else:
        return [frac1[0] - frac2[0], frac1[1]]


def mul_frac(frac1, frac2):
    return [frac1[0] * frac2[0], frac1[1] * frac2[1]]


def div_frac(frac1, frac2):
    if not is_zero(frac2):
        return mul_frac(frac1, [frac2[1], frac2[0]])
    else:
        raise ZeroDivisionError


def is_positive(frac):
    return True if frac[0] * frac[1] > 0 else False


def is_zero(frac):
    return True if frac[0] == 0 else False


def cmp_frac(frac1, frac2):
    def wsp_mian(f1, f2):
        m = nww(f1[1], f2[1])
        f1 = [f1[0] * (m / f1[1]), m]
        f2 = [f2[0] * (m / f2[1]), m]
        return f1, f2

    frac1, frac2 = wsp_mian(frac1, frac2)
    print(frac1)

    if frac1[0] > frac2[0]:
        return -1
    elif frac1[0] == frac2[0]:
        return 0
    else:
        return 1


def frac2float(frac):
    if frac[1] != 0:
        return float(frac[0] / frac[1])
    else:
        raise ZeroDivisionError


def nww(a, b):
    if a < b:
        return nww(b, a)
    k = a
    while k % b != 0:
        k += a
    return k


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
        self.assertEqual(add_frac([3, 4], [5, 6]), [19, 12])

    def test_sub_frac(self):
        self.assertEqual([1, 4], sub_frac([1, 2], [1, 4]))

    def test_mul_frac(self):
        self.assertEqual([1, 8], mul_frac([1, 2], [1, 4]))

    def test_div_frac(self):
        self.assertEqual([4, 2], div_frac([1, 2], [1, 4]))

    def test_is_positive(self):
        self.assertEqual(False, is_positive([1, -1]))

    def test_is_zero(self):
        self.assertEqual(True, is_zero([0, 1]))
        self.assertEqual(False, is_zero([1, 2]))

    def test_cmp_frac(self):
        self.assertEqual(-1, cmp_frac([1, 2], [1, 4]))

    def test_frac2float(self):
        self.assertEqual(0.5, frac2float([1,2]))

    def tearDown(self):
        print("Tests in progress...")


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
