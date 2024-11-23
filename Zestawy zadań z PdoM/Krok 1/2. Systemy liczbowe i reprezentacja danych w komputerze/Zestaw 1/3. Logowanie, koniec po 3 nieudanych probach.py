# Zmodyfikuj kod źródłowy programu Logowanie, tak aby program kończył działanie po trzech nieudanych
# próbach logowania

login = str(input("Podaj login: "))
haslo = str(input("Podaj hasło: "))

login_baza = "tojestlogin"
haslo_baza = "tojesthaslo"

licznik = 1

while licznik < 3:
    if login == login_baza and haslo == haslo_baza:
        print("Zalogowano pomyślnie")
        exit()
    else:
        print("Błędne dane logowania")
        login = str(input("Podaj login: "))
        haslo = str(input("Podaj hasło: "))
        licznik += 1

print("Przekroczono limit prób logowania")
