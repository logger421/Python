def print_measure(x):
    s = "|"
    for n in range(x):
        s += "....|"
    s += '\n'
    for n in range(x + 1):
        s += "{:<5}".format(n)
    return s


if __name__ == '__main__':
    x = int(input("Enter length for your measure: "))
    print(print_measure(x))
