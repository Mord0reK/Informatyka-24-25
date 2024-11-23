# Napisz program, który wypisze najmniejszą liczbę pierwszą większą od podanej liczby całkowitej dodatniej

def pierwsza(liczba):
    if liczba < 2:
        return False
    for i in range(2, int(liczba ** 0.5) + 1):
        if liczba % i == 0:
            return False
    return True

liczba = int(input("Podaj liczbę: "))
liczba += 1

while not pierwsza(liczba):
    liczba += 1

print(liczba)