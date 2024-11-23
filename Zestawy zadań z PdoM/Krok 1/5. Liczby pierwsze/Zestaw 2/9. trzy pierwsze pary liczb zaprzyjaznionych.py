def dzielniki(liczba):
    dzielniki = []
    for i in range(1, liczba):
        if liczba % i == 0:
            dzielniki.append(i)
    return sum(dzielniki)

def trzy_pierwsze_pary_zaprzyjaznione():
    pary = []
    n = 2
    while len(pary) < 3:
        suma1 = dzielniki(n)
        suma2 = dzielniki(suma1)
        # Sprawdzamy, czy liczby są zaprzyjaźnione
        if suma2 == n and n != suma1:
            pary.append((n, suma1))
        n += 1
    return pary

wynik = trzy_pierwsze_pary_zaprzyjaznione()

print("Trzy pierwsze pary liczb zaprzyjaźnionych to:")
for para in wynik:
    print(para)