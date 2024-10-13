# Napisz program, który będzie grą w zgadywanie ustalonej liczby z przedziału od 0 do 100. Program powinien
# działać do momentu podania przez użytkownika właściwej liczby. Po każdej próbie odgadnięcia liczby program
# powinien wypisać jeden z komunikatów: ”Za mała ” ,”Za duża ” ,”Brawo ! Udało ci się za
# x razem”, gdzie x oznacza liczbę prób, które wykonał użytkownik.

import random

U = 0
liczbaprob = 0
proby = [0] * 100

L = random.randint(0,100)

while True:
    U = int(input("Podaj liczbe: "))
    if U < L:
        print("Za mała")
        liczbaprob += 1
    elif U > L:
        print("Za duza")
        liczbaprob += 1
    if U == L:
        print("Brawo!")
        print("Liczba twoich prob: ", liczbaprob)
        break
