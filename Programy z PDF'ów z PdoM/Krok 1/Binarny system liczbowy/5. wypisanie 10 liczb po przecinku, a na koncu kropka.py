liczby = []
for i in range(10):
    liczba = int(input(f"Podaj liczbę {i+1}: "))
    liczby.append(liczba)

print("Liczby:", ", ".join(map(str, liczby)) + ".")
