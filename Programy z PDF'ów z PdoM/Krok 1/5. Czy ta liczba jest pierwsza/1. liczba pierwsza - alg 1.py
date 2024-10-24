n = int(input("Podaj liczbę do sprawdzenia czy jest pierwsza: "))

pierwsza = n > 1

d = 2

while pierwsza and d * d <= n:
    if n % d == 0:
        pierwsza = False
    d += 1

print("Liczba", n, "jest", "pierwsza" if pierwsza else "złożona")