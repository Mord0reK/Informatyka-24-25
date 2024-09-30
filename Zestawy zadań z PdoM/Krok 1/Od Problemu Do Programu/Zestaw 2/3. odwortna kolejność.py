lista = []

liczba = int(input("Podaj liczbę: "))
lista.append(liczba)

while liczba != 0:
    liczba = int(input("Podaj liczbę: "))
    lista.append(liczba)

lista = lista[::-1]

lista.remove(0)

print(lista)