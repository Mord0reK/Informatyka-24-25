a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

a_str = str(a)
b_str = str(b)

wyniki_mnozen = []

for i, cyfry in enumerate(reversed(b_str)):
    cyfra = int(cyfry)
    wynik = a * cyfra
    wyniki_mnozen.append(wynik * 10 ** i)

wynik = sum(wyniki_mnozen)

print(wyniki_mnozen, wynik)