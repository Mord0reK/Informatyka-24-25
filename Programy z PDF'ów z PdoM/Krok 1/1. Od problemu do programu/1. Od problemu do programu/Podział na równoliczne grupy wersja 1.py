n = int(input("Podaj liczbę: "))

licznik_dzielnikow = 0

for d in range(2, n):
    if n % d == 0:
        licznik_dzielnikow += 1

print(licznik_dzielnikow)