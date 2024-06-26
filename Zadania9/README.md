#### Wojciech Lotko
### Zadania
OBOWIĄZKOWE DO PRZESŁANIA: jedno zadanie z zestawu

W rozwiązaniach należy umieścić kod testujący przygotowane funkcje.

### ZADANIE 9.1 (SINGLELIST)
Do klasy SingleList dodać nowe metody.
```
class SingleList:
# ... inne metody ...

    def remove_tail(self): pass   # klasy O(n)
        # Zwraca cały węzeł, skraca listę.
        # Dla pustej listy rzuca wyjątek ValueError.

    def join(self, other): pass   # klasy O(1)
        # Węzły z listy other są przepinane do listy self na jej koniec.
        # Po zakończeniu operacji lista other ma być pusta.

    def clear(self): pass   # czyszczenie listy
```
```
POCZĄTEK JOIN
A1 o-- self.head
|
A2 o-- self.tail
|
None

B1 o-- other.head
|
B2 o-- other.tail
|
None

KONIEC JOIN
A1 o-- self.head
|
A2
|
B1
|
B2 o-- self.tail
|
None

None o-- other.head = other.tail
```

### ZADANIE 9.2 (SINGLELIST)
Do klasy SingleList dodać nowe metody.
```
class SingleList:
# ... inne metody ...

    def search(self, data): pass   # klasy O(n)
        # Zwraca łącze do węzła o podanym kluczu lub None.

    def find_min(self): pass   # klasy O(n)
        # Zwraca łącze do węzła z najmniejszym kluczem lub None dla pustej listy.

    def find_max(self): pass   # klasy O(n)
        # Zwraca łącze do węzła z największym kluczem lub None dla pustej listy.

    def reverse(self): pass   # klasy O(n)
        # Odwracanie kolejności węzłów na liście.

```
### ZADANIE 9.3 (DOUBLELIST)
Do klasy DoubleList dopisać nowe metody.
```
class DoubleList:

    def find_max(self): pass
        # Zwraca łącze do węzła z największym kluczem lub None dla pustej listy.

    def find_min(self): pass
        # Zwraca łącze do węzła z najmniejszym kluczem lub None dla pustej listy.

    def remove(self, node): pass
        # Usuwa wskazany węzeł z listy (węzeł należy do listy).

    def clear(self): pass   # czyszczenie listy
```
### ZADANIE 9.4 (SORTEDLIST)
Na bazie list powiązanych pojedynczo lub podwójnie stworzyć klasę SortedList, która przechowuje listę stale posortowaną. Największy element jest na początku listy (head).

```
class SortedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.head is None

    def insert(self, node): pass
        # L = SortedList() ; L.insert(Node(3))

    def remove(self): pass
        # Zwraca node z elementem największym, czyli head.
        # Długość listy zmniejsza się o jeden węzeł.

    def merge(self, other): pass
        # Scalanie dwóch list posortowanych.
        # Po tej operacji lista other ma być pusta.

    def clear(self): pass   # czyszczenie listy
```

### ZADANIE 9.5 (CYCLICLIST)
Na bazie list powiązanych pojedynczo lub podwójnie (to jest wygodniejsze) stworzyć klasę CyclicList, która przechowuje listę cykliczną. Atrybut head może wskazywać na dowolny węzeł listy cyklicznej, natomiast przez tail rozumiemy węzeł bezpośrednio poprzedzający head.
```
class CyclicList:

    def __init__(self):
        self.head = None   # łącze do dowolnego węzła listy
        # nie potrzeba mieć self.tail

    def is_empty(self):
        return self.head is None

    def insert_head(self, node): pass

    def insert_tail(self, node): pass

    def search(self, data):   # zwraca node lub None

    def remove(self, node): pass

    def join(self, other): pass   # scalanie dwóch list cyklicznych w czasie O(1)

    def clear(self): pass   # czyszczenie listy
```