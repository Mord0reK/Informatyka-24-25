alfabet = "aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż"
tekst = input("Podaj tekst: ")
klucz = int(input("Podaj klucz: "))

zaszyfrowany = ""

for znak in tekst:
    if znak in alfabet:
        pozycja = alfabet.index(znak)
        pozycja = (pozycja + klucz) % len(alfabet)
        zaszyfrowany += alfabet[pozycja]
    else:
        zaszyfrowany += znak

print(zaszyfrowany)