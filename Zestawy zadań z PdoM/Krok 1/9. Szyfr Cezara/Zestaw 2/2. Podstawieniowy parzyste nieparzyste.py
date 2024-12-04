tekst = input("Podaj tekst do zaszyfrowania: ")
klucz1 = input("Podaj klucz do zaszyfrowania liter o indeksie parzystym: ")
klucz2 = input("Podaj klucz do zaszyfrowania liter o indeksie nieparzystym: ")

zaszyfrowany = ""

while len(klucz1) < len(tekst):
    klucz1 += klucz1

klucz1 = klucz1[:len(tekst)]

while len(klucz2) < len(tekst):
    klucz2 += klucz2

klucz2 = klucz2[:len(tekst)]

# Szyfrowanie tekstu
for i in range(len(tekst)):
    if i % 2 == 0:  # Indeksy parzyste
        zaszyfrowany += klucz1[i]
    else:  # Indeksy nieparzyste
        zaszyfrowany += klucz2[i]

print("Zaszyfrowany tekst:", zaszyfrowany)
