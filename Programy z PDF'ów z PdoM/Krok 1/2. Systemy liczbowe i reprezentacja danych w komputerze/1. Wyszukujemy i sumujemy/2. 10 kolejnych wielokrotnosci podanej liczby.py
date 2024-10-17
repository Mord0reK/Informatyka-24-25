# Napisz program wypisujący 10 kolejnych wielokrotności dodatniej liczby naturalnej wczytanej z klawiatury.

liczba = int(input("Podaj liczbę: "))

for i in range(2, 12):
    print(liczba * i)
