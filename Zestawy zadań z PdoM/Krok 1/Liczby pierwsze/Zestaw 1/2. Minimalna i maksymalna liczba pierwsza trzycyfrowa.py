def pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

pierwsze = []

for liczba in range(100, 1000):
    if pierwsza(liczba):
        pierwsze.append(liczba)

print("Minimalna: ", min(pierwsze))
print("Maksymalna: ", max(pierwsze))