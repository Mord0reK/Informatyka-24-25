tekst = str(input("Podaj tekst do zaszyfrowania: "))
klucz = int(input("Podaj klucz: "))

tekst.strip(" ")

zaszyfrowany = ""

for i in range(len(tekst)):
    zaszyfrowany = zaszyfrowany + chr(ord(tekst[i]) + klucz)

print("Zaszyfrowany: ", zaszyfrowany)