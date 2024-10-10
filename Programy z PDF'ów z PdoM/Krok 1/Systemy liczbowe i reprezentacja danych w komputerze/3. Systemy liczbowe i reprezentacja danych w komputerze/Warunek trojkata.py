a = float(input("Podaj długość pierwszego boku: "))
b = float(input("Podaj długość drugiego boku: "))
c = float(input("Podaj długość trzeciego boku: "))

if a + b > c and a + c > b and b + c > a:
    print("TAK")
else:
    print("NIE")