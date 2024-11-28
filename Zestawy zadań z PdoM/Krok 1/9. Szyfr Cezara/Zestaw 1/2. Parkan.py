tekst = str(input("Podaj tekst do zaszyfrowania: "))

wiersz1 = ""
wiersz2 = ""

for i in range(0, len(tekst) -1, 2):
    wiersz1 = wiersz1 + tekst[i]
    wiersz2 = wiersz2 + tekst[i-1]

print("Zaszyfrowany: ")
print(wiersz1)
print(wiersz2)