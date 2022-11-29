import itertools
import random


# 7.6 a)
class InfIter:
    def __init__(self):
        self.start = 1
        self.division = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 1000000:
            self.start += 1
            return self.start % self.division
        # delete if else clause for truly infinite Iterator, limited it for convenience
        else:
            raise StopIteration()

    next = __next__


class InfWeekDay:
    def __init__(self):
        self.start = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        return self.start % 7

    next = __next__


def main():
    print("Select exercise to show:")
    print("{:4} {:4} {:4}".format("a", "b", "c"))
    selected = input()
    return selected


if __name__ == '__main__':
    choice = main()

    if choice == "a":
        # 7.6 a)
        it = InfIter()
        for x in it:
            print(x, end=" ")

    if choice == "b":
        # 7.6 b)
        it = (random.choice(["N", "E", "S", "W"]) for _ in iter(int, 1))  # przypadkowy dzień tygodnia
        for x in it:
            print(x, end=" ")

    if choice == "c":
        it = InfWeekDay()
        for x in it:
            print(x, end=" ")
