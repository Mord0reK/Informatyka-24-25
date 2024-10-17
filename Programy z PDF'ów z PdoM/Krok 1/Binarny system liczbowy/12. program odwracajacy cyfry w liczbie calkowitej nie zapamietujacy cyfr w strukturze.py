liczba = int(input("Podaj liczbę: "))
odwrocona = 0
while liczba > 0:
    odwrocona = odwrocona * 10 + liczba % 10
    liczba //= 10
print("Odwrotna kolejność cyfr:", odwrocona)
