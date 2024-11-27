liczba = int(input("Podaj liczbę: "))

czynniki = []

d = 2

while liczba > 1:
    if liczba % d == 0:
        czynniki.append(d)
        liczba = liczba // d
    else:
        d += 1

print(f"Jest {len(czynniki)} czynników pierwszych: {czynniki}")