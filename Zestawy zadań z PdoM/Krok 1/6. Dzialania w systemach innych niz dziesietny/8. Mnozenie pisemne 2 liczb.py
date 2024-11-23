def dodaj_pisemnie(a, b, podstawa) -> str:
    while len(a) < len(b):
        a = "0" + a
    while len(b) < len(a):
        b = "0" + b

    wynik = []
    przeniesienie = 0

    for i in range(len(a) - 1, -1, -1):
        suma = int(a[i]) + int(b[i]) + przeniesienie
        wynik.append(str(suma % podstawa))
        przeniesienie = suma // podstawa

    if przeniesienie > 0:
        wynik.append(str(przeniesienie))

    return ''.join(reversed(wynik))


def pisemne_mnozenie(a, b, podstawa) -> str:
    if podstawa < 2 or podstawa > 10:
        raise ValueError("Podstawa musi być w zakresie od 2 do 10.")

    wynik = "0"

    # Iterujemy przez cyfry mnożnika od końca.
    for i in range(len(b) - 1, -1, -1):
        cyfra = int(b[i])

        # Mnożenie przez jedną cyfrę.
        czesciowy_wynik = []
        przeniesienie = 0

        for j in range(len(a) - 1, -1, -1):
            iloczyn = int(a[j]) * cyfra + przeniesienie
            czesciowy_wynik.append(str(iloczyn % podstawa))
            przeniesienie = iloczyn // podstawa

        if przeniesienie > 0:
            czesciowy_wynik.append(str(przeniesienie))

        czesciowy_wynik.reverse()

        # Dodajemy zera na końcu dla przesunięcia miejsca dziesiętnego.
        czesciowy_wynik = ''.join(czesciowy_wynik) + '0' * (len(b) - 1 - i)

        wynik = dodaj_pisemnie(wynik, czesciowy_wynik, podstawa)

    return wynik

a = input("Podaj pierwsza liczba: ")
b = input("Podaj druga liczba: ")
podstawa = int(input("Podaj podstawę systemu liczbowego (od 2 do 10): "))

try:
    wynik = pisemne_mnozenie(a, b, podstawa)
    print(f"Wynik mnożenia: {wynik}")
except ValueError as e:
    print(f"Błąd: {e}")
