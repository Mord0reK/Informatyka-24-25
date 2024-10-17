a = int(input("Podaj a:"))
x = int(input("Podaj pierwiastek do przyblizenia: "))

while abs(a - (x/a)) > 0.001:
    a = (a + (x/a)) / 2

print(round(a, 4))

