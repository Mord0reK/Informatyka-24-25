liczba = int(input("Podaj liczbę: "))

cyfry = []

while liczba > 0:
    cyfry.append(liczba % 10)
    liczba = liczba // 10

if cyfry[0] == cyfry[-1]:
    print("Tak")
else:
    print("Nie")