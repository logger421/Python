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
                if col == len(rect_len) -1: s += "+"
            s += "\n"

        for col in rect_len:
            s += "|   "
            if col == len(rect_len) -1: s += "|"
        s += "\n"

        for col in rect_len:
            s += "+---"
            if col == len(rect_len) -1: s += "+"
        s += "\n"
    print(s)

if __name__ == '__main__':
    # 3.5
    x = int(input("Enter length for your measure: "))
    print(print_measure(x))
    # 3.6
    (y, x) = input("Podaj wymiary prostokąta (HeightxLength):").split("x")
    print_rectangle(int(y), int(x))
