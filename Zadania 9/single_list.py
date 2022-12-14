class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)  # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0  # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def __iter__(self):
        # Przy tworzeniu iteratora trzeba mieć zmienną, która będzie pamiętać stan.
        # Przy kolejnym tworzeniu iteratora będzie ustawianie na początek.
        self.current = self.head
        return self

    def __next__(self):
        if self.current:
            node = self.current
            self.current = self.current.next
            return node.data
        else:  # self.current is None
            raise StopIteration

    next = __next__  # kompatybilność Py2 i Py3

    def is_empty(self):
        # return self.length == 0
        return self.head is None

    def count(self):  # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.head:  # dajemy na koniec listy
            node.next = self.head
            self.head = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def insert_tail(self, node):  # klasy O(1)
        if self.head:  # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        else:  # pusta lista
            self.head = self.tail = node
        self.length += 1

    def remove_head(self):  # klasy O(1)
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.head == self.tail:  # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None  # czyszczenie łącza
        self.length -= 1
        return node  # zwracamy usuwany node

    def remove_tail(self):
        if self.is_empty():
            raise ValueError("pusta lista")
        node = self.head
        if self.tail == self.head:  # lista z jednym elementem
            tmp = self.tail
            self.head = self.tail = None
            self.length -= 1
            return tmp
        else:
            while node.next != self.tail:
                node = node.next
            tmp = self.tail
            node.next = None
            self.tail = node
        self.length -= 1
        return tmp

    def join(self, other):
        if other.is_empty():
            raise ValueError("pusta lista")
        while not other.is_empty():
            self.insert_tail(other.remove_tail())

    def clear(self):
        if self.is_empty():
            raise ValueError("pusta lista")
        while not self.is_empty():
            self.remove_tail()


def print_list(l):
    if l.is_empty():
        print('List is empty!')
    for item in l:
        print(item)
