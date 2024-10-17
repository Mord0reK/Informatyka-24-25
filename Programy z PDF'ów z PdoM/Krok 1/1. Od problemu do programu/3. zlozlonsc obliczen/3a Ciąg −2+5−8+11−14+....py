def ciag_a(n):
    suma = 0
    for i in range(1, n + 1):
        wyraz = (-1) ** (i + 1) * (3 * i - 1)
        suma += wyraz
    return suma

# Przykładowe użycie
n = int(input("Podaj n: "))
print("Suma pierwszych", n, "wyrazów ciągu:", ciag_a(n))
