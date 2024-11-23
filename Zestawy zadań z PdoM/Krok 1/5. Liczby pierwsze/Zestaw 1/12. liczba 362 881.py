# Liczba 362 881 ma tę własność, że przy dzieleniu przez 2, 3, 4, 5, 6, 7, 8, 9 daje resztę 1.
# Znajdź najmniejszą liczbę o tej własności.

def znajdz_liczbe():
    liczba = 2
    while True:
        # Sprawdzenie, czy liczba daje resztę 1 przy dzieleniu przez każdą z liczb od 2 do 9
        if all(liczba % k == 1 for k in range(2, 10)):
            return liczba
        liczba += 1

wynik = znajdz_liczbe()
print("Najmniejsza liczba o tej własności to:", wynik)
