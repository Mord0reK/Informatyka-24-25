from datetime import datetime

rok_teraz = int(input("Podaj rok teraz: "))
miesiac_teraz = int(input("Podaj miesiąc teraz (1-12): "))
dzien_teraz = int(input("Podaj dzień teraz: "))

rok_urodzenia = int(input("Podaj rok urodzenia: "))
miesiac_urodzenia = int(input("Podaj miesiąc urodzenia (1-12): "))
dzien_urodzenia = int(input("Podaj dzień urodzenia: "))

data_urodzenia = datetime(rok_urodzenia, miesiac_urodzenia, dzien_urodzenia)

wiek = rok_teraz - data_urodzenia.year - ((miesiac_teraz, dzien_teraz) < (data_urodzenia.month, data_urodzenia.day))

if wiek >= 18:
    print("Jesteś pełnoletni.")
else:
    pelnoletnosc = datetime(rok_urodzenia + 18, miesiac_urodzenia, dzien_urodzenia)
    roznica = (pelnoletnosc.year - rok_teraz) * 12 + (pelnoletnosc.month - miesiac_teraz)

    if dzien_teraz > dzien_urodzenia:
        roznica -= 1

    print(f"Nie jesteś jeszcze pełnoletni. Osiągniesz pełnoletniość za {roznica} miesięcy.")
