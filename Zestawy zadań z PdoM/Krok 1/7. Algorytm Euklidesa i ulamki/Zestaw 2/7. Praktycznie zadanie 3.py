# Napisz program, który dla danych dodatnich liczb całkowitych a i b, będących długościami boków prostokąta,
# wyznaczy najmniejszą liczbę kwadratów nienachodzących na siebie i całkowicie wypełniających prostokąt.
# Długości boków kwadratów mogą być różne.

def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("Podaj długość boku a: "))
b = int(input("Podaj długość boku b: "))

bok = nwd(a, b)

liczba_kwadratow = a * b // bok ** 2

print(f"Najmniejsza liczba kwadratów wynosi: {liczba_kwadratow}")