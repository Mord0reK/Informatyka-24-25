def pierwsza(liczba):
    if liczba < 2 and liczba % 2 == 0:
        return False
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True

for i in range(100):
    if pierwsza(i):
        print(i)

