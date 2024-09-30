n = int(input("Podaj liczbę: "))

licznik_dzielnikow = 0

d = 2

while d * d <= n:
    if n % d == 0:
        licznik_dzielnikow += 2
    d += 1

if d * d == n:
    licznik_dzielnikow += 1

print(licznik_dzielnikow)