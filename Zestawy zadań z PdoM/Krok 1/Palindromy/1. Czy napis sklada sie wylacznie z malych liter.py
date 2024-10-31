napis = str(input("Podaj napis: "))

for i in range(len(napis)):
    if napis[i] < 'a' or napis[i] > 'z':
        print("Napis nie składa się wyłącznie z małych liter")
        exit()

print("Napis składa się wyłącznie z małych liter")