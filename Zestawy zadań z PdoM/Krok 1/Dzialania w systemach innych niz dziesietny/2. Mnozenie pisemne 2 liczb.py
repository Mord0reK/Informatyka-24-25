a = "6543"
b = "4327"

a_pocz = a
b_pocz = b

while len(a) < len(b):
    a = "0" + a

while len(b) < len(a):
    b = "0" + b

# Zamieniamy liczby na listy cyfr w odwrotnej kolejności
a = list(map(int, a[::-1]))
b = list(map(int, b[::-1]))

# Tablica na wyniki cząstkowe
wyniki_czastkowe = []

for i, cyfra_b in enumerate(b):
    przeniesienie = 0
    wynik_czastkowy = [0] * i  # Dodajemy odpowiednią liczbę zer na początku (przesunięcie miejsca)
    for cyfra_a in a:
        iloczyn = cyfra_a * cyfra_b + przeniesienie
        wynik_czastkowy.append(iloczyn % 7)  # Wynik w bieżącej kolumnie
        przeniesienie = iloczyn // 7        # Przeniesienie do następnej kolumny
    if przeniesienie > 0:
        wynik_czastkowy.append(przeniesienie)
    wyniki_czastkowe.append(wynik_czastkowy)

# Dodawanie wyników cząstkowych w systemie siódemkowym
maks_dlugosc = max(len(w) for w in wyniki_czastkowe)
wynik_koncowy = [0] * maks_dlugosc
przeniesienie = 0

for i in range(maks_dlugosc):
    suma = przeniesienie
    for wynik in wyniki_czastkowe:
        if i < len(wynik):
            suma += wynik[i]
    wynik_koncowy[i] = suma % 7
    przeniesienie = suma // 7

if przeniesienie > 0:
    wynik_koncowy.append(przeniesienie)

c = wynik_koncowy.reverse()
c =  ''.join(map(str, wynik_koncowy))

print(f"Wynik mnożenia {a_pocz} i {b_pocz} w systemie siódemkowym to: {c}")