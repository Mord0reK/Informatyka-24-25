def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

dlugosc = float(input("Podaj długość odcinka: "))
szerokosc = float(input("Podaj szerokość odcinka: "))

nwd = nwd(dlugosc, szerokosc)

print("Rozmiar kawałka: ", dlugosc // nwd)
print("Ilość kawałków: ", (szerokosc // nwd) * (dlugosc // nwd))