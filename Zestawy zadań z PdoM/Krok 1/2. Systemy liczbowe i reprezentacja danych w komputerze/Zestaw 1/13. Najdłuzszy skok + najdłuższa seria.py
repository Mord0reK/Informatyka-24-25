# Zmodyfikuj program Najdłuższy skok tak, aby dodatkowo znajdował najdłuższą serię, w której każdy
# kolejny skok był dłuższy od poprzedniego, a jako wynik wyświetlał liczbę skoków w tej serii. Na przykład dla
# skoków o długości 6,20; 6,30; 6,28; 6,33; 6,40; 6,30; 6,23; program powinien wyświetlić
# odpowiedź 3.

skoki = []
licznik_spalonych = 0

while True:
    skok = input("Podaj długość skoku (dla spalonego wpisz 'spalony', zakończ wpisując '0'): ")
    if skok == '0':
        break
    elif skok.lower() == "spalony":
        licznik_spalonych += 1
    else:
        try:
            skoki.append(float(skok))
        except ValueError:
            print("Nieprawidłowa wartość, spróbuj ponownie.")

if skoki:
    print("Najdłuższy skok:", max(skoki))
else:
    print("Brak ważnych skoków.")

print("Liczba skoków nieważnych:", licznik_spalonych)

najdluzsza_seria = 1
aktualna_seria = 1

for i in range(1, len(skoki)):
    if skoki[i] > skoki[i - 1]:
        aktualna_seria += 1
        if aktualna_seria > najdluzsza_seria:
            najdluzsza_seria = aktualna_seria
    else:
        aktualna_seria = 1

print("Najdłuższa seria rosnących skoków wynosi:", najdluzsza_seria)