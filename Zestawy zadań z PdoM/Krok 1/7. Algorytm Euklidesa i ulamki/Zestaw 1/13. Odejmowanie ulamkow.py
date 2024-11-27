def NWD(a,b):
    while b:
        a, b = b, a % b
    return a

def NWW(a,b):
    return a * b // NWD(a,b)

def roznica(ulamek1, ulamek2):
    wynik = [0, 0]

    wspolny_mianownik = NWW(ulamek1[1], ulamek2[1])

    ulamek1[0] = ulamek1[0] * wspolny_mianownik // ulamek1[1]
    ulamek2[0] = ulamek2[0] * wspolny_mianownik // ulamek2[1]

    ulamek1[1], ulamek2[1] = wspolny_mianownik, wspolny_mianownik

    wynik[0] = ulamek1[0] - ulamek2[0]
    wynik[1] = wspolny_mianownik

    return wynik

ulamek1 = [int(input("Podaj licznik 1: ")), int(input("Podaj mianownik 1: "))]
ulamek2 = [int(input("Podaj licznik 2: ")), int(input("Podaj mianownik 2: "))]

wynik = roznica(ulamek1, ulamek2)

print(f"Wynik: {wynik[0]}/{wynik[1]}")