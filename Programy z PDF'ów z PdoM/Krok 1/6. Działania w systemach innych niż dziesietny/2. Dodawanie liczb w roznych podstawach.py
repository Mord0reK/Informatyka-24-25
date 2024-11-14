przn = 0

c = ""

a = input("Podaj pierwsza liczbe: ")
b = input("Podaj druga liczbe: ")
podstawa = int(input("Podaj podstawe systemu liczbowego: "))

while len(a) < len(b):
    a = "0" + a

while len(b) < len(a):
    b = "0" + b

for i in range(len(a) - 1, -1, -1):
    if a[i] <= '9':
        cyfra1 = ord(a[i]) - 48
    else:
        cyfra1 = ord(a[i]) - 55  # Adjust for characters A-F

    if b[i] <= '9':
        cyfra2 = ord(b[i]) - 48
    else:
        cyfra2 = ord(b[i]) - 55  # Adjust for characters A-F

    suma = przn + cyfra1 + cyfra2
    przn = suma // podstawa
    suma = suma % podstawa

    if suma < 10:
        c = chr(suma + 48) + c
    else:
        c = chr(suma + 55) + c  # Adjust for characters A-F

if przn > 0:
    if przn < 10:
        c = chr(przn + 48) + c
    else:
        c = chr(przn + 55) + c

print("Wynik dodawania: ", c)