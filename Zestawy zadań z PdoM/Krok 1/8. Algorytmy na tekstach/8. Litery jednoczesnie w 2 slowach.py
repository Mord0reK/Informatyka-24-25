slowo1 = str(input("Podaj pierwsze słowo: "))
slowo2 = str(input("Podaj drugie słowo: "))

litery = []

for i in range(len(slowo1)):
    if slowo1[i] in slowo2 and slowo2[i] in slowo1:
        litery.append(slowo1[i])

print(litery)