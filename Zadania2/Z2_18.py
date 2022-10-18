def find_zero(x):
    s = str(x)
    if "0" in s:
        return True
    return False

if __name__ == '__main__':
    assert find_zero(1230) == True
    assert find_zero(0) == True
    assert find_zero(123) == False

