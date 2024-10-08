#nawiasy to po prostu mnozenie niestety ulomny windows nie pozwala uzyc *
def ciag_c(n):
    # Licznik: suma pierwszych n liczb
    licznik = n * (n + 1) // 2
    
    # Mianownik: iloczyn sekwencji rosnącej o 0.5, zaczynającej od 2
    mianownik = 1.0
    for i in range(n):
        mianownik *= 2 + i * 0.5
    
    return licznik / mianownik

# Przykładowe użycie
n = int(input("Podaj n: "))
print("Wartość wyrażenia dla ciągu c):", ciag_c(n))
