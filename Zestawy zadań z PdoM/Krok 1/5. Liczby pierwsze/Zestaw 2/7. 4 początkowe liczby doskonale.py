def dzielniki(liczba):
    dzielniki = []
    for i in range(1, liczba):
        if liczba % i == 0:
            dzielniki.append(i)
    return sum(dzielniki)

n = 2
licznik = 0

while licznik < 4:
    if dzielniki(n) == n:
        print(n)
        licznik += 1
    n += 1
