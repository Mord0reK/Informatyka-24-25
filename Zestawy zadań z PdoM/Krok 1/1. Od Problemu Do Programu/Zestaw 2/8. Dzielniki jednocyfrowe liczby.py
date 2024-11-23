liczba = int(input("Podaj liczbę: "))
dzielniki = []

for i in range(1, 10):
    if liczba % i == 0:
        dzielniki.append(i)

for i in range(len(dzielniki)):
    if i == len(dzielniki) - 1:
        print(dzielniki[i])
    else:
        print(dzielniki[i], end=",")