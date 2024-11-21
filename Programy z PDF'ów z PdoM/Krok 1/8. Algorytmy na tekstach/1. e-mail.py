adres = str(input("Podaj adres e-mail: "))

dlugosc = len(adres)

if not "@" in adres:
    print("Podano zły adres e-mail!")
    exit()

adres = adres.split("@")

if not "." in adres[1]:
    print("Podano zły adres e-mail!")
    exit()

print("Podano poprawny adres e-mail!")