samogloski = ['a', 'e', 'i', 'o', 'u', 'y']

try:
    with open("wiadomosc.txt", "r") as plik:
        tekst = plik.read()

except FileNotFoundError:
    print("Nie znaleziono pliku")
    exit()

klucz1 = input("Podaj klucz dla samoglosek: ")
klucz2 = input("Podaj klucz dla spolglosek: ")

while len(klucz1) < len(tekst):
    klucz1 += klucz1

klucz1 = klucz1[:len(tekst)]

while len(klucz2) < len(tekst):
    klucz2 += klucz2

klucz2 = klucz2[:len(tekst)]


zaszyfrowany = ""

for i in range(len(tekst)):
    if tekst[i] in samogloski:
        zaszyfrowany = zaszyfrowany + klucz1[i]
    else:
        zaszyfrowany = zaszyfrowany + klucz2[i]

print("Tekst zaszyfrowany: ", zaszyfrowany)