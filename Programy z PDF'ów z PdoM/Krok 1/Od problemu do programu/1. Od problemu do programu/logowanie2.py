login = str(input("Podaj login: "))
haslo = str(input("Podaj hasło: "))

login_baza = "tojestlogin"
haslo_baza = "tojesthaslo"

if login != login_baza or haslo != haslo_baza:
    print("Błędne dane logowania")
else:
    print("Zalogowano pomyślnie")