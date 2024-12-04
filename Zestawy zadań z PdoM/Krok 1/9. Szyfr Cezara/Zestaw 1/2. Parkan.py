tekst = str(input("Podaj tekst do zaszyfrowania: "))

wiersz1 = ""
wiersz2 = ""

for i in range(0, len(tekst), 2):
    wiersz1 = wiersz1 + tekst[i]
for i in range(1, len(tekst), 2):
    wiersz2 = wiersz2 + tekst[i]

print("Zaszyfrowany: ")
print(wiersz1)
print(wiersz2)