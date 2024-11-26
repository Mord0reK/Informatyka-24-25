# Napisz program, który dla dwóch dodatnich liczb całkowitych a i b, będących długościami boków prostokąta,
# wyznaczy najmniejszą liczbę identycznych kwadratów nienachodzących na siebie i całkowicie wypełniających
# prostokąt.

def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("Podaj długość boku a: "))
b = int(input("Podaj długość boku b: "))

bok = nwd(a, b)

liczba_kwadratow = a * b // bok ** 2

print(f"Prostokąt o bokach {a} i {b} można wypełnić {liczba_kwadratow} kwadratami o boku {bok}.")