tekst = str(input("Podaj tekst: "))

for i in range(len(tekst)):
    if tekst[i].isupper():
        print(tekst[i], end="")