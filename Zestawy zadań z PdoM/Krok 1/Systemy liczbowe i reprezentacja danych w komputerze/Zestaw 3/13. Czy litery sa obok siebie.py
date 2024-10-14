# Napisz program, który wczyta słowo i sprawdzi, czy dwie takie same litery występują w nim obok siebie. Program
# powinien wypisać słowo „TAK” lub „NIE”.

slowo = str(input("Podaj słowo: "))

for i in range(len(slowo)):
    if slowo[i] == slowo[i - 1]:
        print("TAK")
        exit()

print("NIE")