def podzielnosc(liczba):
    if liczba % 3 == 0:
        if liczba % 7 == 0:
            return True
    return False

liczba = int(input("Podaj liczbę do testu podzielności przez 3 i 7: "))

if podzielnosc(liczba):
    print(f"{liczba} jest podzielna przez 3 i 7.")
else:
    print(f"{liczba} nie jest podzielna przez 3 i 7.")