# n = int(input("Podaj liczbę dziesiętną: "))
# print(bin(n)[2:])

# a to normalny

dziesietna = int(input("Podaj liczbę dziesiętną: "))
binarny = ""

while dziesietna > 0:
    if dziesietna % 2 == 0:
        binarny = "0" + binarny
    else:
        binarny = "1" + binarny
    dziesietna = dziesietna // 2

print(binarny)