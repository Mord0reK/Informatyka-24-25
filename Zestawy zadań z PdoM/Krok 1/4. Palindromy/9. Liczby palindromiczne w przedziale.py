print("Liczby mają spełniać warunek: 0 <= a <= b <= 1010")

a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))

while a < 0 or a > 1010 or b < 0 or b > 1010 or a > b:
    print("Liczby nie spełniają warunku: 0 <= a <= b <= 1010")
    a = int(input("Podaj liczbę a: "))
    b = int(input("Podaj liczbę b: "))

for i in range(a, b + 1):
    if str(i) == str(i)[::-1]:
        print(i)
