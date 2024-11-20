def dzielenie_binarne(dzielna: str, dzielnik: str):

    if dzielnik == "0":
        return "Nie można dzielić przez zero", ""

    # Inicjalizacja zmiennych
    iloraz = ""
    reszta = ""

    # Iteracja po każdym bicie dzielnej
    for bit in dzielna:
        # Przesuwamy resztę w lewo i dodajemy aktualny bit
        reszta += bit

        # Sprawdzamy, czy reszta jest większa lub równa dzielnikowi
        if int(reszta, 2) >= int(dzielnik, 2):
            # Odejmujemy dzielnik i dodajemy '1' do ilorazu
            reszta = bin(int(reszta, 2) - int(dzielnik, 2))[2:]
            iloraz += "1"
        else:
            # Dodajemy '0' do ilorazu
            iloraz += "0"

    # Zapewniamy, że reszta jest w formacie binarnym
    if reszta == "":
        reszta = "0"

    return iloraz, reszta

dzielna = input("Podaj liczbę ktorą chcesz podzielić: ")
dzielnik = input("Podaj liczbę przez którą chcesz podzielić: ")

iloraz, reszta = dzielenie_binarne(dzielna, dzielnik)

print(f"Dzielna: {dzielna} (binarnie) = {int(dzielna, 2)} (dziesiętnie)")
print(f"Dzielnik: {dzielnik} (binarnie) = {int(dzielnik, 2)} (dziesiętnie)")
print(f"Iloraz: {iloraz} (binarnie) = {int(iloraz, 2)} (dziesiętnie)")
print(f"Reszta: {reszta} (binarnie) = {int(reszta, 2)} (dziesiętnie)")
