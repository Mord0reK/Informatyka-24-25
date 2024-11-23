adres = str(input("Podaj adres e-mail: "))

dl = len(adres)

i = adres.find('@')

if i < 2 or i == -1:
    print("Podano zły adres e-mail!")
    exit()

j = adres.rfind("@")

if i != j:
    print("Podano zły adres e-mail!")
    exit()

k = adres.find(".")

if k == -1 or k < i + 2 or k > dl - 3:
    print("Podano zły adres e-mail!")
    exit()

print("Podano poprawny adres e-mail!")