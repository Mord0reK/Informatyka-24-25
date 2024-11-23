litery = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u","v", "w", "x", "y", "z"]

tekst = input("Podaj tekst: ")
licznik = 0

for i in range(0, 26):
    for j in range(0, len(tekst)):
        if tekst[j] == litery[i]:
            licznik += 1
    print(litery[i], ":", licznik)
    licznik = 0