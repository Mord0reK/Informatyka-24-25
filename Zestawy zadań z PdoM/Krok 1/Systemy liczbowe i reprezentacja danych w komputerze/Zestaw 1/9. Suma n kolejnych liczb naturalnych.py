# Napisz program, który obliczy sumę n kolejnych liczb naturalnych, w którym nie będziesz używać zmiennej
# skladnik, a wartość składnika będzie ustalana na podstawie zmiennej sterującej i .

n = int(input("Podaj liczbę n: "))

suma = 0

for i in range(0, n+1):
    suma += i

print(f"Suma {n} kolejnych liczb naturalnych wynosi: {suma}")
