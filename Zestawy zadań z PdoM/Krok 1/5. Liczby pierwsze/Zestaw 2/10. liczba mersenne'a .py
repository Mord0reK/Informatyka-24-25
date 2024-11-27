def pierwsza(n):
    if n < 2 and n % 2 == 0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Funkcja obliczająca liczbę doskonałą na podstawie liczby Mersenne'a
def liczba_doskonala(p):
    m = 2**p - 1  # Liczba Mersenne'a
    if pierwsza(m):  # Jeśli liczba Mersenne'a jest pierwsza
        return 2**(p-1) * m  # Zwracamy liczbę doskonałą
    return None

def pierwsze_piec_liczb_doskonalych():
    doskonale = []
    p = 2  # Zaczynamy od liczby pierwszej 2
    while len(doskonale) < 5:
        liczba = liczba_doskonala(p)
        if liczba:
            doskonale.append(liczba)
        p += 1
    return doskonale

print("Pierwsze pięć liczb doskonałych to:", pierwsze_piec_liczb_doskonalych())
