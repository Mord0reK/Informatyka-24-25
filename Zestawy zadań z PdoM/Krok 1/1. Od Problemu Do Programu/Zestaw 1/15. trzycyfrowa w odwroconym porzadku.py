liczba = int(input("Podaj liczbę: "))

while liczba < 100 or liczba > 999 or liczba % 10 == 0:
    liczba = int(input("Podaj liczbę: "))

for i in range(3):
    print(liczba % 10, end="")
    liczba //= 10