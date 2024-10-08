spr = False

def wczytaj_dane():
    global n, a, b
    while True:
        n = int(input("Podaj wartość n: "))
        a = int(input("Podaj wartość a: "))
        b = int(input("Podaj wartość b: "))

        if n >= 0 and a >= 0 and b >= 0:
            break
        else:
            print("Wartości muszą być nieujemne!")
            wczytaj_dane()


def suma_ciagu(n):
    suma = 0
    wyraz = -5
    for i in range(n):
        suma += wyraz
        wyraz /= 3
    return suma

def sprawdzenie(a, b):
    if 2 * a - b > 0:
        spr = True
    else:
        spr = False

def wyraz_ciagu(n):
    if n % 2 == 0:
        return (-1) ** (n // 2) * (n // 2)
    else:
        return 3 + ((n - 1) // 2) * (-4) ** ((n - 1) // 4)

wczytaj_dane()
print(suma_ciagu(n))
sprawdzenie(a, b)
print(spr)
wyraz = wyraz_ciagu(n)
print(n, "- ty wyraz ciągu wynosi: ", wyraz)