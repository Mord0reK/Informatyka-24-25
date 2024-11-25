licznik = int(input("Podaj licznik: "))
mianownik = int(input("Podaj mianownik: "))

while licznik / mianownik >= 0.5:
    print("Podaj ponownie dane")
    licznik = int(input("Podaj licznik: "))
    mianownik = int(input("Podaj mianownik: "))

print(f"Ułamek: {licznik} / {mianownik} mieści się {mianownik // licznik} razy w 1")

