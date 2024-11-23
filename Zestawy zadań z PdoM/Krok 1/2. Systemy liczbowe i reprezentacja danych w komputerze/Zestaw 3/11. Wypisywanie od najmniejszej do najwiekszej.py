# Napisz program, który wczyta trzy liczby całkowite i wypisze je w kolejności od najmniejszej do największej

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = int(input("Podaj trzecią liczbę: "))

lista = [a,b,c]

lista.sort()

for i in range(len(lista)):
    print(lista[i], end=" ")