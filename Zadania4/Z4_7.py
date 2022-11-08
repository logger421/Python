def flatten(seq):
    sq = []
    for el in seq:
        if isinstance(el, (list, tuple)):
            for sub_el in flatten(el):
                yield sub_el
        else:
            yield el


if __name__ == '__main__':
    seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
    assert list(flatten(seq)) == [1,2,3,4,5,6,7,8,9]
