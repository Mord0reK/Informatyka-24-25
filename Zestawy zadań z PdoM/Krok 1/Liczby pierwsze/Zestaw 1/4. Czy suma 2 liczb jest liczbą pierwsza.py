def pierwsza(liczba):
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True

print("Podaj liczby do sprawdzenia czy ich suma jest równa liczbą pierwszą (liczba 0 kończy wprowadzanie liczb): ")
liczba = int(input())
sum = 0

while liczba != 0:
    liczba = int(input())
    sum += liczba

print(sum)

if pierwsza(sum):
    print("Suma podanych liczb jest liczbą pierwszą.")
else:
    print("Suma podanych liczb nie jest liczbą pierwszą.")