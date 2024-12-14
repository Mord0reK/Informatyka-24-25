plik = str(input("Podaj nazwę pliku: "))
klucz = int(input("Podaj klucz: "))

try:
     
    with open(plik, "r") as f:
            tekst = f.read()

            zaszyfrowany_tekst = ""

            for znak in tekst:
                if znak.isupper():
                    zaszyfrowany_tekst += chr((ord(znak) - ord('A') + klucz) % 26 + ord('A'))
                else:
                    zaszyfrowany_tekst += chr((ord(znak) - ord('a') + klucz) % 26 + ord('a'))
            print("Zaszyfrowany tekst:", zaszyfrowany_tekst)
except FileNotFoundError:
     print("Nie ma takiego pliku!")