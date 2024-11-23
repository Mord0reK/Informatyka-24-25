liczba = int(input("Podaj liczbę: "))

while liczba != 0:
    print(liczba % 10, end="")
    liczba //= 10