# Napisz program sprawdzający warunek istnienia trójkąta. Zastosuj w nim alternatywę zdań.

a = float(input("Podaj długość boku a: "))
b = float(input("Podaj długość boku b: "))
c = float(input("Podaj długość boku c: "))

if (a + b < c) or (a + c < b) or (b + c < a):
    print("Taki trójkąt nie może istnieć.")
else:
    print("Taki trójkąt może istnieć.")
