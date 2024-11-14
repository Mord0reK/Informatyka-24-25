def Odejmij(a, b):
    return bin(int(a, 2) - int(b, 2))[2:]

a = input("Podaj pierwsza liczbe: ")
b = input("Podaj druga liczbe: ")

ilorazc = "1"
d = len(b)

reszta = a[:d]

if int(reszta, 2) < int(b, 2):
    reszta = reszta + a[d]
    d += 1

reszta = Odejmij(reszta, b)

for i in range(d, len(a)):
    reszta = reszta + a[i]
    if int(reszta, 2) < int(b, 2):
        ilorazc = ilorazc + '0'
    else:
        ilorazc = ilorazc + '1'
        reszta = Odejmij(reszta, b)

print("Iloraz: ", ilorazc)
print("Reszta: ", reszta)