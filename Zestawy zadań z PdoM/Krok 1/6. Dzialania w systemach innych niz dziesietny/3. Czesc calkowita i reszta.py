liczba1 = "100000000"
liczba2 = "11"

calkowita = bin(int(liczba1, 2) // int(liczba2, 2))[2:]

reszta = bin(int(liczba1, 2) % int(liczba2, 2))[2:]

print(f"Część całkowita z dzielenia {liczba1} przez {liczba2} to: {calkowita} reszty {reszta}")