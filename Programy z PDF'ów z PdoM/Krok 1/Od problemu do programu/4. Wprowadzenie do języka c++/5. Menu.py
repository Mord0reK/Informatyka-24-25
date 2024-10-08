import datetime
import math

def menu():
    print("\n")
    print("1: Dane ucznia")
    print("2: Aktualna data")
    print("3: Samodzielnie wybrany algorytm")
    print("4: Koniec programu")
    opcja = int(input("Wybierz opcję: "))

    return opcja

opcja = menu()

while opcja != 4:
    if opcja == 1:
        print("Imię: Jan")
        print("Nazwisko: Kowalski")
        print("Wiek: 18")
        print("Klasa: 3A")
    elif opcja == 2:
        print(datetime.date.today())
    elif opcja == 3:
        x = int(input("Podaj argument: "))
        n = int(input("Podaj n: "))

        if n == 1:
            print(math.sqrt(2 * x))
        elif n == 2:
            print(math.pow(x, 3) - 5)
        elif n == 3:
            print(math.cos(x) + 1)
        else:
            print(1)
    elif opcja == 4:
        print("Koniec programu")
        exit()
    else:
        print("Nie ma takiej opcji")

    opcja = menu()