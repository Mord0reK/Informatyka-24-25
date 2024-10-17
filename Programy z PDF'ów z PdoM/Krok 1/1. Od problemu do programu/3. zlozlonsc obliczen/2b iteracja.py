# iteracja z tym dyzym E 
n = int(input("Podaj n: "))

# Obliczenie sumy
suma = 0
for i in range(1, n + 1):
    suma += 1 / (2 ** i)

print("Wynik:", suma)
