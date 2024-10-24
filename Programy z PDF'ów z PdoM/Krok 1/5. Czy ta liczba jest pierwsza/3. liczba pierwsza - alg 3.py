n = int(input("Podaj liczbę do sprawdzenia czy jest pierwsza: "))

pierwsza = n > 1

if n > 2 and n % 2 == 0:
    pierwsza = False
if n > 3 and n % 3 == 0:
    pierwsza = False

d = 5

while pierwsza and d * d <= n:
    if n % d == 0:
        pierwsza = False
    else:
        d += 2
    if n % d+2 == 0:
        pierwsza = False
    else:
        d += 6

print("Liczba", n, "jest", "pierwsza" if pierwsza else "złożona")