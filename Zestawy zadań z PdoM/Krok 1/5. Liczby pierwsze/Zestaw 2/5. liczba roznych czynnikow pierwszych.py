import math

# Funkcja obliczająca liczbę różnych czynników pierwszych
def liczba_roznych_czynnikow_pierwszych(n):
    czynniki = []

    d = 2

    while n > 1:
        if n % d == 0:
            czynniki.append(d)
            n //= d
        else:
            d += 1

    return czynniki

liczba = int(input("Podaj liczbę całkowitą dodatnią: "))
wynik = liczba_roznych_czynnikow_pierwszych(liczba)

unikalne = []

for i in range(len(wynik)):
    if wynik[i] not in unikalne:
        unikalne.append(wynik[i])

print(unikalne)

print(f"Liczba różnych czynników pierwszych liczby {liczba} to: {len(unikalne)}")
