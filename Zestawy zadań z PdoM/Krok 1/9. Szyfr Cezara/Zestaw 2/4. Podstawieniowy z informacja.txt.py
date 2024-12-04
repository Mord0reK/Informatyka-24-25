try:
    with open("informacja.txt", "r") as f:
        tekst = f.read()
        tekst = tekst.strip(" ")
except FileNotFoundError:
    print("Nie ma pliku informacja.txt")
    exit()

klucz = str(input("Podaj klucz: "))
zaszyfrowany = ""

while len(klucz) < len(tekst):
    klucz += klucz

klucz = klucz[:len(tekst)]

for i in range(len(tekst)):
    zaszyfrowany = zaszyfrowany + chr(ord(tekst[i]) + int(klucz[i]))

print(zaszyfrowany)