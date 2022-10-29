# przypisujemy do istniejącej listy jedncześnie ją modyfikując
L = [3, 5, 4] ; L = L.sort()

# podaliśmy o jedną zmienną za mało przy rozpakowywaniu dostajemy ValueError
x, y = 1, 2, 3

# Stworzyliśmy krotkę, która jest obiektem immutable - nie możemy modyfikować jej zawartości,
X = 1, 2, 3 ; X[1] = 4

# Stworzyliśmy listę trzy elementową, w pythonie indeksujemy od '0', natomiast poniżej
# chcemy odwołać się do elementu o indeksie spoza listy, aby przypisać nową wartość
# na końcu listy należy użyć metody obj.append(val)
X = [1, 2, 3] ; X[3] = 4

# w pythonie 3 stringi są immutable, nie możemy modyfikować ich zawartości, można
# stworzyć nowy string za pomocą konkatenacji X + "d"
X = "abc" ; X.append("d")

# brakuje argumentów dla metody pow syntax jest następujący:
# pow(number, power, modulus [optional])
L = list(map(pow, range(8)))
