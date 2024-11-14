def dodaj(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]


a = str(input("Podaj pierwszą liczbę binarną: "))
b = str(input("Podaj drugą liczbę binarną: "))

c = "0"

for i in range(len(b) - 1, -1, -1):
    if b[i] == "1":
        c = dodaj(c, a)
    a = a + "0"

print(c)