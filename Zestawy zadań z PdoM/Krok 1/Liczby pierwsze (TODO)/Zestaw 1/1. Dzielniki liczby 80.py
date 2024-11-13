liczba = 80

dzielniki = []

for i in range(2, liczba):
    if liczba % i == 0:
        dzielniki.append(i)

print(dzielniki)