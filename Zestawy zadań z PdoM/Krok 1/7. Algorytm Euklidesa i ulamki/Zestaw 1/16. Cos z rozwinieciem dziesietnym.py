# Napisz program, który wczyta trzy dodatnie liczby jednocyfrowe a, b i c takie, że a ≠ b. Efektem powinna być
# informacja o położeniu cyfry c W rozwinięciu dziesiętnym ułamka a/b. Jeśli taka cyfra się nie pojawia, program
# powinien wypisać liczbę -1.

a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
c = int(input("Podaj liczbę c: "))

if a == b:
    print("a i b nie mogą być takie same")
    exit()

rozwiniecie = a / b

if str(c) in str(rozwiniecie):
    print(f"Liczba {c} znajduje się w rozwinięciu dziesiętnym ułamka w pozycji {str(rozwiniecie).index(str(c)) + 1} od lewej (Włącznie z przecinkiem).")
else:
    print("-1")