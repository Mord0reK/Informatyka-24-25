#windows jak zwykle utrudnia pisanie nazw plikow 
def ciag_d(n):
    # Licznik: iloczyn rosnących wartości w potęgach 10
    licznik = 1
    for i in range(n):
        licznik *= (-3) * (10 ** -i)

    # Mianownik: suma wyrazów o różnicy 5 z naprzemiennym znakiem
    mianownik = 0
    for i in range(1, n + 1):
        wyraz = (-1) ** (i + 1) * (5 * i - 2)
        mianownik += wyraz
    
    return licznik / mianownik

# Przykładowe użycie
n = int(input("Podaj n: "))
print("Wartość wyrażenia dla ciągu d):", ciag_d(n))
