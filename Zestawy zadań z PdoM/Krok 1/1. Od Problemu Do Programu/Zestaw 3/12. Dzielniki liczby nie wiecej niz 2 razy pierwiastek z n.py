import math

n = int(input("Podaj liczbę: "))
dzielniki = []

for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        dzielniki.append(i)
        dzielniki.append(n // i)

dzielniki = sorted(dzielniki)
print(dzielniki)