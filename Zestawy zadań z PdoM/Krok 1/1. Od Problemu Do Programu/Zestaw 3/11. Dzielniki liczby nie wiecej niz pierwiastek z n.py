liczba = int(input("Podaj liczbę: "))

d = 1
dzielniki = []

while d * d <= liczba:
    if liczba % d == 0:
        dzielniki.append(d)
        if d * d != liczba:
            dzielniki.append(liczba // d)
    d += 1

print("Dzielniki liczby to:", sorted(dzielniki))