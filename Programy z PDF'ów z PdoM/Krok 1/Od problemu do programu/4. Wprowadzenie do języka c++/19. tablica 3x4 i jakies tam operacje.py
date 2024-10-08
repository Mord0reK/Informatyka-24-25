tablica = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

print("Wprowadź 12 liczb całkowitych do tablicy 3x4:")
for i in range(3):
    for j in range(4):
        tablica[i][j] = int(input(f"tablica[{i}][{j}]: "))

print("\nElementy tablicy 3x4:")
for i in range(3):
    for j in range(4):
        print(tablica[i][j], end=" ")
    print()

iloczyn = 1
for i in range(3):
    for j in range(4):
        if tablica[i][j] % 7 != 0:
            iloczyn *= tablica[i][j]

print(f"\nIloczyn elementów tablicy, które nie są podzielne przez 7: {iloczyn}")

licznik_dodatnich = 0
for i in range(3):
    for j in range(4):
        if i * j > 0:  # iloczyn indeksów jest dodatni
            licznik_dodatnich += 1

print(f"Liczba elementów o dodatnim iloczynie indeksów: {licznik_dodatnich}")

for i in range(3):
    for j in range(4):
        if tablica[i][j] > 4:
            print("Tak")
            exit()

print("Nie")
