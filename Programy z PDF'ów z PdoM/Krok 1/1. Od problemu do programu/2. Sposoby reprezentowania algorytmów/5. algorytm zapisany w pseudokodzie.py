n = int(input("Podaj liczbę n: "))
suma = 0
liczba_1 = 1
liczba_2 = 0

for i in range(1, n+1):
    liczba_1 += n
    liczba_2 = 1
    for j in range(1, i+1):
        liczba_2 = liczba_2 * j
    suma += liczba_1 + liczba_2

print(suma)