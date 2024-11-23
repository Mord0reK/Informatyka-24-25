import math

# Funkcja obliczająca liczbę różnych czynników pierwszych
def liczba_roznych_czynnikow_pierwszych(n):
    czynniki = []
    while n % 2 == 0:
        czynniki.append(2)
        n //= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            czynniki.append(i)
            n //= i

    if n > 2:
        czynniki.append(n)

    return len(czynniki)

liczba = int(input("Podaj liczbę całkowitą dodatnią: "))
wynik = liczba_roznych_czynnikow_pierwszych(liczba)

print(f"Liczba różnych czynników pierwszych liczby {liczba} to: {wynik}")
