a = int(input())
b = int(input())

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print(a)