def palindrom(slowo):
    slowo = slowo.lower()
    return slowo == slowo[::-1]

zdanie = str(input("Podaj zdanie: "))

slowa = zdanie.split()

for slowo in slowa:
    if palindrom(slowo):
        print("Słowo", slowo, "jest palindromem")
    else:
        print("Słowo", slowo, "nie jest palindromem")