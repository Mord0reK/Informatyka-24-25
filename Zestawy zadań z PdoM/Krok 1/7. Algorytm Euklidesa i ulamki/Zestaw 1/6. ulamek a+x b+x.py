# Napisz program, który wczytuje dwie dodatnie i względnie pierwsze liczby a i b a następnie wyznacza dla nich
# najmniejszą możliwa liczbę x, dla której ułamek 𝑎+𝑥 / 𝑏+𝑥
# jest nieskracalny.

def nwd(a, b):
    while b:
        a, b = b, a % b
    return a


def min_x(a, b):
    if nwd(a, b) != 1:
        print("Liczby a i b muszą być względnie pierwsze.")

    x = 1
    while True:
        if nwd(a + x, b + x) == 1:
            return x
        x += 1

a = int(input("Podaj liczbę a (dodatnią i względnie pierwszą z b): "))
b = int(input("Podaj liczbę b (dodatnią i względnie pierwszą z a): "))

if a <= 0 or b <= 0:
    print("Liczby muszą być dodatnie.")
    a = int(input("Podaj liczbę a (dodatnią i względnie pierwszą z b): "))
    b = int(input("Podaj liczbę b (dodatnią i względnie pierwszą z a): "))

wynik = min_x(a, b)
print(f"Najmniejsza liczba x: {wynik}")