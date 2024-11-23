# Napisz program, który dla wyczytanej liczby całkowitej dodatniej policzy, ile jedynek występuje w jej
# reprezentacji binarnej.

liczba = int(input("Podaj liczbę: "))

binarna = bin(liczba)[2:]

print("Liczba jednek w reprezentacji binarnej:", binarna.count("1"))