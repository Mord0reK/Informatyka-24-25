
liczba1 = int(input("Podaj liczbę: "))

if liczba1 < 100 and liczba1 > 10:
    print(bin(liczba1)[2:], liczba1)

liczba2 = int(input("Podaj liczbę: "))
if liczba2 < 100 and liczba2 > 10:
    print(bin(liczba2)[2:], liczba2)

print("Suma: ", bin(liczba1 + liczba2)[2:])