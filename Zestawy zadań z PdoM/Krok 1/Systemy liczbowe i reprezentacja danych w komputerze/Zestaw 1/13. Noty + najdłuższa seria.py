print("Wprowadź noty za skok lub wpisz 'spalony' dla skoków nieważnych: ")

liczba_spalonych = 0
suma = 0
noty = []  # Lista do przechowywania ważnych not

for i in range(5):
    nota = input(f"Nota za skok {i+1}: ")

    if nota.lower() == "spalony":
        liczba_spalonych += 1
    else:
        try:
            nota = float(nota)
            noty.append(nota)
        except ValueError:
            print("Nieprawidłowa wartość, spróbuj ponownie.")
            i -= 1

if len(noty) > 0:
    suma = suma - (min(noty) + max(noty))
    print("\nNoty skrajne: ", min(noty), " i ", max(noty))
    print("Łączna nota: ", suma)
else:
    print("Brak ważnych skoków")

print("Liczba skoków spalonych: ", liczba_spalonych)

najdluzsza_seria = 1
aktualna_seria = 1

for i in range(1, len(noty)):
    if noty[i] > noty[i - 1]:
        aktualna_seria += 1
        if aktualna_seria > najdluzsza_seria:
            najdluzsza_seria = aktualna_seria
    else:
        aktualna_seria = 1

print("Najdłuższa seria rosnących skoków wynosi:", najdluzsza_seria)
