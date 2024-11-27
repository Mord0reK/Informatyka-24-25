def ile(wzorzec, tekst):
    print("Wzorzec powtórzył się", tekst.count(wzorzec), "razy.")

test = str(input("Podaj Tekst: "))
wzorzec = str(input("Podaj Wzorzec: "))
ile(wzorzec, test)
