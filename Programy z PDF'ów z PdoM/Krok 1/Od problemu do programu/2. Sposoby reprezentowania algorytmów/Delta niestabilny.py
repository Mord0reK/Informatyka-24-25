from math import *

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

if a == 0:
    print("to nie jest równanie kwadratowe")
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print("równanie nie ma pierwiastków")
    elif delta == 0:
        x = -b / (2 * a)
        print(x)
    else:
        if b > 0:
            x1 = (-b - sqrt(delta)) / (2 * a)
            x2 = (-b + sqrt(delta)) / (2 * a)
            print(round(x1, 2), round(x2, 2))