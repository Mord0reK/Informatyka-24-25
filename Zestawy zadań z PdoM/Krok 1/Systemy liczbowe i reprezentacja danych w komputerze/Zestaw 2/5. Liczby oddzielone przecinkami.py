lista = []

for i in range(0, 10):
    a = int(input("Podaj liczbę: "))
    lista.append(a)

for i in range(len(lista)):
    if i == len(lista) - 1:
        print(lista[i], end=".")
    else:
        print(lista[i], end=",")