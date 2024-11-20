a = input("Podaj pierwszą liczbę: ")
b = input("Podaj drugą liczbę: ")
podstawa = int(input("Podaj podstawę systemu: "))

# Krok1: Ustal wartość początkową wyniku c na napis pusty
c = ""

# Krok2: Ustal wartość początkową zmiennej pozyczka na fałsz
pozyczka = False

# Krok3: Uzupełnij odjemnik zerami nieznaczącymi tak, aby liczba cyfr w odjemniku była taka sama jak liczba cyfr odjemnej
while len(a) < len(b):
    a = "0" + a
while len(b) < len(a):
    b = "0" + b

# Krok4: Dla każdej z cyfr odjemnej i odjemnika, traktowanych jako liczby jednocyfrowe, w kolejności od prawej do lewej wykonaj kroki 5 – 12
for i in range(len(a) - 1, -1, -1):
    # Krok5: Jeśli zmienna pozyczka ma wartość prawda, wykonaj Krok: 6
    if pozyczka:
        # Krok6: Odejmij od cyfry odjemnej 1
        if a[i] <= '9':
            cyfra_odjemna = ord(a[i]) - 48 - 1
        else:
            cyfra_odjemna = ord(a[i]) - 55 - 1
        # Krok7: Ustal wartość zmiennej pozyczka na fałsz
        pozyczka = False
    else:
        if a[i] <= '9':
            cyfra_odjemna = ord(a[i]) - 48
        else:
            cyfra_odjemna = ord(a[i]) - 55

    if b[i] <= '9':
        cyfra_odjemnik = ord(b[i]) - 48
    else:
        cyfra_odjemnik = ord(b[i]) - 55

    # Krok8: Oblicz różnicę cyfr odjemnej i odjemnika
    roznica = cyfra_odjemna - cyfra_odjemnik

    # Krok9: Jeśli różnica jest ujemna, to wykonaj kroki 10 – 11
    if roznica < 0:
        # Krok10: Ustal wartość zmiennej pozyczka na prawda
        pozyczka = True
        # Krok11: Do różnicy dodaj podstawę systemu
        roznica += podstawa

    # Krok12: Dołącz cyfrę różnicy do wyniku
    if roznica < 10:
        c = chr(roznica + 48) + c
    else:
        c = chr(roznica + 55) + c

c = c.lstrip("0")


print("Wynik odejmowania: ", c)