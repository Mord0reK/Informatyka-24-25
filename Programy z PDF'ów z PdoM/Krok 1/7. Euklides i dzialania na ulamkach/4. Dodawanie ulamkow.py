class wymierna:
    def __init__(self, licz, mian):
        self.licz = licz
        self.mian = mian

def NWD(a,b):
    while b:
        t = b 
        b = a % b
        a = t
    return a

def dodaj(a, b):
    c = wymierna(0, 0)
    nwd1 = NWD(a.mian, b.mian)
    c.licz = a.licz * (b.mian // nwd1) + b.licz * (a.mian // nwd1)
    nwd2 = NWD(abs(c.licz), nwd1)
    c.licz //= nwd2
    c.mian = (a.mian//nwd1) * (b.mian//nwd2)
    return c

def pisz(a):
    if a.licz < 0:
        print('(', end="")
    print(a.licz, end="")
    if a.mian > 1:
        print('/',a.mian, end="")
    if a.licz < 0:
        print(')', end="")

def skroc(a):
    nwd = NWD(a.licz, a.mian)
    a.licz //= nwd
    a.mian //= nwd
    return a

a = wymierna(int(input("Podaj licznik a: ")), int(input("Podaj mianownik a: ")))
b = wymierna(int(input("Podaj licznik b: ")), int(input("Podaj mianownik b: ")))

c = dodaj(a, b)
c = skroc(c)
pisz(c)