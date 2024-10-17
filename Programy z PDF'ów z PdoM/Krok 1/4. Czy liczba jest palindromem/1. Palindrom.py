slowo = str(input("Podaj słowo: "))

if slowo == slowo[::-1]:
    print("Słowo jest palindromem")
else:
    print("Słowo nie jest palindromem")