a = float(input("Podaj długość pierwszego boku: "))
b = float(input("Podaj długość drugiego boku: "))
c = float(input("Podaj długość trzeciego boku: "))

if b > a:
    a, b = b, a

if c > a:
    a, c = c, a

if b + c > a:
    print("Tak")
else:
    print("Nie")