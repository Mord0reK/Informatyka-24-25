print("Wprowadź noty za skok lub wpisz 'spalony' dla skoków nieważnych: ")

liczba_spalonych = 0
suma = 0
noty_wazne = 0
noty = []  # Lista do przechowywania ważnych not

for i in range(5):
    nota = input(f"Nota za skok {i+1}: ")

    if nota.lower() == "spalony":
        liczba_spalonych += 1
    else:
        try:
            nota = float(nota)
            noty.append(nota)  # Zapisujemy każdą ważną notę

            if noty_wazne == 0:
                mini = nota
                maks = nota
            else:
                if nota < mini:
                    mini = nota
                if nota > maks:
                    maks = nota
            suma += nota
            noty_wazne += 1
        except ValueError:
            print("Nieprawidłowa wartość, spróbuj ponownie.")
            i -= 1  # Powtórz pytanie dla tej samej noty

if noty_wazne > 0:
    suma -= (mini + maks)  # Odejmij najmniejszą i największą notę
    print("\nNoty skrajne: ", mini, " i ", maks)
    print("Łączna nota: ", suma)
else:
    print("Brak ważnych skoków")

print("Liczba skoków spalonych: ", liczba_spalonych)

# Znalezienie najdłuższej serii rosnących skoków
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
