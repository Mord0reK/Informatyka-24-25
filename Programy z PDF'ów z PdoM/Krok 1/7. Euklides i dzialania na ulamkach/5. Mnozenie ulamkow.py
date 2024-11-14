class wymierna:
    def __init__(self, licz, mian):
        self.licz = licz
        self.mian = mian

def NWD(a ,b):
    while b:
        t = b
        b = a % b
        a = t
    return a

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

def mnoz(a, b):
    c = wymierna(0, 1)
    a = skroc(a)
    b = skroc(b)
    c.licz = a.licz * b.licz
    c.mian = a.mian * b.mian
    return c

a = wymierna(int(input("Podaj licznik a: ")), int(input("Podaj mianownik a: ")))
b = wymierna(int(input("Podaj licznik b: ")), int(input("Podaj mianownik b: ")))

c = mnoz(a, b)
c = skroc(c)
pisz(c)