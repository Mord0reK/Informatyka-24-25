a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = int(input("Podaj trzecią liczbę: "))
d = int(input("Podaj czwartą liczbę: "))

a_b = a - b
if a_b < 0:
    a_b = -a_b

b_c = b - c
if b_c < 0:
    b_c = -b_c

c_d = c - d
if c_d < 0:
    c_d = -c_d

print(a_b + b_c + c_d)