def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

dlugosc = float(input("Podaj długość odcinka: "))
szerokosc = float(input("Podaj szerokość odcinka: "))

nwd = nwd(dlugosc, szerokosc)

print("Rozmiar kawałka: ", int(dlugosc // nwd))
print("Ilość kawałków: ", int((szerokosc // nwd) * (dlugosc // nwd)))