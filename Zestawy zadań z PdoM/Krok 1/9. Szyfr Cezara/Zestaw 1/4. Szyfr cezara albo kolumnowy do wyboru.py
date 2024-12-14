def cezar(tekst, klucz):
    zaszyfrowany = ""
    for i in range(len(tekst)):
        zaszyfrowany = zaszyfrowany + chr(ord(tekst[i]) + klucz)
    return zaszyfrowany

def kolumnowy(tekst, klucz):
    zaszyfrowany = ""
    for i in range(klucz):
        for j in range(i, len(tekst), klucz):
            zaszyfrowany = zaszyfrowany + tekst[j]
    return zaszyfrowany


wybor = int(input("Podaj szyfr do wyboru: 1 - Szyfr Cezara, 2 - Szyfr kolumnowy: "))
tekst = str(input("Podaj tekst do zaszyfrowania (bez spacji): "))
klucz = int(input("Podaj klucz: "))

tekst.strip(" ")

if wybor == 1:
    print(f"Szyfrowanie Cezara: {cezar(tekst, klucz)}")
else:
    print("Szyfrowanie kolumnowe: ", kolumnowy(tekst, klucz))
