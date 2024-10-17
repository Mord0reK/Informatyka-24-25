tablica = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

for i in range(5):
    for j in range(5):
        tablica[i][j] = float(input(f"Podaj liczbę na pozycji [{i}][{j}]: "))

for j in range(5):
    kolumna = [tablica[i][j] for i in range(5)]
    kolumna.sort(reverse=True)
    for i in range(5):
        tablica[i][j] = kolumna[i]

min_values = []
min_counts = []

wiersz_2 = tablica[2][:]
for i in range(5):
    tablica[2][i] = tablica[i][2]
    tablica[i][2] = wiersz_2[i]

print("\nPosortowana tablica:")
for i in range(5):
    for j in range(5):
        print(tablica[i][j], end=" ")
    print()

for i in range(5):
    min_value = min(tablica[i])
    min_count = tablica[i].count(min_value)
    min_values.append(min_value)
    min_counts.append(min_count)

print("\nMinimum dla każdego wiersza i liczba ich wystąpień:")
for i in range(5):
    print(f"Wiersz {i}: minimum = {min_values[i]}, liczba wystąpień = {min_counts[i]}")