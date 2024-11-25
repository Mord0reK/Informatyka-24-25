# Liczby wzglednie pierwsze to liczby ktorych nwd wynosi 1

def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

if nwd(a, b) == 1:
    print("Liczby są względnie pierwsze")
else:
    print("Liczby nie są względnie pierwsze")