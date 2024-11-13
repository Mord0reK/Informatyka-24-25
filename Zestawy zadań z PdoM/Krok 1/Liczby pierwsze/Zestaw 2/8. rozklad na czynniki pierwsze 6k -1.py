import math

def rozloz_na_czynniki_pierwsze(n):
    czynniki = []

    while n % 2 == 0:
        czynniki.append(2)
        n //= 2

    while n % 3 == 0:
        czynniki.append(3)
        n //= 3

    i = 5
    while i * i <= n:
        if n % i == 0:
            czynniki.append(i)
            n //= i
        elif n % (i + 2) == 0:
            czynniki.append(i + 2)
            n //= (i + 2)
        else:
            i += 6

    if n > 2:
        czynniki.append(n)
    return czynniki

liczba = int(input("Podaj liczbę całkowitą dodatnią: "))
czynniki = rozloz_na_czynniki_pierwsze(liczba)

print(f"Rozkład liczby {liczba} na czynniki pierwsze: {czynniki}")
