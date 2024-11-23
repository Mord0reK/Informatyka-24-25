def ile(wzorzec, tekst):
    polaczony = " ".join(tekst)

    print("Wzorzec powtórzył się", polaczony.count(wzorzec), "razy.")

test = str(input("Podaj Tekst: "))
wzorzec = str(input("Podaj Wzorzec: "))
ile(wzorzec, test)
