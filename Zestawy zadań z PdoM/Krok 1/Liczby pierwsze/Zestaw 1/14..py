#Wśród poniższych liczb są iloczyny dwóch liczb pierwszych nieparzystych. Napisz program zawierający funkcję
#sprawdz, która pozwoli znaleźć te liczby.
#1 838 947 883
#1 004 098 109
#851 260 967
#809 509 261
#669 266 311

import math

def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def sprawdz(liczba):
    for i in range(3, int(math.sqrt(liczba)) + 1, 2):
        if liczba % i == 0:
            dzielnik = i
            iloraz = liczba // dzielnik
            # Sprawdzamy, czy dzielnik i iloraz są liczbami pierwszymi
            if czy_pierwsza(dzielnik) and czy_pierwsza(iloraz):
                return dzielnik, iloraz
    return None

liczby = [
    1838947883,
    1004098109,
    851260967,
    809509261,
    669266311
]

for liczba in liczby:
    wynik = sprawdz(liczba)
    if wynik:
        print(f"Liczba {liczba} jest iloczynem dwóch liczb pierwszych: {wynik[0]} * {wynik[1]}")
    else:
        print(f"Liczba {liczba} nie jest iloczynem dwóch liczb pierwszych.")
