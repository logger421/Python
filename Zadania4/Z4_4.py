def fibonnaci(n):
    if n == 0: return 0
    if n == 1: return 1
    n0, n1 = 0, 1
    i = 2
    result = 0
    while i <= n:
        result = n0 + n1
        n0 = n1
        n1 = result
        i += 1
    return result


if __name__ == '__main__':
    results = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for n in range(10):
        val = fibonnaci(n)
        print(val)
        assert val == results[n]
