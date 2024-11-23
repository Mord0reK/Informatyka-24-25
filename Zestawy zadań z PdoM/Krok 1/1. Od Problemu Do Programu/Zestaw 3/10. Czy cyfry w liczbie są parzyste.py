liczba = int(input("Podaj liczbę: "))

cyfry = []

while liczba > 0:
    cyfry.append(liczba % 10)
    liczba = liczba // 10

parzysta = True

for cyfra in cyfry:
    if cyfra % 2 != 0:
        parzysta = False
        break

if parzysta:
    print("Tak")
else:
    print("Nie")