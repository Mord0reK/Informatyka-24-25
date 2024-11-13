import math

def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Funkcja sprawdzająca, czy liczba jest półpierwsza
def czy_liczba_polpierwsza(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            dzielnik1 = i
            dzielnik2 = n // i

            if czy_pierwsza(dzielnik1) and czy_pierwsza(dzielnik2):
                return True
    return False

liczba = int(input("Podaj liczbę całkowitą dodatnią: "))

if czy_liczba_polpierwsza(liczba):
    print("TAK")
else:
    print("NIE")
