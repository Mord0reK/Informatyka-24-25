tekst = str(input("Podaj tekst do zaszyfrowania: "))
klucz = int(input("Podaj klucz: "))

tekst.strip(" ")

zaszyfrowany = ""

for i in range(len(tekst)):
    if tekst[i] >= 'A' and tekst[i] <= 'Z':
        zaszyfrowany = zaszyfrowany + chr(ord(tekst[i]) + klucz)
    elif tekst[i] >= 'a':
        zaszyfrowany = zaszyfrowany + chr(ord(tekst[i]) + klucz)

print(zaszyfrowany)