#### Wojciech Lotko

### Zadania
OBOWIĄZKOWE DO PRZESŁANIA: jedno zadanie

### ZADANIE 8.1 (KLASA RECTANGLE)
Wzbogacić klasę Rectangle o nowe funkcjonalności (plik rectangles.py).

Stworzyć metodę klasy o nazwie 'from_points', która pozwoli utworzyć prostokąt z listy lub krotki zawierającej dwa punkty, lewy dolny i prawy górny. Wywołanie:
rectangle = Rectangle.from_points((point1, point2))

Za pomocą dekoratora @property dodać atrybuty wirtualne zwracające liczbę (współrzędną): top, left, bottom, right, width, height. Dodać atrybuty wirtualne zwracające Point: topleft, bottomleft, topright, bottomright. Można rozważyć zamianę metody center() na atrybut wirtualny.

W osobnym pliku (test_rectangles.py) przygotować testy klasy Rectangle w formacie dla modułu 'pytest'.

### ZADANIE 8.2 (KLASA TRIANGLE)
Wzbogacić klasę Triangle o nowe funkcjonalności (plik triangles.py).

Stworzyć metodę klasy o nazwie 'from_points', która pozwoli utworzyć trójkąt z listy lub krotki zawierającej trzy punkty. Wywołanie:
triangle = Triangle.from_points((point1, point2, point3))

Za pomocą dekoratora @property dodać atrybuty wirtualne zwracające liczbę (współrzędną): top, left, bottom, right, width, height. Dodać atrybuty wirtualne zwracające Point: topleft, bottomleft, topright, bottomright. Wymienione atrybuty wirtualne opisują prostokąt ograniczający dany trójkąt (bounding box). Można rozważyć zamianę metody center() na atrybut wirtualny.

W osobnym pliku (test_triangles.py) przygotować testy klasy Triangle w formacie dla modułu 'pytest'.

### ZADANIE 8.3 (KLASA CIRCLE)
https://en.wikipedia.org/wiki/Circumscribed_circle#Circumcircle_equations

Wzbogacić klasę Circle o nowe funkcjonalności (plik circles.py).

Stworzyć metodę klasy o nazwie 'from_points', która pozwoli utworzyć okrąg z listy lub krotki zawierającej trzy punkty. Punkty będą leżeć na okręgu [trudne!]. Wywołanie:
circle = Circle.from_points((point1, point2, point3))

Za pomocą dekoratora @property dodać atrybuty wirtualne zwracające liczbę (współrzędną): top, left, bottom, right, width, height. Dodać atrybuty wirtualne zwracające Point: topleft, bottomleft, topright, bottomright. Wymienione atrybuty wirtualne opisują prostokąt ograniczający dany okrąg (bounding box).

W osobnym pliku (test_circles.py) przygotować testy klasy Circle w formacie dla modułu 'pytest'.