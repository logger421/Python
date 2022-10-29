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
    (y, x) = input("Podaj wymiary prostokąta (HeightxLength):").split("x")
    print_rectangle(int(y), int(x))