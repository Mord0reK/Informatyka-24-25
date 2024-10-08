# wyrazenie sumy n elementowej ciagu
n = int(input("Podaj n: "))

# Obliczenie sumy
suma = 0
for i in range(1, n + 1):
    suma += (2 * 3 * 2 ** (i - 1)) / i

print("Wynik:", suma)
