a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = int(input("Podaj trzecią liczbę: "))

lista = [a,b,c]

if lista == sorted(lista):
    print("Tak")
else:
    print("Nie")