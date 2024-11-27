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

    return "".join(skompresowany) + f"{tekst[-1]}{licznik}"

tekst = str(input("Podaj tekst do skompresowania: "))
wynik = kompresuj_tekst(tekst)
print(f"Wynik dla '{tekst}': {wynik}")
