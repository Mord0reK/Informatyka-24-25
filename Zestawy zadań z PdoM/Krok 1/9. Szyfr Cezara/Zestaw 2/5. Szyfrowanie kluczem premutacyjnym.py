import random

def permutacja():
    perm = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    perm = list(perm)
    for _ in range(100):
        j = random.randint(0, 25)  # Losowy indeks od 0 do 25
        k = random.randint(0, 25)  # Losowy indeks od 0 do 25

        perm[j], perm[k] = perm[k], perm[j]

    return ''.join(perm)

tekst = input("Podaj tekst do zaszyfrowania: ")
tekst = tekst.upper()

klucz = permutacja()

while len(klucz) < len(tekst):
    klucz += klucz

zaszyfrowany = ""

for i in range(len(tekst)):
    zaszyfrowany += klucz[i]

print("Zaszyfrowany tekst:", zaszyfrowany)