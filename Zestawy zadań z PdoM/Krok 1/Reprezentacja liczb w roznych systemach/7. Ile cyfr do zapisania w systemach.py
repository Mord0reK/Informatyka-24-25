import math

def oblicz_cyfry(bity):
    cyfry_czworkowe = math.ceil(bity / 2)
    cyfry_osemkowe = math.ceil(bity / 3)
    cyfry_szesnastkowe = math.ceil(bity / 4)
    return cyfry_czworkowe, cyfry_osemkowe, cyfry_szesnastkowe

bity = int(input("Podaj liczbę cyfr potrzebnych do zapisania liczby binarnej: "))

czworkowy, osemkowy, szesnastkowy = oblicz_cyfry(bity)

print(f"Liczba cyfr w systemie czwórkowym: {czworkowy}")
print(f"Liczba cyfr w systemie ósemkowym: {osemkowy}")
print(f"Liczba cyfr w systemie szesnastkowym: {szesnastkowy}")
