def sum_seq(sequence):
    sum = 0
    for el in sequence:
        if isinstance(el, (list, tuple)):
            sum += sum_seq(el)
        else:
            sum += el
    return sum


if __name__ == "__main__":
    print(sum_seq([1, 2, [3, 4], [5, 6], (7, 8, 9)]))
