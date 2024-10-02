# Specyfikacja
# Dane: Liczba n; n > 0
# Wynik: Suma cyfr liczby n

suma = 0
liczba = int(input("Podaj liczbę: "))

while liczba > 0:
    cyfra = liczba % 10
    suma += cyfra
    liczba = liczba // 10

print("Suma cyfr wynosi:", suma)
