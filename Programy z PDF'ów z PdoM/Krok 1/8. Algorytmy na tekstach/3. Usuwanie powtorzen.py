wyraz = str(input("Podaj pierwszy wyraz: "))

lista = [wyraz]

while wyraz != "":
    wyraz = str(input("Podaj kolejny wyraz: "))
    lista.append(wyraz)

unikalne = []

for wyraz in lista:
    if wyraz not in unikalne:
        unikalne.append(wyraz)

for wyraz in unikalne:
    print(wyraz)
