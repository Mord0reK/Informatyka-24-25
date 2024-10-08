#jescze 2 zadania
def wykonaj_algorytm():
    x = 0
    y = 1
    z = 2
    i = 0
    wynik = ""

    while i < 5:  # Pętla dla i od 0 do 4
        j = 0
        while j < 5:  # Pętla dla j od 0 do 4
            if (j + 1) % 3 == 0:  # Warunek: (j + 1) podzielne przez 3
                if i % 2 == 0:
                    wynik += str(z)  # wypisz z
                else:
                    wynik += str(y)  # wypisz y
            else:
                wynik += str(x)  # wypisz x
            
            if j == 1 or j == 3:  # Dodatkowy warunek dla j = 1 lub j = 3
                wynik += str(x)  # wypisz x jeszcze raz
            
            j += 1
        i += 1
    
    return wynik

# Wywołanie funkcji i wyświetlenie wyniku
print("Ciąg znaków po wykonaniu algorytmu:", wykonaj_algorytm())
