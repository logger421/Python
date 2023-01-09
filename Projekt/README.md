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
 > pytest test_edge.py
# lub
 > pyhton3 test_graph.py
```

#### Folder projektu zawiera w sobie dwie klasy:
- klasę Graph będącą reprezentacją grafu za pomocą listw sąsiedztwa
- klasę Edge reprezentującą pojedynczą krawędź grafu skierowanego

#### Klasa Graph udostępnia nam metody:
- `add_edge(e: Edge)` dodającą krawędź do grafu, przyjmującą jako paramter obiekt klasy Edge,
- `remove_edge(e: Edge)` usuwającą krawędź z grafu, przyjmującą jako parametr obiekt klasy Edge,
- `is_in_graph(e: Edge)` sprawdząjącą czy krawędź jest w grafie, przyjmującą jako parametr obiekt klasy Edge,
- `print(self)` wypisującą graf w konsoli,
- `sort_list(self)` jest to metoda pomocnicza stworzona na potrzeby algorytmu BFS i DFS,
- `load_from_file(fileName: str)` jest to statyczna metoda tworząca graf z pliku tekstowego, przyjmująca 
  jako parametr nazwę pliku 

#### W pliku `graph.py` znajdują się dwie funkcje operujące na obiektach typu Graph:
- `print_bfs(instance: Graph, start: int)` przyjmuje jako parametr instancję klasy, oraz indeks wierzchołka początkowego 
  rozpoczynającego algorytm BFS
- `print_dfs(instance: Graph, start: int)` przyjmuje jako parametr instancję klasy, oraz indeks wierzchołka początkowego 
  rozpoczynającego algorytm DFS

#### Plik main.py
plik `main.py` zawiera główną funkcjonalność projektu, jest to konsolowa aplikacja udostępniająca przystepne, przykładowe
użycia klasy `graph.py`. 

Po uruchomieniu dostaniemy opcje wyboru z czterech dostępnych w menu:
1) Utworzenie grafu - użytkownik zostanie poproszony o podanie maksymalnego indeksu wierzchołka w grafie a nastęnie 
   będzie musiał wprowadzić wszystkie krawędzie swojego grafu w formie: `v1 v2` `Enter`, po wprowadzeniu wszystkich `q` 
   aby zakończyć. Następnie graf zostanie wypisany na ekran
2) Wypisanie algorytmu `BFS` na stworzonym już grafie
3) Wypisanie algorytmu `DFS` na stworzonym już grafie
4) Wczytanie grafu z pliku. Plik musi być w formacie jak załączony plik `demo.txt`. Pierwsza wartość w pliku oznacza
   maksymalny wierzchołek w grafie.