przn = 0

c = " "

a = input("Podaj pierwsza liczbe binarna: ")
b = input("Podaj druga liczbe binarna: ")

while len(a) < len(b):
    a = "0" + a

while len(b) < len(a):
    b = "0" + b

for i in range(len(a) - 1, -1, -1):
    suma = przn + ord(a[i]) - 48 + ord(b[i]) - 48
    if suma % 2 == 1:
        c = "1" + c
    else:
        c = "0" + c
    przn = suma // 2  # Use floor division to get an integer result

if przn == 1:
    c = "1" + c

print("Wynik dodawania: ", c)