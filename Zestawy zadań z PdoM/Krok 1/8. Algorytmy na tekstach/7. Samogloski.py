samogloski = ['a', 'e', 'i', 'o', 'u', 'y']

lancuch = str(input("Podaj lańcuch znaków: "))

lancuch.strip(" ")

licznik = 0

for i in range(len(lancuch)):
    if lancuch[i] in samogloski:
        licznik += 1

print(f"Liczba samogłosek w podanym łańcuchu znaków wynosi: {licznik}")