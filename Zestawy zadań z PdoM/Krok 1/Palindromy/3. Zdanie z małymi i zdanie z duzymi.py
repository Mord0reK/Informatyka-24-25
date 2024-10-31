zdanie = str(input("Wprowadź zdanie: "))

wyrazy = zdanie.split()
sformatowane = [wyraz.capitalize() for wyraz in wyrazy]
print("Sformatowane zdanie: ", ' '.join(sformatowane))
