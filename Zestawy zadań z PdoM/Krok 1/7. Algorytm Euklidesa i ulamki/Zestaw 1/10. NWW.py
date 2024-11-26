def nwd(a,b):
    while b:
        a, b = b, a % b
    return a

def nww(a,b):
    return a * b // nwd(a, b)

print("NWW:",nww(int(input("Podaj pierwsza liczbe: ")), int(input("Podaj druga liczbe: "))))