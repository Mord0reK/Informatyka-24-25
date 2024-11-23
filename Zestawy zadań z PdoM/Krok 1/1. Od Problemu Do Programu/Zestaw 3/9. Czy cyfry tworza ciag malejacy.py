liczba = int(input("Podaj liczbę: "))

cyfry = []

while liczba > 0:
    cyfry.append(liczba % 10)
    liczba = liczba // 10

cyfry = cyfry[::-1]
lista = sorted(cyfry)
lista = lista[::-1]

if cyfry == lista:
    print("Tak")
else:
    print("Nie")