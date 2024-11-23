def zrownowazony_trojkowy_na_dziesietny(liczba):
    dlugosc = len(liczba)
    dziesietna_wartosc = 0

    for i in range(dlugosc):
        if liczba[i] == '+':
            cyfra = 1
        elif liczba[i] == '0':
            cyfra = 0
        elif liczba[i] == '-':
            cyfra = -1
        else:
            raise ValueError("Nieprawidłowy znak w zrównoważonym systemie trójkowym")

        # Dodajemy do wyniku wartość cyfry razy 3 podniesione do odpowiedniej potęgi
        dziesietna_wartosc += cyfra * (3 ** (dlugosc - i - 1))

    return dziesietna_wartosc

liczba1 = input("Podaj pierwszą liczbę w zrównoważonym systemie trójkowym: ")
liczba2 = input("Podaj drugą liczbę w zrównoważonym systemie trójkowym: ")
zmieniona1, zmieniona2 = zrownowazony_trojkowy_na_dziesietny(liczba1), zrownowazony_trojkowy_na_dziesietny(liczba2)

print(f"Wynik: {zmieniona1 + zmieniona2}")
