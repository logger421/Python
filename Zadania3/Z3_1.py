"""
Poniższa instrukcja jest poprawna python dopuszcza użycie średników
jednak jest ono niezalecane. Po wykonaniu result=3
"""
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

"""
Aby poniża instrukcja była poprawna można ją przerobić na dwa sposoby:
1) for i in "axby": print(i) if ord(i) < 100 else print("coś")
ale nie mamy dostępnego 'cosia' a w inline pętli for 'else' jest wymagany,
więc najprostszym sposobem jest zastosowanie wcięć:
for i in "axby":
    if ord(i) < 100:
        print(i)
w takiej formie else jest opcjonalny.
"""
for i in "axby": if ord(i) < 100: print (i)


"""
instrukcja jest poprawna
"""
for i in "axby": print (ord(i) if ord(i) < 100 else i)