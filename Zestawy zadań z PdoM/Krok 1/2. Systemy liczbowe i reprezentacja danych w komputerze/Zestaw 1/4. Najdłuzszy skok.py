# Zmodyfikuj program Najdłuższy skok tak, aby trener mógł dodatkowo zliczać liczbę skoków nieważnych
# (spalonych).

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

