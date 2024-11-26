n = int(input("Podaj liczbę n: "))

liczby = []

for i in range(n):
    liczba = int(input(f"Podaj liczbę {i + 1}: "))
    liczby.append(liczba)

def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

wynik = liczby[0]

for i in range(1, n):
    wynik = nwd(wynik, liczby[i])

print(f"NWD podanych liczb wynosi: {wynik}")