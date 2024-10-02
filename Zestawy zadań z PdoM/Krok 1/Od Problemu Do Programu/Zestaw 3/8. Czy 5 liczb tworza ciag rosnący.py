a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = int(input("Podaj trzecią liczbę: "))
d = int(input("Podaj czwartą liczbę: "))
e = int(input("Podaj piątą liczbę: "))

lista = [a,b,c,d,e]

if lista == sorted(lista):
    print("Tak")
else:
    print("Nie")