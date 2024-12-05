plik = str(input("Podaj nazwę pliku: "))
wyjscie = str(input("Podaj nazwę pliku wyjściowego: "))
klucz = int(input("Podaj klucz: "))

szyfrogram = ""

try:
    with open(plik, "r") as f:
        tekst = f.read()
        for i in range(len(tekst)):
            szyfrogram = chr(ord(tekst[i]) + klucz) + szyfrogram

except FileNotFoundError:
    print("Nie ma takiego pliku")

with open(wyjscie, "w") as f:
    f.write(szyfrogram)