#Ni...

liczba = int(input("Podaj liczbę: "))
dzielniki = [i for i in range(1, liczba + 1) if liczba % i == 0]
print("Dzielniki liczby", liczba, ":", dzielniki)
