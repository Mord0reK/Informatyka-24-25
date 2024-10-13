# Napisz program, który wypisze pierwszych 100 liczb całkowitych dodatnich podzielnych przez:
# a. 3
# b. 7
# c. 3 i 7

print("Liczby podzielne przez 3:")

for i in range(0, 101):
    if i % 3 == 0:
        print(i, end=" ")
print()

print("Liczby podzielne przez 7:")

for i in range(0, 101):
    if i % 7 == 0:
        print(i, end=" ")
print()

print("Liczby podzielne przez 3 i 7:")

for i in range(0, 101):
    if i % 3 == 0 and i % 7 == 0:
        print(i, end=" ")
print()