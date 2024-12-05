tekst = str(input("Podaj tekst do zaszyfrowania: "))
klucz = int(input("Podaj klucz: "))

zaszyfrowany_tekst = ""
for znak in tekst:
    zaszyfrowany_tekst += chr((ord(znak) - ord('A') + klucz) % 26 + ord('A'))

print("Zaszyfrowany tekst:", zaszyfrowany_tekst)