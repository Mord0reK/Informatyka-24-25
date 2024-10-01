cyfry = []

liczba = int(input("Podaj liczbę: "))

for i in range(len(str(liczba))):
    cyfry.append(liczba % 10)
    liczba //= 10

print(cyfry)