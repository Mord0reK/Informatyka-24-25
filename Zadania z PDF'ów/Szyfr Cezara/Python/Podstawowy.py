import string

jawny = ""
szyfrogram = ""
klucz = 0
kod = 0

jawny = str(input("Podaj tekst do zaszyfrowania: "))
klucz = int(input("Podaj klucz: "))

for i in range(0, len(jawny)):
    kod = ord(jawny[i]) + klucz
    if kod > ord('Z'):
        kod -= 26
    szyfrogram += chr(kod)

print(szyfrogram)