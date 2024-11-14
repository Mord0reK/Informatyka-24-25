def przeciwnaU2(a):
    a = list(a)  # Convert string to list
    for i in range(len(a)):
        if a[i] == "0":
            a[i] = '1'
        else:
            a[i] = '0'
    a = ''.join(a)  # Convert list back to string
    a = '0' + a
    a = list(a)  # Convert string to list again for further operations
    i = len(a) - 1
    while a[i] == '1':
        a[i] = '0'
        i -= 1
    a[i] = '1'
    return ''.join(a)  # Convert list back to string

a = str(input("Podaj pierwszą liczbę binarną: "))
b = str(input("Podaj drugą liczbę binarną: "))

while len(a) < 8:
    a = "0" + a
while len(b) < 8:
    b = "0" + b

def dodajU2(a, b):
    przn = 0
    c = " "
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
    return c

b = przeciwnaU2(b)
c = dodajU2(a, b)

print("Wynik: ", c)