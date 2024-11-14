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

def skroc(a):
    nwd = NWD((abs(a.licz)), abs(a.mian))
    a.licz //= nwd
    a.mian //= nwd
    return a

a = wymierna(int(input()), int(input()))
a = skroc(a)
print(a.licz, "/", a.mian)