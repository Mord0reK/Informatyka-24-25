def czworkowy(liczba):
    czworkowy = ""
    while liczba > 0:
        czworkowy = str(liczba % 4) + czworkowy
        liczba //= 4
    return czworkowy

binarna = input("Podaj liczbę binarną: ")

print(czworkowy(int(binarna, 2)))
print(oct(int(binarna, 2))[2:])
print(hex(int(binarna, 2))[2:].upper())