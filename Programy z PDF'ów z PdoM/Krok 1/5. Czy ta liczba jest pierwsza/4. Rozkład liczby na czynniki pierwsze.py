n = int(input("Podaj liczbę do rozłożenia na czynniki pierwsze: "))

d = 2

czynniki = []

while n > 1:
    if n % d == 0:
        czynniki.append(d)
        n = n // d
    else:
        d += 1

for i in range(len(czynniki)):
    if i == len(czynniki) - 1:
        print(czynniki[i])
    else:
        print(czynniki[i], end=" * ")