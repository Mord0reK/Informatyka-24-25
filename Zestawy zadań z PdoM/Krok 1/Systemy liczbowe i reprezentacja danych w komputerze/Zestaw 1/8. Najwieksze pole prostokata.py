# Napisz program, który po wczytaniu 10 liczb wskaże te, które potraktowane jako długości boków utworzą
# prostokąt o największym polu.

liczby = []

liczba = float(input("Podaj liczbę: "))

for _ in range(9):
    liczba = float(input("Podaj liczbę: "))
    liczby.append(liczba)

liczby.sort(reverse=True)

print("Największe pole wynosi: ", liczby[0] * liczby[1])