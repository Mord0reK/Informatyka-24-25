napis1 = str(input("Podaj pierwszą liczbę: "))
napis2 = str(input("Podaj drugą liczbę: "))
napis3 = str(input("Podaj trzecią liczbę: "))

podstawa = int(input("Podaj podstawę systemu liczbowego: "))

suma = int(napis1, podstawa) + int(napis2, podstawa) + int(napis3, podstawa)

wynik = ""

while suma > 0:
    wynik = str(suma % podstawa) + wynik
    suma = suma // podstawa

print(wynik)
