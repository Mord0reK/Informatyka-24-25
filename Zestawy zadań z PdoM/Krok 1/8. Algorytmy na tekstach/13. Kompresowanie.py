def kompresuj_tekst(tekst):
    if not tekst:
        return tekst  # Jeśli tekst jest pusty, zwróć go od razu

    skompresowany = []
    licznik = 1

    for i in range(1, len(tekst)):
        if tekst[i] == tekst[i - 1]:
            licznik += 1
            if licznik > 9:
                skompresowany.append(f"{tekst[i - 1]}9")
                licznik = 1
        else:
            skompresowany.append(f"{tekst[i - 1]}{licznik}")
            licznik = 1

    # Dodaj ostatni znak i jego licznik
    skompresowany.append(f"{tekst[-1]}{licznik}")

    skompresowany_tekst = ''.join(skompresowany)

    # Jeśli wynikowy tekst jest dłuższy, zwróć oryginał
    return skompresowany_tekst if len(skompresowany_tekst) < len(tekst) else tekst

tekst = str(input("Podaj tekst do skompresowania: "))
wynik = kompresuj_tekst(tekst)
print(f"Wynik dla '{tekst}': {wynik}")
