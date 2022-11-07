from functools import reduce


def factorial(n):
    if n == 0:
        return 1
    if n < 0:
        raise ValueError("Factorial cannot be calculated on negative numbers!")
    i = 1
    s = 1
    while i <= n:
        s *= i
        i += 1
    return s


def factorial2(n):
    if n == 0:
        return 1
    if n < 0:
        raise ValueError("Factorial cannot be calculated on negative numbers!")
    return reduce((lambda x,y: x*y), range(1, n+1))

if __name__ == '__main__':
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120

    assert factorial2(0) == 1
    assert factorial2(1) == 1
    assert factorial2(2) == 2
    assert factorial2(3) == 6
    assert factorial2(4) == 24
    assert factorial2(5) == 120
