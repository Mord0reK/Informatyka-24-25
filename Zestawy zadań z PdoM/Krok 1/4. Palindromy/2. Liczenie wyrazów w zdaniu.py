zdanie = str(input("Podaj zdanie: "))

liczba_wyrazow = 1

for i in range(len(zdanie)):
    if zdanie[i] == ' ':
        liczba_wyrazow += 1

print("Zdanie składa się z", liczba_wyrazow, "wyrazów")