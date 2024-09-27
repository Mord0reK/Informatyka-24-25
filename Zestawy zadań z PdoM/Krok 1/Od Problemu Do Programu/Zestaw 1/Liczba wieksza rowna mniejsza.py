a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

if a > b:
    print("Liczba", a, "jest większa od liczby", b)
elif a < b:
    print("Liczba", a, "jest mniejsza od liczby", b)
else:
    print("Liczby są sobie równe")