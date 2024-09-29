login = str(input("Podaj login: "))
haslo = str(input("Podaj hasło: "))

login_baza = "tojestlogin"
haslo_baza = "tojesthaslo"

if login == login_baza and haslo == haslo_baza:
    print("Zalogowano pomyślnie")
else:
    print("Błędne dane logowania")