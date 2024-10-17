#Napisz program, który wyznaczy najmniejsza liczbę z ciągu liczb całkowitych dodatnich podawanych z klawiatury.
#Przyjmij, że podanie liczby 0 kończy wprowadzanie liczb.

liczba = int(input("Podaj liczbę: "))

liczby = []

while liczba != 0:
    liczby.append(liczba)
    liczba = int(input("Podaj liczbę: "))

print("Najmniejsza liczba: ", min(liczby))