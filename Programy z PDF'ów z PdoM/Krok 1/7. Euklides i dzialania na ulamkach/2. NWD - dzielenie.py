a = int(input())
b = int(input())

while b:
    t = b
    b = a % b
    a = t

print(a)