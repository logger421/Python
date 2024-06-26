#### Wojciech Lotko

Zadania
OBOWIĄZKOWE DO PRZESŁANIA: jedno zadanie ze stosem lub kolejką (10.2 - 10.7), zadanie z kolejką przypadkową (10.8)

W rozwiązaniach należy umieścić kod testujący przygotowane funkcje.

### ZADANIE 10.1 (MATRIX)
W pliku matrix.py zdefiniować klasę Matrix reprezentującą macierz prostokątną. Wykorzystać wyjątek ValueError do obsługi błędów, np. przy dodawaniu macierzy liczby wierszy i kolumn obu macierzy powinny być zgodne; indeksy wierszy i kolumn muszą być w określonych przedziałach (Python wykryje tylko przekroczenie zakresu listy). Poprawić metodę do wyświetlania macierzy.
```
class Matrix:

    def __init__(self, rows=1, cols=1):
        self.rows = rows
        self.cols = cols
        self.data = [0] * rows * cols

    def __str__(self):
        return str(self.data)

    def __getitem__(self, pair):   # odczyt m[i,j]
        i, j = pair
        return self.data[i * self.cols + j]

    def __setitem__(self, pair, value):   # m[i,j] = value
        i, j = pair
        self.data[i * self.cols + j] = value

    def __add__(self, other): pass   # dodawanie macierzy

    def __sub__(self, other): pass   # odejmowanie macierzy

    def __mul__(self, other): pass   # mnożenie macierzy

# Zastosowanie.
m = Matrix(3, 4)
m[1, 2] = 12     # metoda __setitem__
print(m[1, 2])   # metoda __getitem__
print(m)         # metoda __str__
```
### ZADANIE 10.2 (STACK)
Poprawić implementację tablicową stosu tak, aby korzystała z wyjątków w przypadku pojawienia się błędu. Metoda pop() ma zgłaszać błąd w przypadku pustego stosu. Metoda push() ma zgłaszać błąd w przypadku przepełnienia stosu. Napisać kod testujący stos.

### ZADANIE 10.3 (STACK)
Stworzyć implementację tablicową stosu do przechowywania bez powtórzeń liczb całkowitych od 0 do size-1. Powtarzająca się liczba ma być ignorowana bez żadnej akcji (inne podejście to wyzwolenie wyjątku). Wskazówka: stworzyć drugą tablicę, w której 0 lub 1 na pozycji i oznacza odpowiednio brak lub istnienie liczby i na stosie.

### ZADANIE 10.4 (QUEUE)
Poprawić metodę get(), aby w przypadku pustej kolejki zwracała wyjątek. Poprawić metodę put() w tablicowej implementacji kolejki, aby w przypadku przepełnienia kolejki zwracała wyjątek. Napisać kod testujący kolejkę.

### ZADANIE 10.5 (PRIORITYQUEUE)
Poprawić metodę remove() w pythonowej implementacji kolejki priorytetowej tak, aby uniknąć kosztownego pobierania elementu ze środka listy.

Poprawić metodę remove() w tablicowej implementacji kolejki priorytetowej, aby w przypadku pustej kolejki generowała wyjątek.

Poprawić metodę insert() w tablicowej implementacji kolejki priorytetowej, aby w przypadku przepełnienia kolejki generowała wyjątek.

### ZADANIE 10.6 (PRIORITYQUEUE)
Załóżmy, że w kolejce priorytetowej będą przechowywane elementy, których priorytet można zmienić za pomocą metody increase(value). Dodać kolejce metodę increase(value), która pozwoli na zmianę priorytetów wszystkich elementów w kolejce o wartość value. Taka kolejka może symulować działanie systemu operacyjnego, który zwiększa priorytet zadaniom czekającym w kolejce do wykonania. Cykliczne zwiększanie priorytetów zapobiega długiemu przebywaniu w kolejce zadań o niskim początkowym priorytecie.

### ZADANIE 10.7 (PRIORITYQUEUE)
W pythonowej implementacji kolejki priorytetowej dodać możliwość ustawiania sposobu porównywania elementów znajdujących się w kolejce.
```
class PriorityQueue:

    def __init__(self, cmpfunc=cmp):
        self.items = []
        self.cmpfunc = cmpfunc
ZADANIE 10.8 (RANDOMQUEUE)
Stworzyć ADT w postaci kolejki losowej, z której elementy będą pobierane w losowej kolejności. Zadbać o to, aby każda operacja była wykonywana w stałym czasie, niezależnie od liczby elementów w kolejce.

class RandomQueue:

    def __init__(self): pass

    def insert(self, item): pass   # wstawia element w czasie O(1)

    def remove(self): pass   # zwraca losowy element w czasie O(1)

    def is_empty(self): pass

    def is_full(self): pass

    def clear(self): pass   # czyszczenie listy
```

### ZADANIE 10.8 (RANDOMQUEUE)
Stworzyć ADT w postaci kolejki losowej, z której elementy będą pobierane w losowej kolejności. Zadbać o to, aby każda operacja była wykonywana w stałym czasie, niezależnie od liczby elementów w kolejce.
```
class RandomQueue:

    def __init__(self): pass

    def insert(self, item): pass   # wstawia element w czasie O(1)

    def remove(self): pass   # zwraca losowy element w czasie O(1)

    def is_empty(self): pass

    def is_full(self): pass

    def clear(self): pass   # czyszczenie listy
```