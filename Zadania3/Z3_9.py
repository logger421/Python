def sum_each_subsequence(x):
    return [sum(sq) for sq in x]

if __name__ == '__main__':
    print(sum_each_subsequence([[],[4],(1,2),[3,4],(5,6,7)]))