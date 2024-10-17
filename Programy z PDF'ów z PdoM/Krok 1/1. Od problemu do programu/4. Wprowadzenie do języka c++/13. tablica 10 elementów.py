x = float(input("Podaj x: "))
licznik = 1
tablica = []
tablica.append(x)


while licznik < 10:
    licznik += 1
    x = float(input("Podaj x: "))
    tablica.append(x)

suma = 0
iloczyn = 1

print("Suma: ", sum(tablica))

for i in range(len(tablica)):
    if i < 6:
        iloczyn *= tablica[i]

print("Iloczyn: ", iloczyn)