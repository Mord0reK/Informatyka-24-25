binarna = input("Podaj liczbę binarną: ")
dziesietna = 0

for i in range(len(binarna)):
    dziesietna *= 2
    if binarna[i] == "1":
        dziesietna += 1

print(dziesietna)