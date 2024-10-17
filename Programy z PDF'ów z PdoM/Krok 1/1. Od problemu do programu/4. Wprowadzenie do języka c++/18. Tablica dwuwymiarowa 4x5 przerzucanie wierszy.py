tablica = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
]

wiersz = int(input("Podaj numer wiersza, który chcesz usunąć (1,4): "))

wiersz -= 1

tablica.pop(wiersz)
tablica.append([0, 0, 0, 0, 0])

for i in range(4):
    for j in range(5):
        print(tablica[i][j], end=" ")
    print()