tekst = str(input("Podaj tekst: "))

for litera in tekst:
    print(litera, " ", end="")

print()
tekst = tekst[::-1]

for litera in tekst:
    print(litera, " ", end="")

print()

tekst = tekst[::-1]

for i in range(0, len(tekst), 2):
    if i + 1 < len(tekst):
        print(tekst[i], tekst[i + 1], " ", end="")
    else:
        print(tekst[i], " ", end="")
print()

for i in range(0, len(tekst), 3):
    if i + 2 < len(tekst):
        print(tekst[len(tekst) - i - 1], tekst[len(tekst) - i - 2], tekst[len(tekst) - i - 3], "  ", end="")
    else:
        for j in range(3):
            if i + j < len(tekst):
                print(tekst[len(tekst) - i - j - 1], " ", end="")
        print(" ", end="")
print()