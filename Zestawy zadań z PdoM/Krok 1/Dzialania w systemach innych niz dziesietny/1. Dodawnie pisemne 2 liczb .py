a = "6543"
b = "432"

while len(a) < len(b):
    a = "0" + a

while len(b) < len(a):
    b = "0" + b

wynik = []
przeniesienie = 0

for i in range(len(a) - 1, -1, -1):
    suma = int(a[i]) + int(b[i]) + przeniesienie
    wynik.append(str(suma % 7))
    przeniesienie = suma // 7

# Jeśli na końcu jest przeniesienie, dodajemy je
if przeniesienie:
    wynik.append(str(przeniesienie))

# Składamy wynik w poprawnej kolejności
c = ''.join(reversed(wynik))

print(f"Wynik dodawania {a} i {b} w systemie siódemkowym to: {c}")
