import string

try:
    with open("dane.txt", "r") as f:
        wejscie = f.read()
except FileNotFoundError:
    print("Nie znaleziono pliku wejsciowego!")

wyjscie = ""
klucz = 0

klucz = int(input("Podaj klucz: "))

for i in range(0, len(wejscie)):
    if wejscie[i] == " ":
        wyjscie = wyjscie + " "
    elif wejscie[i] >= 'A' and wejscie[i] <= 'Z':
        wyjscie += chr((ord(wejscie[i]) - ord('A') + klucz) % 26 + ord('A'))
    elif wejscie[i] >= 'a' and wejscie[i] <= 'z':
        wyjscie += chr((ord(wejscie[i]) - ord('a') + klucz) % 26 + ord('a'))

try:
    with open("wyjscie.txt", "w") as f:
        f.write(wyjscie)
        f.close()
except FileNotFoundError:
    print("Nie znaleziono pliku wyjsciowego!")



