tekst = str(input("Podaj tekst do zaszyfrowania: "))
klucz = int(input("Podaj klucz: "))

zaszyfrowany = ""

tekst = tekst.strip(" ")

for i in range(klucz):
    for j in range(i, len(tekst), klucz):
        zaszyfrowany = zaszyfrowany + tekst[j]

print(zaszyfrowany)