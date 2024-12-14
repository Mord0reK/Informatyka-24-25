tekst = str(input("Podaj tekst do zaszyfrowania: "))
klucz = int(input("Podaj klucz: "))

zaszyfrowany_tekst = ""

for znak in tekst:
    if znak.isalpha():
        if znak.islower():
            zaszyfrowany_tekst += chr((ord(znak) - ord('a') + klucz) % 26 + ord('a'))
        elif znak.isupper():
            zaszyfrowany_tekst += chr((ord(znak) - ord('A') + klucz) % 26 + ord('A'))
    else:
        zaszyfrowany_tekst += znak

print("Zaszyfrowany tekst:", zaszyfrowany_tekst)