def dzielniki(liczba):
    dzielniki = []
    for i in range(1, liczba):
        if liczba % i == 0:
            dzielniki.append(i)
    return dzielniki

liczba1 = int(input("Podaj pierwszą liczbę 6-cio cyfrową: "))
liczba2 = int(input("Podaj drugą liczbę 6-cio cyfrową: "))

while liczba1 < 100000 or liczba2 < 100000 or liczba1 > 999999 or liczba2 > 999999:
    print("Podano nieprawidłowe liczby!")
    liczba1 = int(input("Podaj pierwszą liczbę 6-cio cyfrową: "))
    liczba2 = int(input("Podaj drugą liczbę 6-cio cyfrową: "))

print(f"Liczba {liczba1} ma {len(dzielniki(liczba1))} dzielników własciwych.")
print(f"Liczba {liczba2} ma {len(dzielniki(liczba2))} dzielników własciwych.")

if len(dzielniki(liczba1)) > len(dzielniki(liczba2)):
    print("Gracz 1 wygrywa")
else:
    print("Gracz 2 wygrywa")