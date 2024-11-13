liczba = int(input("Podaj liczbę: "))

for i in range(1, liczba):
    if liczba % i == 0:
        print(i)
        liczba //= i