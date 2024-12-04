def vigenere(tekst, klucz):
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    zaszyfrowany = ""

    for i in range(len(tekst)):
        if tekst[i] in alfabet:
            indeks_znak = alfabet.index(tekst[i])
            indeks_klucz = alfabet.index(klucz[i % len(klucz)])
            zaszyfrowany += alfabet[(indeks_znak + indeks_klucz) % 26]
        else:
            zaszyfrowany += tekst[i]

    return zaszyfrowany

tekst = input("Podaj tekst do zaszyfrowania: ").upper()
klucz = "VIGENERE"


print("Zaszyfrowany tekst:", vigenere(tekst, klucz))