# Napisz program, który będzie obliczać średnią wartość (obciętą do części całkowitej) wszystkich liczb
# wprowadzonych z klawiatury, z pominięciem liczb najmniejszej i największej


wartosc = input("Podaj wartość: ")

liczby = []

while wartosc != "koniec":
    liczby.append(int(wartosc))
    wartosc = input("Podaj wartość: ")


liczby.sort()
liczby.pop(0)
liczby.pop(-1)

print("Średnia wartość: ", sum(liczby) // len(liczby))
