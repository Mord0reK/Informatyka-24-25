liczby = []
while True:
    liczba = int(input("Podaj liczbę (0 kończy): "))
    if liczba == 0:
        break
    liczby.append(liczba)

liczby.reverse()
print("Liczby w odwrotnej kolejności:", liczby)
