m = int(input("Wprowadź liczbę wierszy (m): "))
n = int(input("Wprowadź liczbę kolumn (n): "))

tablica = [[0] * n for _ in range(m)]

print("Wprowadź elementy tablicy:")
for i in range(m):
    for j in range(n):
        tablica[i][j] = float(input(f"tablica[{i}][{j}]: "))

print("\nElementy tablicy:")
for i in range(m):
    for j in range(n):
        print(tablica[i][j], end=" ")
    print()

suma_nieparzystych = 0.0
for i in range(m):
    if (i + 1) % 2 != 0:  # Sprawdzanie, czy numer wiersza jest nieparzysty
        suma_nieparzystych += sum(tablica[i])

print(f"\nSuma elementów wierszy nieparzystych: {suma_nieparzystych}")

for i in range(m):
    for j in range(n):
        if tablica[i][j] < 0:
            tablica[i][j] -= 2

print("\nZmodyfikowana tablica (ujemne wartości zmniejszone o 2):")
for i in range(m):
    for j in range(n):
        print(tablica[i][j], end=" ")
    print()

for i in range(m):
    for j in range(n):
        if tablica[i][j] < 10:
            print("\nWszystkie elementy tablicy są mniejsze od 10.")
            exit()

print("\nNie wszystkie elementy tablicy są mniejsze od 10.")

