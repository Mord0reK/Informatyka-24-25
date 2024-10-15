liczba = int(input("Podaj liczbę: "))
potega = 1
while potega * 2 <= liczba:
    potega *= 2

print("Największa potęga liczby 2 nie większa od", liczba, "to:", potega)
