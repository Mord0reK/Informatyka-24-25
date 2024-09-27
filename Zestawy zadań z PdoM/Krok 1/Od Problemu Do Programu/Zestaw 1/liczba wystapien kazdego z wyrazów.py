wyraz1 = str(input("Podaj pierwszy wyraz: "))
wyraz2 = str(input("Podaj drugi wyraz: "))
wyraz3 = str(input("Podaj trzeci wyraz: "))

lista = [wyraz1, wyraz2, wyraz3]

unikalne = []

for wyraz in lista:
    if wyraz not in unikalne:
        unikalne.append(wyraz)

for wyraz in unikalne:
    print(wyraz, lista.count(wyraz))
