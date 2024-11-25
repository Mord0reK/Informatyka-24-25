licznik1 = int(input("Podaj licznik pierwszego ułamka: "))
mianownik1 = int(input("Podaj mianownik pierwszego ułamka: "))
licznik2 = int(input("Podaj licznik drugiego ułamka: "))
mianownik2 = int(input("Podaj mianownik drugiego ułamka: "))

if licznik1 / mianownik1 > licznik2 / mianownik2:
    print("Pierwszy ułamek jest większy")
elif licznik2 / mianownik2 > licznik1 / mianownik1:
    print("Drugi ułamek jest większy")
else:
    print("Ułamki są równe")