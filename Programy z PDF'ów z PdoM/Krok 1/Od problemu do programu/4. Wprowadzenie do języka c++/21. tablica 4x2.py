tablica = [
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

iloczyn = 1
licznik = 0
istnieje = False
for i in range(2):
    for j in range(4):
        tablica[i][j] = int(input(f"Podaj wartość dla tablica[{i}][{j}]: "))

for i in range(2):
    for j in range(4):
        if tablica[i][j] % 3 == 0:
            iloczyn *= tablica[i][j]
        if tablica[i][j] != 0:
            licznik += 1
        if tablica[i][j] > 20:
            istnieje = True

if istnieje:
    istnieje = "Istnieje"
else:
    istnieje = "Nie istnieje"

print("Iloczyn liczb podzielnych przez 3: ", iloczyn)
print("Liczba niezerowych elementów: ", licznik)
print("Czy istnieje element większy od 20: ", istnieje)

