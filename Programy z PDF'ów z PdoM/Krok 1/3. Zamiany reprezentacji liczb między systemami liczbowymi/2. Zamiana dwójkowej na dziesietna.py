binarna = str(input("Podaj liczbe binarna: "))
dziesietna = 0

binarna = binarna[::-1]

for i in range(len(binarna)):
    if binarna[i] == '1':
        dziesietna += 2**i

print(dziesietna)