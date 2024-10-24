n = int(input("Podaj liczbę do sprawdzenia czy jest pierwsza: "))

pierwsza = n > 2 and n % 2 != 0

d = 3

while pierwsza and d * d <= n:
    if n % d == 0:
        pierwsza = False
    d += 2

print("Liczba", n, "jest", "pierwsza" if pierwsza else "złożona")