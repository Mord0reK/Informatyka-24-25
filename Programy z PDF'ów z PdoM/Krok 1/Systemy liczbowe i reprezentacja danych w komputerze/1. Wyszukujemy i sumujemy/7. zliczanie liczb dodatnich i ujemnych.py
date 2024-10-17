# Napisz program, który zliczy osobno, ile liczb ujemnych i liczb dodatnich wprowadzono z klawiatury. Przyjmij, że
# wczytanie liczby 0 kończy wczytywanie liczb.

liczby = []
dodatnie = 0
ujemne = 0

liczba = int(input("Podaj liczbę: "))

while liczba != 0:
    liczby.append(liczba)
    liczba = int(input("Podaj liczbę: "))

for i in range(len(liczby)):
    if liczby[i] < 0:
        ujemne += 1
    elif liczby[i] == 0:
        continue
    else:
        dodatnie += 1

print("Liczb ujemnych wprowadzono:", ujemne)
print("Liczb dodatnich wprowadzono:", dodatnie)