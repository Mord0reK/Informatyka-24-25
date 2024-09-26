alfabet_m = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
alfabet_w = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSŚTUVWXYZŹŻ"

klucz = 0
jawny = ""
szyfrogram = ""

jawny = str(input("Podaj tekst do zaszyfrowania: "))
klucz = int(input("Podaj klucz: "))

for i in range(0, len(jawny)):
    litera = jawny[i]

    if litera in alfabet_m:
        nowy_indeks = (alfabet_m.find(litera) + klucz) % len(alfabet_m)
        szyfrogram += alfabet_m[nowy_indeks]
    elif litera in alfabet_w:
        nowy_indeks = (alfabet_w.find(litera) + klucz) % len(alfabet_w)
        szyfrogram += alfabet_w[nowy_indeks]
    else:
        szyfrogram += litera  # Jeśli znak nie jest w alfabecie (np. spacje, cyfry)

print("Zaszyfrowany tekst:", szyfrogram)
