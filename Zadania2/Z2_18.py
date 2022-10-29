def find_zero(x):
    s = str(x)
    return s.count('0')

if __name__ == '__main__':
    assert find_zero(1230) == 1
    assert find_zero(0) == 1
    assert find_zero(123) == 0
    assert find_zero(1000) == 3
    assert find_zero(2100) == 2

