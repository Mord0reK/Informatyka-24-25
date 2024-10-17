tekst = str(input("Podaj tekst: "))
licznika = 0
licznikB = 0

for i in range(len(tekst)):
    if tekst[i] == "a":
        licznika += 1
    if tekst[i] == "B":
        if i % 2 == 0:
            licznikB += 1

print(licznika)
print(licznikB)