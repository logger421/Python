def union(l1, l2):
    return sorted(list(set().union(l1, l2)))


def intersection(l1, l2):
    return sorted(list(set(l1) & set(l2)))

if __name__ == '__main__':
    print("Intersection:")
    print(intersection([1, 1, 2, 3, 8], [1, 1, 3]))
    print("Union:")
    print(union([1, 1, 2, 3, 8], [1, 1, 3]))
    print("Intersection:")
    print(intersection(['a', 'b', 'c'], ['a', 'd', 'e', 'b']))
    print("Union:")
    print(union(['a', 'b', 'c'], ['c', 'd', 'e']))
