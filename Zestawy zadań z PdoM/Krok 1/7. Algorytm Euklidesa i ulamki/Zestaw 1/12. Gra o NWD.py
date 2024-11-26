# Napisz w języku Python prostą grę dwuosobową, w której pierwszy z graczy podaje dwie liczby naturalne
# mniejsze od 200, a drugi gracz próbuje odgadnąć ich NWD.

# Kolejne próby powinny być numerowane. Po odgadnięciu gracze zamieniają się rolami.

# Wygrywa ten, który poda poprawny wynik w mniejszej liczbie prób.

def nwd(a,b):
    while b:
        a, b = b, a % b
    return a

proby_1 = 0
proby_2 = 0

print("Podaj dwie liczby naturalne mniejsze od 200")

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

while a > 200 or b > 200:
    print("Podane liczby są większe od 200")
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))

nwd_ab = nwd(a,b)

guess = int(input("Podaj NWD podanych liczb: "))

while nwd_ab != guess:
    proby_1 += 1
    print("Pudło!")
    guess = int(input("Podaj NWD podanych liczb: "))

# Po zamianie ról

print("Podaj dwie liczby naturalne mniejsze od 200")

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

while a > 200 or b > 200:
    print("Podane liczby są większe od 200")
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))

nwd_ab = nwd(a,b)

guess = int(input("Podaj NWD podanych liczb: "))

while nwd_ab != guess:
    proby_2 += 1
    print("Pudło!")
    guess = int(input("Podaj NWD podanych liczb: "))

if proby_1 < proby_2:
    print(f"Wygrał gracz 1, wykonując {proby_1 + 1} prób")
else:
    print(f"Wygrał gracz 2, wykonując {proby_2 + 1} prób")

