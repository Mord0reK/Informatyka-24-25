dziesietna = int(input("Podaj liczbę w systemie dziesiętnym: "))

binarna = bin(dziesietna)

print("Liczba dziesiętna",dziesietna, "do zapisania w systemie binarnym wymaga", len(binarna) - 2, "cyfr.")