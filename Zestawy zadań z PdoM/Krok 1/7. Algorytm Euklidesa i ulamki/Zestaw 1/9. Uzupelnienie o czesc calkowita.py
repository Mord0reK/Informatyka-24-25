# Uzupełnij program Suma ułamków o wyodrębnianie części całkowitej i części ułamkowej dla sumy, która jest
# ułamkiem niewłaściwym.


def NWD(a,b):
    while b:
        a, b = b, a % b
    return a

def nww(a, b):
    """Oblicza najmniejszą wspólną wielokrotność (NWW) dwóch liczb."""
    return abs(a * b) // NWD(a, b)


def dodaj_ulamki(ulamek1, ulamek2, ulamek3):
    """Dodaje trzy ułamki."""
    licznik1, mianownik1 = ulamek1
    licznik2, mianownik2 = ulamek2
    licznik3, mianownik3 = ulamek3

    wspolny_mianownik = nww(nww(mianownik1, mianownik2), mianownik3)

    licznik1 *= wspolny_mianownik // mianownik1
    licznik2 *= wspolny_mianownik // mianownik2
    licznik3 *= wspolny_mianownik // mianownik3

    suma_licznikow = licznik1 + licznik2 + licznik3

    # Skrócenie wyniku
    nwd = NWD(suma_licznikow, wspolny_mianownik)
    licznik = suma_licznikow // nwd
    mianownik = wspolny_mianownik // nwd

    return licznik, mianownik

ulamek1 = (int(input("Podaj licznik pierwszego ulamka: ")), int(input("Podaj mianownik pierwszego ulamka: ")))
ulamek2 = (int(input("Podaj licznik drugiego ulamka: ")), int(input("Podaj mianownik drugiego ulamka: ")))
ulamek3 = (int(input("Podaj licznik trzeciego ulamka: ")), int(input("Podaj mianownik trzeciego ulamka: ")))

wynik = dodaj_ulamki(ulamek1, ulamek2, ulamek3)

if wynik[0] >= wynik[1]:
    print(f"Wynik: {wynik[0] // wynik[1]} {wynik[0] % wynik[1]}/{wynik[1]}")
else:
    print(f"Wynik: {wynik[0]}/{wynik[1]}")