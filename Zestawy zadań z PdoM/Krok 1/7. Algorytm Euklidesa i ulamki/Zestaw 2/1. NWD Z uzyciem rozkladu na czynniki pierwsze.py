# Zapisz w postaci listy kroków algorytm znajdowania największego wspólnego dzielnika dwóch liczb całkowitych
# dodatnich z wykorzystaniem rozkładu liczb na czynniki pierwsze.

# Zrobione tak pokracznie

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

dzielniki_a = []
dzielniki_b = []

wspolne = []


def nwd(a, b):
    d = 2
    while a > 1:
        if a % d == 0:
            dzielniki_a.append(d)
            a = a // d
        else:
            d += 1

    d = 2

    while b > 1:
        if b % d == 0:
            dzielniki_b.append(d)
            b = b // d
        else:
            d += 1

    for i in range(len(dzielniki_a)):
        if dzielniki_a[i] in dzielniki_b:
            wspolne.append(dzielniki_a[i])
            dzielniki_b.remove(dzielniki_a[i])

    return wspolne

print(f"Największy wspólny dzielnik liczb {a} i {b} to {max(nwd(a, b))}")
