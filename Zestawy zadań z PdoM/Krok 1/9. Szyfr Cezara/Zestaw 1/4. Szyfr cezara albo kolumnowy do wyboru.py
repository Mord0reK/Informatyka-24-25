def cezar(tekst, klucz):
    zaszyfrowany = ""
    for i in range(len(tekst)):
        zaszyfrowany = zaszyfrowany + chr(ord(tekst[i]) + klucz)
    return zaszyfrowany

def kolumnowy(tekst):
    kolumna1 = []
    kolumna2 = []
    for i in range(0, len(tekst), 2):
        kolumna1.append(tekst[i])
    for i in range(1, len(tekst), 2):
        kolumna2.append(tekst[i])
    for i in range(len(kolumna1)):
        print(kolumna1[i], end=" ")
    print()
    for i in range(len(kolumna2)):
        print(kolumna2[i], end=" ")

wybor = int(input("Podaj szyfr do wyboru: 1 - Szyfr Cezara, 2 - Szyfr kolumnowy: "))
tekst = str(input("Podaj tekst do zaszyfrowania (bez spacji): "))

if wybor == 1:
    klucz = int(input("Podaj klucz: "))

tekst.strip(" ")

if wybor == 1:
    print(f"Szyfrowanie Cezara: {cezar(tekst, klucz)}")
else:
    print("Szyfrowanie kolumnowe: ")
    kolumnowy(tekst)


