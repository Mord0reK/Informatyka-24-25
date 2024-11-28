tekst = str(input("Podaj tekst do zaszyfrowania: "))
klucz = int(input("Podaj klucz: "))

for i in range(len(tekst)):
    print(chr(ord(tekst[i]) + klucz), end="")

