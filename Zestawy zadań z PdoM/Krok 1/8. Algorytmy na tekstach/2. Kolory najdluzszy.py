kolory = []

for i in range(10):
    kolory.append(str(input(f"Podaj {i+1} kolor: ")))

najwiekszy = kolory[0]

for i in range(10):
    if len(kolory[i]) > len(najwiekszy):
        najwiekszy = kolory[i]

print(najwiekszy)