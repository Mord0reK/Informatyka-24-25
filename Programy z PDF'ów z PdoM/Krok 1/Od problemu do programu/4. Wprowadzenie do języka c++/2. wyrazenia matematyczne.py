import math

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

wyr_1 = math.pow(a, 3) + math.cos(b) * math.sqrt(a + b)
wyr_2 = math.fabs(a - b) + math.sin(a) * math.sqrt(b)
wyr_3 = math.sqrt((3 + math.sqrt(a * b)) / math.fabs(b ** 2 - 20))
wyr_4 = math.sin((math.pow(a + b, 4)) / math.sqrt(11) + math.sin(b))
wyr_5 = math.pow((math.cos(a+1)) / math.fabs(math.sqrt(5) - b), 3)

print("Wynik wyr_1: ", wyr_1)
print("Wynik wyr_2: ", wyr_2)
print("Wynik wyr_3: ", wyr_3)
print("Wynik wyr_4: ", wyr_4)
print("Wynik wyr_5: ", wyr_5)
