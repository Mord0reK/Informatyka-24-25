import math

x = float(input("Podaj x: "))

if x < 7:
    print("y = ", x ** 3 + 1)
elif x == 7:
    print("y = ", math.cos(x-1))
elif x == 9:
    print("y = ", (3*x)**0.5)
else:
    print("y = ", -8 * x)