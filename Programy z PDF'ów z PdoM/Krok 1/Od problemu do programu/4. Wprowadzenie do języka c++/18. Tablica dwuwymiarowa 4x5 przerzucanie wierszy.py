tablica = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

wiersz = int(input("Podaj numer wiersza, który chcesz usunąć (1,4): "))

wiersz -= 1

tablica.pop(wiersz)

for i in range(3):
    for j in range(4):
        print(tablica[i][j], end=" ")
    print()