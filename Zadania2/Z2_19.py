def fill_missing_numbers(L):
    """The zfill() method adds zeros (0) at the beginning of
     the string, until it reaches the specified length."""
    L = [str(x) for x in L]
    L = [x.zfill(3) for x in L]
    return L


if __name__ == '__main__':
    assert fill_missing_numbers([1, 0, 14, 2, 12, 22, 200, 15, 100]) == ['001', '000', '014', '002', '012', '022', '200', '015', '100']
    assert fill_missing_numbers([1, 0, 14, 2, 12, 22, 200, 15, 100]) != [1, 0, 14, 2, 12, 22, 200, 15, 100]

