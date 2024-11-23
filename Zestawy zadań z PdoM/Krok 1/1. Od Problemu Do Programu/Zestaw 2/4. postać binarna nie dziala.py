
liczba1 = int(input("Podaj liczbę: "))

if liczba1 < 100 and liczba1 > 10:
    print(bin(liczba1) + " " + str(liczba1))

liczba2 = int(input("Podaj liczbę: "))
if liczba2 < 100 and liczba2 > 10:
    print(bin(liczba2))

print(bin(liczba1 + liczba2))