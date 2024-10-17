podstawa = int(input("Podaj podstawę systemu liczbowego: "))
liczba = input("Podaj liczbę w podanym systemie: ")

wynik = 0

for i in range(len(liczba)):
    if '0' <= liczba[i] <= '9':
        cyfra = ord(liczba[i]) - ord('0')
    else:
        cyfra = ord(liczba[i]) - ord('A') + 10
    wynik = wynik * podstawa + cyfra

print(wynik)