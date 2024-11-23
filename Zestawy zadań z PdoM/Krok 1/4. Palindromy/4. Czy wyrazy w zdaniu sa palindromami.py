def palindrom(slowo):
    slowo = slowo.upper()
    return slowo == slowo[::-1]

zdanie = str(input("Podaj zdanie: "))

slowa = zdanie.split()
twierdzenie = False


for slowo in slowa:
    if palindrom(slowo):
        twierdzenie = True
    else:
        twierdzenie = False
        break

if twierdzenie:
    print("Tak")
else:
    print("Nie")