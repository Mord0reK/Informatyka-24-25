slowo = str(input("Podaj słowo: "))

ile = 0

for i in range(len(slowo)):
    ile += 1

print(f"W słowie {slowo} jest {ile} liter.")