liczba = int(input("Podaj liczbę: "))

potega = 0

while 2 ** potega < liczba:
    potega += 1

potega -= 1

print(2 ** potega)