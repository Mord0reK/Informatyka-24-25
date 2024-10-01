binarna = str(input("Podaj liczbe binarna 8-io bitową: "))
liczba = 0

while len(binarna) < 8:
    binarna = str(input("Podaj liczbe binarna 8-io bitową: "))

binarna = binarna[::-1]

for i in range(0, 8):
    if binarna[i] == '1':
        liczba += 2**i

print(liczba)