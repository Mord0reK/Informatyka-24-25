x = float(input("Podaj x: "))

if x < 1:
    print("y = ", 2 * x)
elif x == 1:
    print("y = ", -10)
elif x == 3:
    print("y = ", (x-1)**4)
elif x == 6:
    print("y = ", (x-4)**0.5)
else:
    print("y = ", 0)