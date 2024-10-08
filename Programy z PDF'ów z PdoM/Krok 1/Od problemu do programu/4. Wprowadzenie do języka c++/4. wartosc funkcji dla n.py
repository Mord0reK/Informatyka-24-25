import math

x = int(input("Podaj argument: "))
n = int(input("Podaj n: "))

if n == 1:
    print(math.sqrt(2 * x))
elif n == 2:
    print(math.pow(x, 3) - 5)
elif n == 3:
    print(math.cos(x) + 1)
else:
    print(1)