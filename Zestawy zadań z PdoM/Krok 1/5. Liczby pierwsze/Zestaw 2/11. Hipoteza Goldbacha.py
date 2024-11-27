def pierwsza(n):
    if n < 2 and n % 2 == 0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Funkcja sprawdzająca hipotezę Goldbacha dla liczby n
def sprawdz_goldbacha(n):
    if n % 2 != 0 or n <= 2:  # Hipoteza Goldbacha dotyczy tylko liczb parzystych > 2
        return False

    for i in range(2, n):
        if pierwsza(i) and pierwsza(n - i):
            return True, i, n - i  # Zwraca True i parę liczb pierwszych

    return False, None, None  # Jeśli nie znaleziono takiej pary

n = int(input("Podaj liczbę: "))

wynik, p1, p2 = sprawdz_goldbacha(n)
if wynik:
    print(f"Liczba {n} jest sumą dwóch liczb pierwszych: {p1} + {p2}")
else:
    print(f"Liczba {n} nie spełnia hipotezy Goldbacha")
