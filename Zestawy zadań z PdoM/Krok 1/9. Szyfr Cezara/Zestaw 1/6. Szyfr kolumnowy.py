def szyfruj_tekst(tekst, klucz):
    # Usunięcie spacji i przekształcenie tekstu na wielkie litery
    tekst = tekst.replace(" ", "").upper()

    # Liczba kolumn to długość klucza
    liczba_kolumn = len(klucz)

    # Dodanie wypełnienia, jeśli tekst nie dzieli się równo na kolumny
    nadmiar = len(tekst) % liczba_kolumn
    if nadmiar != 0:
        tekst += 'X' * (liczba_kolumn - nadmiar)

    # Utworzenie siatki (wiersze = długość tekstu / liczba kolumn)
    liczba_wierszy = len(tekst) // liczba_kolumn
    siatka = [tekst[i * liczba_kolumn:(i + 1) * liczba_kolumn] for i in range(liczba_wierszy)]

    # Sortowanie klucza i określenie kolejności kolumn
    klucz_kolejnosc = sorted(range(len(klucz)), key=lambda k: klucz[k])

    # Odczyt tekstu według kolejności kolumn
    szyfrogram = ""
    for kolumna in klucz_kolejnosc:
        for wiersz in siatka:
            szyfrogram += wiersz[kolumna]

    return szyfrogram


# Przykład użycia
tekst = "PRZESYLKACZEKAWWILLI"
klucz = "40132"
szyfrogram = szyfruj_tekst(tekst, klucz)
print("Szyfrogram:", szyfrogram)
