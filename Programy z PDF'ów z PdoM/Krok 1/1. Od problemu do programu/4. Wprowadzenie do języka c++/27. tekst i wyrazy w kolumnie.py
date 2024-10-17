tekst = input("Wprowadź tekst: ")

wyrazy = tekst.split()

print("\nWszystkie wyrazy:")
for wyraz in wyrazy:
    print(wyraz)

print("\nWyrazy, których pierwszy i ostatni znak są takie same:")
for wyraz in wyrazy:
    if wyraz[0] == wyraz[-1]:
        print(wyraz)