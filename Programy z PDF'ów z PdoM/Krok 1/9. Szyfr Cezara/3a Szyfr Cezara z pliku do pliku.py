plik = str(input("Podaj nazwę pliku: "))
wyjscie = str(input("Podaj nazwę pliku wyjściowego: "))
klucz = int(input("Podaj klucz: "))

szyfrogram = ""

try:
    with open(plik, "r") as f:
        tekst = f.read()
        for znak in tekst:
            if znak == " ":
                szyfrogram += znak
            else:
                szyfrogram += chr(ord(znak) + klucz)

except FileNotFoundError:
    print("Nie ma takiego pliku")

with open(wyjscie, "w") as f:
    f.write(szyfrogram)
    print("Szyfrogram został zapisany do pliku: ", wyjscie)