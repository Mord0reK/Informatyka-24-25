import string

jawny = ""
szyfrogram = ""
klucz = 0

jawny = str(input("Podaj tekst do zaszyfrowania: "))
klucz = int(input("Podaj klucz: "))

for i in range(0, len(jawny)):
    if jawny[i] >= 'A' and jawny[i] <= 'Z':
        szyfrogram += chr((ord(jawny[i]) - ord('A') + klucz) % 26 + ord('A'))
    elif jawny[i] >= 'a' and jawny[i] <= 'z':
        szyfrogram += chr((ord(jawny[i]) - ord('a') + klucz) % 26 + ord('a'))

print(szyfrogram)