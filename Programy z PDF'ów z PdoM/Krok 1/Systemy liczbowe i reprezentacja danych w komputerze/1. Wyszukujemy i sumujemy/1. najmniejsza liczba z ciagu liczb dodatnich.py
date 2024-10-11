#Napisz program, który wyznaczy najmniejsza liczbę z ciągu liczb całkowitych dodatnich podawanych z klawiatury.
#Przyjmij, że podanie liczby 0 kończy wprowadzanie liczb.

liczba = int(input("Podaj liczbę: "))

namjmniejsza = liczba

while liczba != 0:
    if liczba < 0:
        print("Podano liczbę ujemną")
    liczba = int(input("Podaj liczbę: "))
    if liczba < namjmniejsza and liczba != 0:
        namjmniejsza = liczba

print("Najmniejsza liczba to: ", namjmniejsza)