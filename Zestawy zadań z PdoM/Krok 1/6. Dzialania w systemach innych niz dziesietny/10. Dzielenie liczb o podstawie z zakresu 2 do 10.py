dzielna = input("Podaj liczbę ktorą chcesz podzielić: ")
dzielnik = input("Podaj liczbę (jednocyfrową) przez którą chcesz podzielić: ")
podstawa = int(input("Podaj podstawe systemu liczbowego: "))

dzielna, dzielnik = int(dzielna, podstawa), int(dzielnik, podstawa)

wynik = dzielna // dzielnik

koncowy = ""

while wynik > 0:
    koncowy = str(wynik % podstawa) + koncowy
    wynik = wynik // podstawa

print(f"Wynik dzielenia: {koncowy}")