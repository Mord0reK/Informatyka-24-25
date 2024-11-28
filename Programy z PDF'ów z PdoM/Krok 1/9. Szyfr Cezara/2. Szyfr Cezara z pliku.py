plik = str(input("Podaj nazwę pliku: "))

try:
    with open(plik, "r") as f:
        tekst = f.read()
        for i in range(len(tekst)):
            print(chr(ord(tekst[i]) + 1), end="")

except FileNotFoundError:
    print("Nie ma takiego pliku")