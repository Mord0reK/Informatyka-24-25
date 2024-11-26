def NWD(a,b):
    while b:
        a, b = b , a % b
    return a

def skroc(a, b):
    nwd = NWD(a, b)
    a = a // nwd
    b = b // nwd
    return a, b

def dziel(a, b):
    wynik = a[0] * b[1], a[1] * b[0]
    wynik = skroc(wynik[0], wynik[1])
    return wynik

a = (int(input("Podaj licznik pierwszego ułamka: ")), int(input("Podaj mianownik pierwszego ułamka: ")))
b = (int(input("Podaj licznik drugiego ułamka: ")), int(input("Podaj mianownik drugiego ułamka: ")))

wynik = dziel(a, b)

print(f"Wynik dzielenia: {wynik[0]}/{wynik[1]}")