def znajdz_znak_zodiaku(dzien, miesiac):
    znaki_zodiaku = [
        ("Koziorożec", (1, 1), (1, 19)),
        ("Wodnik", (1, 20), (2, 18)),
        ("Ryby", (2, 19), (3, 20)),
        ("Baran", (3, 21), (4, 19)),
        ("Byk", (4, 20), (5, 20)),
        ("Bliźnięta", (5, 21), (6, 20)),
        ("Rak", (6, 21), (7, 22)),
        ("Lew", (7, 23), (8, 22)),
        ("Panna", (8, 23), (9, 22)),
        ("Waga", (9, 23), (10, 22)),
        ("Skorpion", (10, 23), (11, 21)),
        ("Strzelec", (11, 22), (12, 21)),
        ("Koziorożec", (12, 22), (12, 31)),
    ]

    for znak, poczatek, koniec in znaki_zodiaku:
        if (miesiac == poczatek[0] and dzien >= poczatek[1]) or (miesiac == koniec[0] and dzien <= koniec[1]):
            return znak

    return "Nieprawidłowa data"

dzien = int(input("Podaj dzień urodzenia (1-31): "))
miesiac = int(input("Podaj miesiąc urodzenia (1-12): "))
znak = znajdz_znak_zodiaku(dzien, miesiac)
print(f"Twój znak zodiaku to: {znak}")
