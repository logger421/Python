def convert_to_string(l):
    l = [str(x) for x in l]
    return "".join(l)

L = list(range(10))

if __name__ == '__main__':
    print(convert_to_string(L))