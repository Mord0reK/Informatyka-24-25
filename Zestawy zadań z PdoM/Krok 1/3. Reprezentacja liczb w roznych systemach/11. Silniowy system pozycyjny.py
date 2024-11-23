import math

def silniowy_system(x):
    wynik = []

    # Zaczynamy od jak najwyższej silni, która jest mniejsza lub równa x
    n = 1
    while math.factorial(n) <= x:
        n += 1

    for i in range(n - 1, 0, -1):
        # Obliczamy współczynnik dla i!
        wspolczynnik = x // math.factorial(i)
        wynik.append(str(wspolczynnik))

        # Odejmujemy część już przetworzoną
        x -= wspolczynnik * math.factorial(i)

    return ''.join(wynik)

x = int(input("Podaj liczbę dziesiętną (0 ≤ x ≤ 3 628 799): "))

print(f"Liczba w silniowym systemie pozycyjnym: {silniowy_system(x)}")
