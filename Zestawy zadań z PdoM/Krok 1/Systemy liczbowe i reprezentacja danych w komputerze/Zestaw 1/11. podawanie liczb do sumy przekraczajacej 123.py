# Napisz program, który będzie wczytywał podane przez użytkownika liczby jedno i dwucyfrowe całkowite i
# sumował je do momentu otrzymania sumy przekraczającej 123. Program powinien zwrócić informację o liczbie
# składników sumy i wartość sumy.

suma = 0
liczby = []

while suma <= 123:
    liczba = int(input("Podaj liczbę: "))
    liczby.append(liczba)
    if liczba < 10 or liczba > 99:
        print("Podana liczba nie jest dwucyfrowa")
        continue
    suma += liczba

print("Suma przekroczyła 123. Liczba składników sumy: ", len(liczby)," wartość sumy: ", suma)
