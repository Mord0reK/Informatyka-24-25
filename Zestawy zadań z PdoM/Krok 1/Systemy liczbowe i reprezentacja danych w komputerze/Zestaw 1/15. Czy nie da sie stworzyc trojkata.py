def trojkat(a, b, c):
    return not ((a + b > c) and (a + c > b) and (b + c > a))

n = int(input("Podaj liczbę liczb (n): "))

if n < 3:
    print("Musi być przynajmniej 3 liczby.")
else:
    liczby = []
    for i in range(n):
        liczba = int(input(f"Podaj liczbę {i + 1}: "))
        liczby.append(liczba)

    znaleziono_niezgodnosc = False
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if trojkat(liczby[i], liczby[j], liczby[k]):
                    znaleziono_niezgodnosc = True
                    break
            if znaleziono_niezgodnosc:
                break
        if znaleziono_niezgodnosc:
            break

    if znaleziono_niezgodnosc:
        print("TAK")
    else:
        print("NIE")
