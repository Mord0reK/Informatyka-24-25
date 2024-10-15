#dla podanej liczby ich forma binarna, a nastepnie ich suma? nie rozumiem
#co autor mial na mysli
#juz wiem!

liczba1 = int(input("Podaj pierwszą liczbę dwucyfrową: "))
liczba2 = int(input("Podaj drugą liczbę dwucyfrową: "))

bin1 = bin(liczba1)[2:]
bin2 = bin(liczba2)[2:]
suma_bin = bin(liczba1 + liczba2)[2:]

print(f"Liczba {liczba1} w postaci binarnej: {bin1}")
print(f"Liczba {liczba2} w postaci binarnej: {bin2}")
print("Suma w postaci binarnej:", suma_bin)
