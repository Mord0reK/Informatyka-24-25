miejscowosc = str(input("Podaj nazwe miejscowosci: "))

miejscowosc.strip(" ")

for i in range(0, len(miejscowosc), 2):
    print(miejscowosc[i], end=" ")