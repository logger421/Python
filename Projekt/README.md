#### Wojciech Lotko

## Zadanie:

```
Dla ADT grafów z wykładu stworzyć implementację grafów opartą na liście sąsiedztwa (lista list).
Wierzchołki są liczbami int od 0 do n-1. Zaimplementować BFS i DFS.
```

## Dokumentacja:

#### Uruchomienie:

```
# Zakładając, że znajdujemy się w katalogu głównym projektu (obecne repo ./Projekt)
 > python main.py
# lub
 > pyhton3 main.py
```

#### Testowanie

```
# Zakładając, że znajdujemy się w katalogu głównym projektu (obecne repo ./Projekt)
 > python test_edge.py
 > python test_graph.py
# lub
  > python3 test_edge.py
  > python3 test_graph.py
```

#### Folder projektu zawiera w sobie dwie klasy:

- klasę Graph będącą reprezentacją grafu skierowanego/nieskierowanego za pomocą list sąsiedztwa
- klasę Edge reprezentującą pojedynczą krawędź grafu skierowanego

#### Klasa Graph udostępnia nam metody:

- `add_edge(e: Edge)` dodającą krawędź do grafu, przyjmującą jako paramter obiekt klasy Edge,
- `remove_edge(e: Edge)` usuwającą krawędź z grafu, przyjmującą jako parametr obiekt klasy Edge,
- `is_in_graph(e: Edge)` sprawdząjącą czy krawędź jest w grafie, przyjmującą jako parametr obiekt klasy Edge,
- `print(self)` wypisującą graf w konsoli,
- `sort_list(self)` jest to metoda pomocnicza stworzona na potrzeby algorytmu BFS i DFS,
- `load_from_file(fileName: str)` jest to statyczna metoda tworząca graf z pliku tekstowego, przyjmująca
  jako parametr nazwę pliku
- `save_to_file(g: Graph, fileName: str)` jest to statyczna metoda zapisująca graf do pliku tekstowego, przyjmująca
  jako parametry instancję grafu i nazwę pliku.

#### W pliku `graph.py` znajdują się dwie funkcje operujące na obiektach typu Graph:

- `print_bfs(instance: Graph, start: int)` przyjmuje jako parametr instancję klasy, oraz indeks wierzchołka początkowego
  rozpoczynającego algorytm BFS
- `print_dfs(instance: Graph, start: int)` przyjmuje jako parametr instancję klasy, oraz indeks wierzchołka początkowego
  rozpoczynającego algorytm DFS

#### Tworzenie obiektu klasy Graph:

Konstruktor klasy Graph przyjmuje jako parametry dwie zmienne

- max_vertex_idx - reprezentuje maksymalny numer indeksu wierzchołka w naszym grafie
- directed - zmienna typu bool od niej zależy czy graf jest skierowany lub nieskierowany (odpowiednio: `True/False`)

```python
def __init__(self, max_vertex_idx: int, directed: bool = True): pass


# utworzenie obiektu:
g = Graph(3, False)
g = Graph(3, True)
g = Graph(3)  # powstanie graf skierowany
```

Zmienna `directed` ma ustawioną wartość domyślną na `True` dzięki temu możemy tworzyć grafy skierowane z użyciem
konstruktora "jednoargumentowego"

#### Plik main.py

plik `main.py` zawiera główną funkcjonalność projektu, jest to konsolowa aplikacja udostępniająca przystepne,
przykładowe
użycia klasy `graph.py`.

Po uruchomieniu dostaniemy opcje wyboru z czterech dostępnych w menu:

1) Utworzenie grafu - użytkownik zostanie poproszony o podanie maksymalnego indeksu wierzchołka w grafie, oraz musi
   określić
   za pomocą `True/False` czy graf będzie skierowany/nieskierowany. Następnie będzie musiał wprowadzić wszystkie
   krawędzie swojego grafu w formie: `v1 v2` `Enter`, po wprowadzeniu wszystkich należy wcisnąć `q` aby zakończyć
   wprowadzanie. Następnie program przejdzie do pod menu wypisując dostępne operacje dla stworzonego grafu.
2) Wypisanie algorytmu `BFS` na testowym grafie wczytanym z pliku `demo.txt`.
3) Wypisanie algorytmu `DFS` na testowym grafie wczytanym z pliku `demo.txt`.
4) Wczytanie grafu z pliku. Plik musi być w formacie jak załączony plik `demo.txt`. Pierwsza wartość w pliku oznacza
   maksymalny wierzchołek w grafie, druga jest to zmienna bool mówiąca czy graf będzie skierowany/nieskierowany.