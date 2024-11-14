def dodaj(a, b, podstawa):
    przn = 0
    c = ""
    while len(a) < len(b):
        a = "0" + a

    while len(b) < len(a):
        b = "0" + b

    for i in range(len(a) - 1, -1, -1):
        if a[i] <= '9':
            cyfra1 = ord(a[i]) - 48
        else:
            cyfra1 = ord(a[i]) - 55  # Adjust for characters A-F

        if b[i] <= '9':
            cyfra2 = ord(b[i]) - 48
        else:
            cyfra2 = ord(b[i]) - 55  # Adjust for characters A-F

        suma = przn + cyfra1 + cyfra2
        przn = suma // podstawa
        suma = suma % podstawa

        if suma < 10:
            c = chr(suma + 48) + c
        else:
            c = chr(suma + 55) + c  # Adjust for characters A-F

    if przn > 0:
        if przn < 10:
            c = chr(przn + 48) + c
        else:
            c = chr(przn + 55) + c
    return c

def MnozPrzezCyfre(cyfra, liczba, podstawa):
    wynik = ""
    przeniesienie = 0
    cyfra = int(cyfra)
    for i in range(len(liczba) - 1, -1, -1):
        if liczba[i] <= '9':
            cyfra_liczba = ord(liczba[i]) - 48
        else:
            cyfra_liczba = ord(liczba[i]) - 55  # Adjust for characters A-F

        iloczyn = cyfra * cyfra_liczba + przeniesienie
        przeniesienie = iloczyn // podstawa
        wynik = chr(iloczyn % podstawa + 48) + wynik
    if przeniesienie > 0:
        wynik = chr(przeniesienie + 48) + wynik
    return wynik

c = "0"

a = str(input("Podaj pierwsza liczbe: "))
b = str(input("Podaj druga liczbe: "))
podstawa = int(input("Podaj podstawe systemu: "))

d = len(b) - 1

for i in range(d, -1, -1):
    pom = MnozPrzezCyfre(b[i], a, podstawa)
    for j in range(d - i):
        pom = pom + '0'
    c = dodaj(c, pom, podstawa)

print(c)