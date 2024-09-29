a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = int(input("Podaj trzecią liczbę: "))

lista = [a,b,c]

print(min(lista), a + b + c - max(lista) - min(lista), max(lista))