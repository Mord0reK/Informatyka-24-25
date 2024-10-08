#a)
#* - | * - | * - | * - | * - | * - |
#b)
#* & & * * ^ ^ * * * & & * * * * ^ ^
#C)
#* | * - - * | | | * - - - - * I I I I I
#d)
#* | | | $ $ * * | | $ $ $ $ * * * | $ $

#jeden program ktore ma rozne ciagi
#chcesz jeden skopiuj funkcje i printa z dolu powinno zadzialac

def ciag_a():
    wynik = ""
    for _ in range(6):  # powtarzamy 6 razy
        wynik += "* - | "
    wynik = wynik.strip()  # usuwamy końcową spację dla estetyki
    return wynik


def ciag_b():
    wynik = ""
    for i in range(9):  # powtarzamy wzorce zależnie od indeksu
        if i % 3 == 0:
            wynik += "* "
        elif i % 3 == 1:
            wynik += "& & "
        else:
            wynik += "^ ^ "
    wynik = wynik.strip()
    return wynik


def ciag_c():
    wynik = ""
    for i in range(15):  # różna liczba powtórzeń zależnie od wzorca
        if i % 5 == 0:
            wynik += "* "
        elif i % 5 == 1:
            wynik += "| "
        elif i % 5 == 2:
            wynik += "- - "
        elif i % 5 == 3:
            wynik += "| | "
        else:
            wynik += "I I I I I "
    wynik = wynik.strip()
    return wynik


def ciag_d():
    wynik = ""
    for i in range(14):  # różne wzorce w zależności od reszty z dzielenia
        if i % 4 == 0:
            wynik += "* "
        elif i % 4 == 1:
            wynik += "| | "
        elif i % 4 == 2:
            wynik += "$ $ "
        else:
            wynik += "* * "
    wynik = wynik.strip()
    return wynik


# Wypisanie wszystkich ciągów
print("Ciąg a):", ciag_a())
print("Ciąg b):", ciag_b())
print("Ciąg c):", ciag_c())
print("Ciąg d):", ciag_d())
