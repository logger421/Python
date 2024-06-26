## Wojciech Lotko
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8">
</head>

<body bgcolor="white" text="black" link="blue" vlink="navy" alink="red">

<h1>Zadania</h1>


<p>OBOWIĄZKOWE DO PRZESŁANIA: wszystko oprócz 3.7

<p>Prosty sposób na automatyczne sprawdzenie kodu:
<br>assert result == expected_result

<p>W zadaniach budujemy całe napisy, a nie wyświetlamy po kawałku.

<h3>ZADANIE 3.1</h3>

<p>Czy podany kod jest poprawny składniowo w Pythonie?
Jeśli nie, to dlaczego?

<hr><pre>
x = 2; y = 3;
if (x &gt; y):
    result = x;
else:
    result = y;
</pre><hr><pre>
for i in "axby": if ord(i) &lt; 100: print (i)
</pre><hr><pre>
for i in "axby": print (ord(i) if ord(i) &lt; 100 else i)
</pre><hr>

<h3>ZADANIE 3.2</h3>

<p>Co jest złego w kodzie:

<hr><pre>
L = [3, 5, 4] ; L = L.sort()
</pre><hr><pre>
x, y = 1, 2, 3
</pre><hr><pre>
X = 1, 2, 3 ; X[1] = 4
</pre><hr><pre>
X = [1, 2, 3] ; X[3] = 4
</pre><hr><pre>
X = "abc" ; X.append("d")
</pre><hr><pre>
L = list(map(pow, range(8)))
</pre><hr>

<h3>ZADANIE 3.3</h3>

<p>Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb
podzielnych przez 3.

<pre>
</pre>

<h3>ZADANIE 3.4</h3>

<p>Napisać program pobierający w pętli od użytkownika
liczbę rzeczywistą x (typ float) i wypisujący x oraz trzecią potęgę x.
Zatrzymanie programu następuje po wpisaniu z klawiatury <em>stop</em>.
Jeżeli użytkownik wpisze napis zamiast liczby, to program
ma wypisać komunikat o błędzie i kontynuować pracę.


<h3>ZADANIE 3.5</h3>

<p>Napisać program rysujący "miarkę" o zadanej długości.
Należy prawidłowo obsłużyć liczby składające się z kilku cyfr
(ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej).
Należy zbudować pełny string, a potem go wypisać.

<pre>
|....|....|....|....|....|....|....|....|....|....|....|....|
0    1    2    3    4    5    6    7    8    9   10   11   12
</pre>

<h3>ZADANIE 3.6</h3>

<p>Napisać program rysujący prostokąt zbudowany z małych kratek.
Należy zbudować pełny string, a potem go wypisać.
Przykładowy prostokąt składający się 2x4 pól ma postać:

<pre>
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   | 
+---+---+---+---+
</pre>


<h3>ZADANIE 3.7</h3>

<p>Podany fragment programu pokaże problem z wyświetlaniem
list obiektów stworzonych przez użytkownika,
jeżeli nie została zdefiniowana metoda __repr__.
Jeżeli zdefiniowano tylko metodę __repr__, to zostanie
ona użyta również wtedy, gdy zwykle pracuje __str__.
Sprawdzić działanie kodu, jeżeli wykomentujemy metodę __str__()
lub metodę __repr__().

<!--
<p>Załóżmy, że mamy listę obiektów, które nie mają zdefiniowanej
metody __repr__(). Napisać program wypisujący na ekranie zawartość 
listy z użyciem metody __str__(). Przykładowo dla listy [a, b]
chcemy dostać string "["+str(a)+", "+str(b)+"]".
Należy prawidłowo obsłużyć przypadek pustej sekwencji. 
-->

<hr><pre>
class Time:

    def __init__(self, seconds=0):
        self.s = seconds

    def __str__(self):
        return "{} sec".format(self.s)

    def __repr__(self):
        return "Time({})".format(self.s)

time1 = Time(12)
time2 = Time(3456)
print("{} {}".format(time1, time2))   # Python wywołuje str()
print("{}".format([time1, time2]))   # Python wywołuje repr()
</pre><hr>

<h3>ZADANIE 3.8</h3>

<p>Dla dwóch sekwencji liczb lub znaków znaleźć:
(a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń),
(b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).

<pre>
</pre>

<h3>ZADANIE 3.9</h3>

<p>Mamy daną listę sekwencji (listy lub krotki)
różnej długości zawierających liczby. 
Znaleźć listę zawierającą sumy liczb z tych sekwencji.
Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)],
spodziewany wynik [0,4,3,7,18].

<pre>
</pre>

<h3>ZADANIE 3.10</h3>

<p>Stworzyć słownik tłumaczący liczby zapisane w systemie 
rzymskim (z literami I, V, X, L, C, D, M)
na liczby arabskie (podać kilka sposobów tworzenia takiego słownika).
Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].

<pre>
</pre>

</body>
</html>