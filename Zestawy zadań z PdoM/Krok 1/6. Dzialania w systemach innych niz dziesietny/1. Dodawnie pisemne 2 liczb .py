a = "6543"
b = "432"

while len(a) < len(b):
    a = "0" + a

while len(b) < len(a):
    b = "0" + b

wynik = []
przeniesienie = 0

a = a[::-1]
b = b[::-1]

for i in range(len(a)):
    suma = int(a[i]) + int(b[i]) + przeniesienie
    wynik.append(str(suma % 7))
    przeniesienie = suma // 7

# Jeśli na końcu jest przeniesienie, dodajemy je
if przeniesienie:
    wynik.append(str(przeniesienie))

# Składamy wynik w poprawnej kolejności
c = ''.join(reversed(wynik))

print(f"Wynik dodawania {a[::-1]} i {b[::-1]} w systemie siódemkowym to: {c}")
