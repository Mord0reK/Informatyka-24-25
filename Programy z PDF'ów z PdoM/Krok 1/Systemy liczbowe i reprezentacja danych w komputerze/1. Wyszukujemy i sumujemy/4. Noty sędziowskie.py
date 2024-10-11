#Program Noty sędziowskie
print("Wprowadź noty za skok: ")
nota = float(input())
mini = nota
maks = nota
suma = nota
for i in range(4):
    nota = float(input())
    suma += nota
    if nota < mini:
        mini = nota
    if nota > maks:
        maks = nota

suma -= mini - maks
print("\nNoty skrajne : ", mini," i ", maks)
print(" Łączna nota : ", suma)