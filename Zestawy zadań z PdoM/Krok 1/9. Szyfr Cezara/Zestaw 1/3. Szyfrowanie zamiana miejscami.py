tekst = str(input("Podaj tekst do zaszyfrowania: "))

for i in range(len(tekst)):
    print(tekst[i + 1], end="")
    print(tekst[i], end="")