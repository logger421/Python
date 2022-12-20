import random


class RandomQueue:
    def __init__(self):
        self.items = []

    def insert(self, data):
        self.items.append(data)

    def remove(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        max = len(self.items) - 1
        idx = random.randint(0, max)
        tmp = self.items[idx]
        self.items[idx] = self.items[max]
        self.items[max] = tmp
        return self.items.pop()

    def is_empty(self):
        return not self.items

    def is_full(self):
        return False

    def clear(self):
        self.items.clear()
