def odwracanie(L, left, right):
    while left != right:
        cp = L[right]
        L[right] = L[left]
        L[left] = cp
        left += 1
        right -= 1
    return L


if __name__ == '__main__':
    L = [1, 2, 3, 4]
    print(odwracanie(L, 0, 3))
