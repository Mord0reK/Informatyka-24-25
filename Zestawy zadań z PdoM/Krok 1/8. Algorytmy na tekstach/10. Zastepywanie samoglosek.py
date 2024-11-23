samogloski = ['a', 'e', 'i', 'o', 'u', 'y']

lancuch = str(input("Podaj lańcuch znaków: "))

lancuch.strip(" ")

for i in range(len(lancuch)):
    if lancuch[i] in samogloski:
        lancuch = lancuch.replace(lancuch[i], "_")

print(lancuch)