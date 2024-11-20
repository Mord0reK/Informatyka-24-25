import math

# Funkcja do konwertowania liczby z systemu silniowego na dziesiętny
def silniowy_na_dziesietny(factorial_num):
    decimal_value = 0
    length = len(factorial_num)
    for i in range(length):
        decimal_value += int(factorial_num[length - i - 1]) * math.factorial(i + 1)
    return decimal_value

# Funkcja do konwertowania liczby z dziesiętnego na silniowy system pozycyjny
def dziesietny_na_silniowy(decimal_num):
    factorial_num = []
    i = 1
    while decimal_num > 0:
        factorial_digit = decimal_num % (i + 1)
        factorial_num.append(str(factorial_digit))
        decimal_num //= (i + 1)
        i += 1
    return ''.join(factorial_num[::-1])

num1 = str(input("Podaj pierwszą liczbę w systemie silniowym: "))
num2 = str(input("Podaj drugą liczbę w systemie silniowym: "))

num1, num2 = silniowy_na_dziesietny(num1), silniowy_na_dziesietny(num2)

suma = dziesietny_na_silniowy(num1 + num2)

print(f"Wynik dodawania: {suma}")
