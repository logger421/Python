def odwracanie(L, left, right):
    P = L[left:right].reverse()
    print(P)

if __name__ == '__main__':
    odwracanie([1,2,3,4], 0, 3)