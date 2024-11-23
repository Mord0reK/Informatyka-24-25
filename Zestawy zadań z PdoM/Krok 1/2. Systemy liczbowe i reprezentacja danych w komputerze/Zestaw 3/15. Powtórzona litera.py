slowo = input("Podaj słowo: ")

unikalne_litery = []

powtorzona_litera = False

for litera in slowo:
    if litera in unikalne_litery:
        powtorzona_litera = True
        break
    else:
        unikalne_litery.append(litera)

# Wypisanie wyniku
if powtorzona_litera:
    print("TAK")
else:
    print("NIE")
