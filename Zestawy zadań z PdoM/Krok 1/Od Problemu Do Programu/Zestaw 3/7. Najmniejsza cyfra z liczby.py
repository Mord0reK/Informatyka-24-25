liczba = int(input("Podaj liczbę: "))
cyfry = []

while liczba > 0:
    cyfry.append(liczba % 10)
    liczba //= 10

print("Najmniejsza cyfra to: ", min(cyfry))