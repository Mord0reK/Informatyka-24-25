def ciag_a():
    wynik = ""
    for _ in range(6):  # powtarzamy 6 razy
        wynik += "* - | "
    wynik = wynik.strip()  # usuwamy końcową spację dla estetyki
    return wynik
print("Ciąg a):", ciag_a())
