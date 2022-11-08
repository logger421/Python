# Zadanie 3.5
def print_measure(x):
    s = "|"
    for n in range(x):
        s += "....|"
    s += '\n'
    for n in range(x + 1):
        s += "{:<5}".format(n)
    return s


# Zadanie 3.6
def print_rectangle(y, x):
    s = ""
    rect_len = range(x)
    rect_height = range(y)
    for row in rect_height:
        if row == 0:
            for col in rect_len:
                s += "+---"
                if col == len(rect_len) - 1: s += "+"
            s += "\n"

        for col in rect_len:
            s += "|   "
            if col == len(rect_len) - 1: s += "|"
        s += "\n"

        for col in rect_len:
            s += "+---"
            if col == len(rect_len) - 1: s += "+"
        s += "\n"
    print(s)


if __name__ == '__main__':
    # 3.5
    print(print_measure(8))

    # 3.6
    print("\n")
    print_rectangle(4, 5)
