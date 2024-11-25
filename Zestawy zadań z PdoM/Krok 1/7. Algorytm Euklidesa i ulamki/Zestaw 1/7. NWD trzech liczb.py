def nwd(a,b):
    while b:
        a, b= b, a % b
    return a

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = int(input("Podaj trzecią liczbę: "))

print(f"NWD liczb: {a}, {b}, {c} wynosi: {nwd(nwd(a,b),c)}")