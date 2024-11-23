liczby = []

liczby.append(int(input("Podaj liczbę: ")))

while len(liczby) < 5:
    liczby.append(int(input("Podaj liczbę: ")))

print("Największa liczba to: ", max(liczby))