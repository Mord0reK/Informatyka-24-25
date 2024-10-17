tablica = [[i + j for j in range(6)] for i in range(5)]

print("Początkowa tablica:")

for wiersz in tablica:
    print(" ".join(map(str, wiersz)))

for i in range(5):
    tablica[i][1], tablica[i][2] = tablica[i][2], tablica[i][1]

print("\nTablica po zamianie kolumn 1 i 2:")

for wiersz in tablica:
    print(" ".join(map(str, wiersz)))

wiersz1 = int(input("\nPodaj pierwszy numer wiersza do zamiany (0-4): "))
wiersz2 = int(input("Podaj drugi numer wiersza do zamiany (0-4): "))

tablica[wiersz1], tablica[wiersz2] = tablica[wiersz2], tablica[wiersz1]

print(f"\nTablica po zamianie wierszy {wiersz1} i {wiersz2}:")

for wiersz in tablica:
    print(" ".join(map(str, wiersz)))
