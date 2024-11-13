import math

a = int(input("Podaj początek przedziału: "))
b = int(input("Podaj koniec przedziału: "))

liczby = []

for i in range(a ** 2, b ** 2 + 1):
    liczby.append(int(math.sqrt(i ** 2)))

print(liczby)