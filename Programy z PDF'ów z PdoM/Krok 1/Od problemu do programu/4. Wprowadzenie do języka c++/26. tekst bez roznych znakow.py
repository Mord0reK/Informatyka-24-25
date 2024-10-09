tekst = str(input("Podaj tekst: "))

znaki_rozne_od_h = []
znaki_rowne_a_A_o_O = []


for znak in tekst:
    if znak != "h":
        znaki_rozne_od_h.append(znak)
    if znak == "a" or znak == "A" or znak == "o" or znak == "O":
        znaki_rowne_a_A_o_O.append(znak)

for i in range(len(znaki_rozne_od_h)):
    print(znaki_rozne_od_h[i], end="")
print()

for i in range(len(znaki_rowne_a_A_o_O)):
    print(znaki_rowne_a_A_o_O[i], end="")
print()