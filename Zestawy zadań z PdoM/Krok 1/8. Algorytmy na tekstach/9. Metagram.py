slowo1 = str(input("Podaj pierwsze słowo: "))
slowo2 = str(input("Podaj drugie słowo: "))

roznice = 0

if len(slowo1) != len(slowo2):
    print(f"Słowa {slowo1} i {slowo2} nie są metagramami")
else:
    for i in range(len(slowo1)):
        if slowo1[i] != slowo2[i]:
            roznice += 1
    if roznice == 1:
        print(f"Słowa {slowo1} i {slowo2} są metagramami")
    else:
        print(f"Słowa {slowo1} i {slowo2} nie są metagramami")
