podstawa = int(input("Podaj podstawę systemu liczbowego: "))
liczba = int(input("Podaj liczbę w systemie dziesiętnym: "))

wynik = ""

while liczba > 0:
    reszta = liczba % podstawa
    if reszta < 10:
        wynik = chr(ord('0') + reszta) + wynik
    else:
        wynik = chr('A' - 10 + reszta) + wynik
    liczba = liczba // podstawa

print("Liczba w systemie o podstawie", podstawa, "to:", wynik)