x = int(input("Podaj x: "))
y = int(input("Podaj y: "))

while x < 0:
    x = int(input("Podaj x: "))
while y < 0:
    y = int(input("Podaj y: "))

x_silnia = 1
y_silnia = 1
suma = 0

for i in range(1, x + 1):
    x_silnia *= i

for i in range(1, y + 1):
    y_silnia *= i

for i in range(0, y + 1):
    suma = suma + i

w = (x_silnia + y_silnia) / suma

print(w)