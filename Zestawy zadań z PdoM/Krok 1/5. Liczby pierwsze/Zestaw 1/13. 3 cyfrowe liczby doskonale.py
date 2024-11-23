# Napisz program, który wyznaczy wszystkie trzycyfrowe liczby doskonałe. Liczba doskonała to liczba równa sumie
# swych dzielników różnych od niej samej, np. 28 = 1 + 2 + 4 + 7 + 14.

def dzielniki(liczba):
    dzielniki = []
    for i in range(1, liczba):
        if liczba % i == 0:
            dzielniki.append(i)
    if sum(dzielniki) == liczba:
        return True
    else:
        return False

for i in range(100, 999):
    if dzielniki(i):
        print(i)