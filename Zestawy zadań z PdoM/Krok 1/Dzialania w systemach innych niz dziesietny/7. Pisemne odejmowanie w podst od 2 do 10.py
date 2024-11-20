a = input("Podaj odejmną: ")
b = input("Podaj odejmnik: ")
podstawa = int(input("Podaj podstawę systemu liczbowego (od 2 do 10): "))

while podstawa < 2 or podstawa > 10:
    print("Podstawa musi być w zakresie od 2 do 10.")
    podstawa = int(input("Podaj podstawę systemu liczbowego (od 2 do 10): "))

wynik = []
pozycja = 0
pozyczenie = 0  # Przeniesienie między kolumnami.

while len(a) < len(b):
    a = "0" + a
while len(b) < len(a):
    b = "0" + b

for i in range(len(a) - 1, -1, -1):
    odejmna = int(a[i]) - pozyczenie
    odejmnik = int(b[i])

    if odejmna < odejmnik:
        odejmna += podstawa
        pozyczenie = 1
    else:
        pozyczenie = 0

    wynik.append(str(odejmna - odejmnik))

print("Wynik: ", ''.join(reversed(wynik)).lstrip('0'))
