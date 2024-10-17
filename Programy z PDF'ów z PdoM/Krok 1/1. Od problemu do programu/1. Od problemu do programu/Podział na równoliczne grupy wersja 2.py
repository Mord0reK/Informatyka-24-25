n = int(input("Podaj liczbę: "))
d = 2
licznik_dzielnikow = 0

dd = int(n**0.5) + 1

for d in range(2, dd):
    if n % d == 0:
        licznik_dzielnikow += 2

if d*d == n:
    licznik_dzielnikow += 1

print(licznik_dzielnikow)