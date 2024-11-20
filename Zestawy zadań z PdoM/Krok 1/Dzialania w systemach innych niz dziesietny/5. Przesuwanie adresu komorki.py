szesnastkowa = input("Podaj liczbe szesnastkowa: ")
przesuniecie = int(input("Podaj przesuniecie: "))

szesnastkowa = int(szesnastkowa, 16) + przesuniecie

print("Wynik przesunięcia: ", hex(szesnastkowa)[2:].upper())