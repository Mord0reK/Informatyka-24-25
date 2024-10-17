podstawa = int(input("Podaj podstawę potęgi: "))
wykladnik = int(input("Podaj wykładnik potęgi: "))

tmp = podstawa
y = 1

while wykladnik > 0:
    if wykladnik % 2 == 1:
        y *= tmp
    wykladnik //= 2
    if wykladnik > 0:
        tmp *= tmp

print("Wynik:", y)