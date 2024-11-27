# Dwie liczby uważa się za zaprzyjaźnione, jeśli sumy dzielników właściwych tych liczb są równe.


def dzielniki(liczba):
    dzielniki = []
    for i in range(1, liczba):
        if liczba % i == 0:
            dzielniki.append(i)
    return sum(dzielniki)

def zaprzyjaznione(limit):
    zaprzyjaznione = []
    suma_dzielnikow = {}

    for i in range(2, limit):
        suma_dzielnikow[i] = dzielniki(i)

    for a in range(2, limit):
        b = suma_dzielnikow.get(a, 0)
        if a < b < limit:
            if suma_dzielnikow.get(b, 0) == a:
                zaprzyjaznione.append((a, b))
    return zaprzyjaznione

limit = 1_000_000
wynik = zaprzyjaznione(limit)

print("Pary liczb zaprzyjaźnionych mniejszych niż milion:")
for para in wynik:
    print(para)