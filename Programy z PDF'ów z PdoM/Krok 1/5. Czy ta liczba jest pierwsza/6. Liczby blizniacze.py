def pierwsza(n):
    pierwsza = n > 1
    d = 2
    while pierwsza and d * d <= n:
        if n % d == 0:
            pierwsza = False
        d += 1
    return pierwsza

licznik = 1
pary = int(input("Podaj liczbę par liczb bliźniaczych: "))

print("3", "5")
x = 5

while licznik < pary:
    if pierwsza(x) and pierwsza(x + 2):
        print(x, x + 2)
        licznik += 1
    x += 6